# 1. Análise da História de Usuário

## História

**Como** administrador da biblioteca  
**Quero** que o sistema bloqueie automaticamente usuários que possuem livros em atraso por mais de 7 dias  
**Para** evitar que continuem realizando novas reservas até regularizarem a devolução do livro.

## Análise

A história apresenta uma regra central clara, porém existem pontos que precisam ser esclarecidos antes da implementação e da execução definitiva dos testes.

## Possíveis ambiguidades

1. O bloqueio ocorre somente quando o atraso é maior que 7 dias ou também exatamente no 7º dia?
2. Como o sistema calcula o atraso: por data, hora, fuso horário ou apenas diferença entre dias corridos?
3. O que acontece quando o usuário possui vários livros e apenas um deles está atrasado?
4. O bloqueio ocorre imediatamente ao atingir o limite ou por uma rotina agendada?
5. Depois da devolução, o desbloqueio é imediato ou depende de processamento posterior?
6. O bloqueio manual pode ser removido automaticamente pelo sistema?
7. Se o administrador remover manualmente um bloqueio enquanto ainda existe atraso superior a 7 dias, o sistema deve bloquear novamente?
8. O que acontece com reservas já existentes quando o bloqueio é aplicado?
9. Renovação significa renovar empréstimo, reserva ou ambos?
10. Qual mensagem deve ser apresentada ao usuário?
11. Quais informações devem aparecer exatamente no painel administrativo?
12. O sistema deve registrar histórico das ações de bloqueio e desbloqueio?

## Perguntas para o time de produto

1. Confirmar se a regra é `> 7 dias` ou `>= 7 dias`.
2. Definir se são considerados dias corridos e qual timezone será utilizado.
3. Definir o momento em que o bloqueio automático será processado.
4. Definir o comportamento quando houver múltiplos empréstimos.
5. Definir se a devolução remove o bloqueio imediatamente.
6. Definir a prioridade entre bloqueio automático e desbloqueio manual.
7. Definir se bloqueios e desbloqueios serão registrados em histórico/auditoria.
8. Definir mensagens exibidas para usuário e administrador.
9. Definir o comportamento de reservas já existentes.
10. Definir quais administradores terão permissão para remover bloqueios.

## Regras que precisam de detalhamento

- Limite exato do atraso.
- Critério de bloqueio com múltiplos livros.
- Critério de desbloqueio quando outro livro continua atrasado.
- Persistência do bloqueio.
- Auditoria de ações.
- Permissões administrativas.
- Tratamento de falhas na rotina automática.
