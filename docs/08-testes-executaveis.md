# 8. Testes Executáveis

## Objetivo

Executar os cenários críticos da funcionalidade de bloqueio automático de usuários com empréstimos em atraso, validando comportamento esperado, mensagens exibidas e persistência do status.

## Procedimento geral

1. Preparar massa de dados com usuários em situação regular e com atraso.
2. Validar a regra de negócio aplicada ao cálculo de dias de atraso.
3. Executar a rotina de bloqueio.
4. Confirmar que o usuário não consegue realizar novas reservas ou renovações.
5. Validar o painel administrativo e a mensagem ao usuário.
6. Simular devolução e confirmar o desbloqueio quando a regra permitir.

## Matriz de execução

| ID | Cenário | Passos principais | Resultado esperado | Status |
|---|---|---|---|---|
| CT01 | Usuário com 8 dias de atraso | Acessar conta, verificar empréstimo, executar rotina | Usuário bloqueado automaticamente | Executável |
| CT02 | Usuário com 7 dias de atraso | Validar regra do limite | Comportamento conforme regra do produto | Executável |
| CT03 | Usuário com 6 dias de atraso | Validar dias antes do limite | Usuário continua desbloqueado | Executável |
| CT04 | Usuário sem atraso | Verificar histórico de empréstimos | Permanece sem bloqueio | Executável |
| CT05 | Usuário bloqueado tenta reservar | Acessar reserva | Operação negada com mensagem adequada | Executável |
| CT06 | Usuário bloqueado tenta renovar | Acessar renovação | Renovação recusada | Executável |
| CT07 | Status no perfil do usuário | Acessar perfil | Exibe status e motivo do bloqueio | Executável |
| CT08 | Painel administrativo | Consultar painel | Visualiza usuário bloqueado e dias de atraso | Executável |
| CT09 | Lista de bloqueados | Abrir lista | Exibe usuários, motivo e atraso | Executável |
| CT10 | Devolução do livro | Devolver item em atraso | Bloqueio removido quando não houver outro atraso elegível | Executável |
| CT11 | Dois livros atrasados | Devolver um dos dois | Bloqueio continua se outro livro ainda atender à regra | Executável |
| CT12 | Desbloqueio manual | Usuário admin remove bloqueio | Bloqueio removido conforme permissão | Executável |
| CT13 | Usuário sem permissão | Tentar remover bloqueio | Operação negada | Executável |
| CT14 | Falha no cálculo | Simular dados inconsistentes | Sistema registra erro e não bloqueia indevidamente | Executável |
| CT15 | Falha na rotina automática | Interromper processamento | Sistema reprocessa ou registra falha | Executável |
| CT16 | Reinicialização após bloqueio | Recarregar fluxo | Status permanece consistente | Executável |
| CT17 | Integração API x interface | Consultar API e tela | Dados consistentes entre camadas | Executável |
| CT18 | Mensagem de bloqueio | Tentar reserva/renovação | Mensagem informa motivo e restrições | Executável |

## Critérios de aceite para execução

- O usuário deve receber retorno claro quando a ação for negada.
- O status de bloqueio deve refletir a regra de negócio em tempo real.
- Resultados da API e da interface devem ser consistentes.
- Desbloqueio só deve ocorrer quando o usuário deixar de atender à regra.
- Ações administrativas devem respeitar permissões.

## Registro de evidência

As evidências de execução devem ser armazenadas na pasta:

- `docs/prints-resultados/`

Cada print deve conter:

- ID do teste;
- nome do cenário;
- data e hora da execução;
- resultado obtido;
- observações relevantes.

## Resultados executados

| ID | Cenário | Resultado | Evidência |
|---|---|---|---|
| CT01 | Bloqueio após 8 dias | PASS | [01-CT01-bloqueio-8-dias.png](prints-resultados/01-CT01-bloqueio-8-dias.png) |
| CT02 | Validação do limite de 7 dias | PENDENTE/CONFIRMAR REGRA | [02-CT02-limite-7-dias.png](prints-resultados/02-CT02-limite-7-dias.png) |
| CT05 | Usuário bloqueado tenta reservar | PASS | [03-CT05-bloqueio-reserva.png](prints-resultados/03-CT05-bloqueio-reserva.png) |
| CT06 | Usuário bloqueado tenta renovar | PASS | [04-CT06-bloqueio-renovacao.png](prints-resultados/04-CT06-bloqueio-renovacao.png) |
| CT10 | Desbloqueio após devolução | PASS | [05-CT10-desenvolucao-bloqueio.png](prints-resultados/05-CT10-desenvolucao-bloqueio.png) |
| CT11 | Dois livros atrasados | PASS | [06-CT11-dois-livros-atrasados.png](prints-resultados/06-CT11-dois-livros-atrasados.png) |

## Automação do processo

O processo foi deixado automatizado por meio do script:

- `gerar_evidencias_testes.py`

Esse script gera automaticamente todos os prints e também o resumo em markdown em `docs/prints-resultados/resultados-testes.md`.

## Observação

Esta estrutura foi organizada para que os testes fiquem executáveis, rastreáveis e com geração automatizada de evidências visuais.
