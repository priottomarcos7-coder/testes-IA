# 4. Identificação de Riscos

| ID | Risco | Impacto | Mitigação |
|---|---|---|---|
| R01 | Cálculo incorreto do atraso | Alto | Testar 6, 7 e 8 dias, datas e horários |
| R02 | Bloqueio aplicado antes/depois do momento esperado | Alto | Testar a transição exata do limite |
| R03 | Desbloqueio automático não executado | Alto | Testar devolução e processamento posterior |
| R04 | Desbloqueio indevido com outro livro atrasado | Alto | Testar múltiplos empréstimos |
| R05 | API e interface com status diferentes | Médio/Alto | Comparar resposta da API com telas |
| R06 | Usuário sem permissão remove bloqueio | Alto | Testar perfis e autorização |
| R07 | Painel administrativo com dados incorretos | Médio | Validar lista, motivo e dias |
| R08 | Regressão em reservas/renovações | Alto | Executar suíte de regressão |
| R09 | Falha no processamento automático | Alto | Testar indisponibilidade, retry e recuperação |

## Principais riscos

### R01 – Erro no cálculo do atraso

É um dos riscos mais importantes porque pode provocar bloqueios indevidos ou permitir reservas para usuários que deveriam estar bloqueados.

### R02 – Erro no limite de 7 dias

A expressão "mais de 7 dias" gera uma ambiguidade importante. O comportamento no 7º dia deve ser confirmado com produto.

### R03 – Desbloqueio automático

Após a devolução, o usuário não deve permanecer bloqueado indevidamente.

### R04 – Múltiplos livros

A devolução de um livro não deve desbloquear o usuário caso outro empréstimo continue atendendo à regra de bloqueio.

### R05 – Inconsistência entre camadas

A API pode considerar o usuário bloqueado enquanto a interface mostra o contrário. Essa situação pode gerar problemas funcionais e de experiência.

### R06 – Permissões

A remoção manual do bloqueio precisa ser protegida para impedir alterações por usuários não autorizados.
