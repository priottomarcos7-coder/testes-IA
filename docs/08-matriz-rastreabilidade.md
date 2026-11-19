# Matriz de Rastreabilidade — Bloqueio por atraso

Esta matriz relaciona os requisitos e regras identificados na história de usuário aos cenários de teste planejados. Ela ajuda a visualizar a cobertura e os pontos que ainda dependem de esclarecimento.

| ID | Requisito / regra a validar | Cenários relacionados | Situação |
|---|---|---|---|
| RF01 | Bloquear automaticamente usuário com atraso superior a 7 dias | CT01, CT14, CT15 | Regra principal descrita na história |
| RF02 | Não bloquear usuário abaixo do limite | CT03, CT04 | A validar |
| RF03 | Definir comportamento no limite exato de 7 dias | CT02 | Pendente de confirmação do produto |
| RF04 | Impedir novas reservas de usuário bloqueado | CT05 | A validar |
| RF05 | Impedir renovação de usuário bloqueado | CT06 | A validar |
| RF06 | Exibir status e motivo do bloqueio | CT07, CT08, CT09, CT18 | Detalhes de interface pendentes |
| RF07 | Remover bloqueio após regularização | CT10 | Momento e condição de desbloqueio pendentes |
| RF08 | Manter bloqueio se outro empréstimo continuar elegível | CT11 | A validar com produto |
| RF09 | Permitir desbloqueio manual somente a perfil autorizado | CT12, CT13 | Permissões pendentes |
| RF10 | Manter consistência entre API e interface | CT17 | A validar |
| RF11 | Tratar falhas no cálculo e processamento automático | CT14, CT15 | Comportamento técnico pendente |
| RF12 | Preservar o estado após nova consulta/reinicialização | CT16 | A validar |
| RF13 | Registrar histórico de bloqueios e desbloqueios, se requerido | CT20 | Pendente de confirmação do produto |
| RF14 | Não causar regressão em operações de usuários regulares | CT19 | A validar |

## Como interpretar a matriz

- **Regra principal descrita na história:** consta explicitamente no contexto da funcionalidade.
- **A validar:** cenário planejado, ainda sem evidência de execução.
- **Pendente de confirmação do produto:** a história não define o comportamento com precisão suficiente.

## Limitações

A matriz representa rastreabilidade planejada, não comprova cobertura executada. Para transformar os cenários em testes aprovados, é necessário confirmar os critérios de aceite, executar no ambiente disponível e registrar evidências.
