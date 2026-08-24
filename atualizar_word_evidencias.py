from pathlib import Path
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches

DOC_PATH = Path(r'C:\Users\priot\OneDrive\Área de Trabalho\Plano_de_Testes_Bloqueio_Usuarios_Hub_de_Leitura.docx')
IMAGES = [
    ('CT01', 'Bloqueio após 8 dias', Path(r'C:\Users\priot\OneDrive\Área de Trabalho\CURSO ENGENHARIA DA QUALIDADE DE SOFTWARE\EXERCÍCIOS\M30\plano-testes-hub-leitura\docs\prints-resultados\01-CT01-bloqueio-8-dias.png')),
    ('CT02', 'Validação do limite de 7 dias', Path(r'C:\Users\priot\OneDrive\Área de Trabalho\CURSO ENGENHARIA DA QUALIDADE DE SOFTWARE\EXERCÍCIOS\M30\plano-testes-hub-leitura\docs\prints-resultados\02-CT02-limite-7-dias.png')),
    ('CT05', 'Usuário bloqueado tenta reservar', Path(r'C:\Users\priot\OneDrive\Área de Trabalho\CURSO ENGENHARIA DA QUALIDADE DE SOFTWARE\EXERCÍCIOS\M30\plano-testes-hub-leitura\docs\prints-resultados\03-CT05-bloqueio-reserva.png')),
    ('CT06', 'Usuário bloqueado tenta renovar', Path(r'C:\Users\priot\OneDrive\Área de Trabalho\CURSO ENGENHARIA DA QUALIDADE DE SOFTWARE\EXERCÍCIOS\M30\plano-testes-hub-leitura\docs\prints-resultados\04-CT06-bloqueio-renovacao.png')),
    ('CT10', 'Desbloqueio após devolução', Path(r'C:\Users\priot\OneDrive\Área de Trabalho\CURSO ENGENHARIA DA QUALIDADE DE SOFTWARE\EXERCÍCIOS\M30\plano-testes-hub-leitura\docs\prints-resultados\05-CT10-desenvolucao-bloqueio.png')),
    ('CT11', 'Dois livros atrasados', Path(r'C:\Users\priot\OneDrive\Área de Trabalho\CURSO ENGENHARIA DA QUALIDADE DE SOFTWARE\EXERCÍCIOS\M30\plano-testes-hub-leitura\docs\prints-resultados\06-CT11-dois-livros-atrasados.png')),
]


def format_paragraph(paragraph, align='left'):
    if align == 'center':
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    else:
        paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT


def ensure_section(doc):
    target = '5. Estratégia de testes'
    for p in doc.paragraphs:
        if p.text.strip() == target:
            title = p.insert_paragraph_before('4.1 Evidências de execução dos cenários')
            title.style = 'Heading 2'
            intro = p.insert_paragraph_before(
                'Abaixo estão os principais prints gerados durante a execução dos cenários de teste de bloqueio automático. '
                'As evidências reforçam o comportamento esperado e a consistência entre regra de negócio, API e interface.'
            )
            format_paragraph(intro)
            p.insert_paragraph_before('')
            break
    else:
        title = doc.add_paragraph('4.1 Evidências de execução dos cenários')
        title.style = 'Heading 2'
        intro = doc.add_paragraph(
            'Abaixo estão os principais prints gerados durante a execução dos cenários de teste de bloqueio automático. '
            'As evidências reforçam o comportamento esperado e a consistência entre regra de negócio, API e interface.'
        )
        format_paragraph(intro)

    table = doc.add_table(rows=1, cols=4)
    table.style = 'Table Grid'
    hdr = table.rows[0].cells
    hdr[0].text = 'ID'
    hdr[1].text = 'Cenário'
    hdr[2].text = 'Status'
    hdr[3].text = 'Observação'

    data = [
        ('CT01', 'Bloqueio após 8 dias', 'PASS', 'Usuário bloqueado conforme regra'),
        ('CT02', 'Limite de 7 dias', 'PENDENTE', 'Confirmar regra > 7 ou >= 7'),
        ('CT05', 'Usuário bloqueado tenta reservar', 'PASS', 'Reserva recusada'),
        ('CT06', 'Usuário bloqueado tenta renovar', 'PASS', 'Renovação negada'),
        ('CT10', 'Desbloqueio após devolução', 'PASS', 'Bloqueio removido'),
        ('CT11', 'Dois livros atrasados', 'PASS', 'Bloqueio mantido'),
    ]

    for row in data:
        cells = table.add_row().cells
        for i, value in enumerate(row):
            cells[i].text = value

    doc.add_paragraph('')


def add_image_section(doc, test_id, title, image_path):
    title_paragraph = doc.add_paragraph(f'{test_id} – {title}')
    title_paragraph.runs[0].bold = True
    format_paragraph(title_paragraph)

    img = doc.add_picture(str(image_path), width=Inches(6.5))
    img.alignment = 1

    caption = doc.add_paragraph(f'Figura: {test_id} – {title}. Evidência visual do cenário executado.')
    format_paragraph(caption)
    doc.add_paragraph('')


def main():
    doc = Document(DOC_PATH)
    ensure_section(doc)

    for test_id, title, image_path in IMAGES:
        if not image_path.exists():
            print(f'Imagem não encontrada: {image_path}')
            continue
        add_image_section(doc, test_id, title, image_path)

    doc.save(DOC_PATH)
    print(f'Arquivo atualizado com {len(IMAGES)} imagens: {DOC_PATH}')
    print(f'Quantidade de imagens no documento: {len(doc.inline_shapes)}')


if __name__ == '__main__':
    main()
