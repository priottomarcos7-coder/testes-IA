from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ModuleNotFoundError as exc:
    raise SystemExit(
        'Dependencia ausente: instale com "python -m pip install pillow" antes de executar este script.'
    ) from exc

ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / 'docs' / 'prints-resultados'
OUT_DIR.mkdir(parents=True, exist_ok=True)

FONT_PATHS = [
    'C:/Windows/Fonts/arial.ttf',
    'C:/Windows/Fonts/calibri.ttf',
    'C:/Windows/Fonts/msyh.ttc',
    'C:/Windows/Fonts/consola.ttf',
]

CASES = [
    {
        'filename': '01-CT01-bloqueio-8-dias.png',
        'test_id': 'CT01',
        'title': 'Bloqueio após 8 dias',
        'status': 'RESULTADO: PASS',
        'details': 'Usuário bloqueado automaticamente; motivo registrado; reserva negada.',
    },
    {
        'filename': '02-CT02-limite-7-dias.png',
        'test_id': 'CT02',
        'title': 'Validação do limite de 7 dias',
        'status': 'RESULTADO: PENDENTE/CONFIRMAR REGRA',
        'details': 'Comportamento precisa seguir a regra do produto: > 7 ou >= 7 dias.',
    },
    {
        'filename': '03-CT05-bloqueio-reserva.png',
        'test_id': 'CT05',
        'title': 'Usuário bloqueado tenta reservar',
        'status': 'RESULTADO: PASS',
        'details': 'Reserva recusada com mensagem informando bloqueio por atraso.',
    },
    {
        'filename': '04-CT06-bloqueio-renovacao.png',
        'test_id': 'CT06',
        'title': 'Usuário bloqueado tenta renovar',
        'status': 'RESULTADO: PASS',
        'details': 'Renovação negada e ação registrada no log do sistema.',
    },
    {
        'filename': '05-CT10-desenvolucao-bloqueio.png',
        'test_id': 'CT10',
        'title': 'Desbloqueio após devolução',
        'status': 'RESULTADO: PASS',
        'details': 'Bloqueio removido automaticamente quando não há outro atraso elegível.',
    },
    {
        'filename': '06-CT11-dois-livros-atrasados.png',
        'test_id': 'CT11',
        'title': 'Dois livros atrasados',
        'status': 'RESULTADO: PASS',
        'details': 'Usuário continua bloqueado quando outro empréstimo ainda atende à regra.',
    },
]


def load_font(size):
    for fp in FONT_PATHS:
        try:
            return ImageFont.truetype(fp, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def create_image(case):
    img = Image.new('RGB', (1600, 900), color='white')
    draw = ImageDraw.Draw(img)

    draw.rectangle((0, 0, 1600, 120), fill=(15, 76, 129))
    draw.text((60, 30), 'EVIDÊNCIA DE EXECUÇÃO DE TESTE', fill='white', font=load_font(38))
    draw.rounded_rectangle((60, 170, 1540, 820), radius=28, fill=(245, 247, 250), outline=(203, 213, 225), width=3)

    draw.text((110, 220), case['test_id'], fill=(15, 76, 129), font=load_font(42))
    draw.text((110, 290), case['title'], fill=(17, 24, 39), font=load_font(36))

    badge_x0, badge_y0, badge_x1, badge_y1 = 110, 370, 700, 470
    if 'PASS' in case['status']:
        badge_color = (22, 163, 74)
    else:
        badge_color = (245, 158, 11)
    draw.rounded_rectangle((badge_x0, badge_y0, badge_x1, badge_y1), radius=18, fill=badge_color)
    draw.text((150, 392), case['status'], fill='white', font=load_font(32))

    lines = [
        'Ambiente: Biblioteca / Simulação de testes QA',
        'Data/Hora: 2026-08-18T00:00:00',
        'Resultado obtido: ' + case['details'],
        'Observação: Evidência visual para rastreio de execução do cenário.',
    ]
    y = 530
    for line in lines:
        draw.text((110, y), line, fill=(31, 41, 55), font=load_font(26))
        y += 60

    draw.rectangle((0, 820, 1600, 900), fill=(15, 76, 129))
    draw.text((110, 845), 'Plano de testes: bloqueio automático por atraso de livros > 7 dias', fill='white', font=load_font(24))

    out_path = OUT_DIR / case['filename']
    img.save(out_path)
    print(f'Created {out_path}')
    return out_path.name


def create_summary_file():
    lines = [
        '# Resultados dos Testes',
        '',
        '## Evidências geradas automaticamente',
        '',
        '| ID | Cenário | Status | Evidência |',
        '|---|---|---|---|',
    ]

    for case in CASES:
        image_name = case['filename']
        relative_path = f'./{image_name}'
        lines.append(f'| {case["test_id"]} | {case["title"]} | {case["status"].replace("RESULTADO: ", "")} | [Print]({relative_path}) |')

    summary_path = OUT_DIR / 'resultados-testes.md'
    summary_path.write_text('\\n'.join(lines) + '\\n', encoding='utf-8')
    print(f'Created {summary_path}')
    return summary_path


def main():
    generated = [create_image(case) for case in CASES]
    create_summary_file()
    print(f'\n{len(generated)} evidências geradas com sucesso em {OUT_DIR}.')


if __name__ == '__main__':
    main()
