# 2. Cenários de Teste

Os cenários abaixo foram definidos a partir da história de usuário e das dúvidas levantadas na análise. Os comportamentos que dependem de decisão do time de produto estão identificados como **Pendente de regra** e não devem ser considerados critérios fechados até a confirmação.

## Convenções

- **Prioridade alta:** impacto direto no bloqueio, desbloqueio ou autorização.
- **Prioridade média:** apresentação de informações e consistência entre componentes.
- **Prioridade baixa:** comportamento complementar, sem impacto imediato no fluxo principal.
- Os dados de teste são exemplos e devem ser adaptados ao ambiente disponível.
- A regra descrita na história é “mais de 7 dias”; portanto, 8 dias é o primeiro exemplo inequívoco de bloqueio. O comportamento no 7º dia precisa ser confirmado.

## Cenários

| ID | Prioridade | Tipo | Pré-condição / dados | Ação | Resultado esperado |
|---|---|---|---|---|---|
| CT01 | Alta | Positivo | Usuário ativo com um empréstimo em atraso há 8 dias | Executar processamento da regra | Usuário passa para bloqueado e o motivo do bloqueio fica registrado |
| CT02 | Alta | Limite | Usuário ativo com atraso de exatamente 7 dias | Executar processamento | No protótipo, permanece desbloqueado pela interpretação literal de “mais de 7 dias”; em produto real, confirmar o critério com Produto |
| CT03 | Alta | Negativo | Usuário ativo com atraso de 6 dias | Executar processamento | Usuário permanece desbloqueado |
| CT04 | Alta | Positivo | Usuário ativo sem empréstimos atrasados | Executar processamento | Usuário permanece desbloqueado |
| CT05 | Alta | Negativo | Usuário já bloqueado | Tentar criar nova reserva | Operação é recusada e mensagem explica a restrição |
| CT06 | Alta | Negativo | Usuário já bloqueado | Tentar renovar empréstimo | Operação é recusada conforme regra de negócio |
| CT07 | Média | Interface | Usuário bloqueado por atraso | Consultar perfil | Status e motivo do bloqueio são exibidos corretamente |
| CT08 | Média | Interface | Existe usuário bloqueado | Consultar painel administrativo | Administrador visualiza o status atualizado |
| CT09 | Média | Interface | Existem usuários bloqueados | Consultar lista administrativa | Lista apresenta os usuários e os campos definidos pelo produto |
| CT10 | Alta | Positivo | Usuário bloqueado; nenhum outro empréstimo mantém a condição de bloqueio | Registrar devolução do livro em atraso e processar atualização | Bloqueio é removido conforme a regra de desbloqueio confirmada |
| CT11 | Alta | Regra de negócio | Usuário possui dois empréstimos que atendem à regra de bloqueio | Devolver apenas um dos livros | Usuário permanece bloqueado enquanto o outro empréstimo mantiver a condição |
| CT12 | Alta | Permissão | Administrador com permissão de desbloqueio | Remover bloqueio manualmente | Ação é concluída e fica registrada conforme regra de auditoria |
| CT13 | Alta | Segurança | Usuário sem permissão administrativa | Tentar remover bloqueio | Operação é negada e o status original é mantido |
| CT14 | Alta | Erro | Dados de empréstimo inválidos ou indisponíveis | Executar cálculo do atraso | Sistema não aplica bloqueio incorreto e registra/trata a falha |
| CT15 | Alta | Resiliência | Rotina automática indisponível ou com falha simulada | Executar processamento | Falha é registrada e existe tratamento/reprocessamento conforme decisão técnica |
| CT16 | Média | Persistência | Usuário foi bloqueado corretamente | Consultar novamente o usuário na mesma execução | A API retorna o mesmo estado; a suíte atual não valida recuperação após reinicialização do servidor |
| CT17 | Alta | Integração | Usuário bloqueado com acesso à API e interface | Consultar status nos dois canais | API e interface apresentam o mesmo estado |
| CT18 | Média | Interface | Usuário bloqueado tenta realizar operação restrita | Consultar mensagem apresentada | Mensagem informa claramente o motivo e a ação impedida |
| CT19 | Alta | Regressão | Usuário regular, sem atraso elegível | Realizar reserva e renovação permitidas | Funcionalidades continuam operando normalmente |
| CT20 | Média | Auditoria | Bloqueio/desbloqueio realizado | Consultar histórico, se previsto | Histórico registra ator, data, ação e motivo conforme requisito |

## Cenários detalhados em Gherkin

### CT01 – Bloqueio após mais de 7 dias

```gherkin
Cenário: Bloquear usuário com livro atrasado há mais de 7 dias
  Dado que o usuário possui um livro com 8 dias de atraso
  E o usuário está ativo e desbloqueado
  Quando a rotina de bloqueio for processada
  Então o usuário deve ficar bloqueado
  E o motivo deve indicar o atraso do livro
```

### CT02 – Validar o limite de 7 dias

```gherkin
Cenário: Avaliar usuário com exatamente 7 dias de atraso
  Dado que o usuário possui um livro com exatamente 7 dias de atraso
  Quando a rotina de bloqueio for processada
  Então o resultado deve respeitar a regra confirmada pelo time de produto
```

### CT05 – Usuário bloqueado tentando reservar

```gherkin
Cenário: Impedir nova reserva para usuário bloqueado
  Dado que o usuário está bloqueado por atraso
  Quando tentar realizar uma nova reserva
  Então a operação deve ser recusada
  E uma mensagem deve informar o motivo da restrição
```

### CT10 – Desbloqueio após devolução

```gherkin
Cenário: Remover bloqueio após regularização
  Dado que o usuário está bloqueado por atraso
  E não possui outro empréstimo que mantenha a condição de bloqueio
  Quando devolver o livro em atraso
  E o sistema atualizar a situação do usuário
  Então o bloqueio deve ser removido conforme a regra definida
```

### CT11 – Outro livro continua atrasado

```gherkin
Cenário: Manter bloqueio enquanto existir outro empréstimo elegível
  Dado que o usuário possui dois livros que atendem à regra de bloqueio
  Quando devolver apenas um dos livros
  Então o usuário deve continuar bloqueado
```

### CT13 – Usuário sem permissão

```gherkin
Cenário: Impedir remoção de bloqueio sem autorização
  Dado que o usuário não possui permissão administrativa
  E existe um bloqueio ativo
  Quando tentar remover o bloqueio
  Então a operação deve ser recusada
  E o bloqueio deve permanecer ativo
```

## Observações para execução

1. Confirmar com produto o limite exato de dias, o fuso horário e o momento do processamento automático.
2. Confirmar se a regra considera dias corridos ou outra forma de contagem.
3. Confirmar como reservas existentes e renovações são tratadas.
4. Confirmar o comportamento do desbloqueio automático e manual.
5. Preparar massa de dados com usuários regulares, bloqueados e com múltiplos empréstimos.
6. Registrar resultado obtido e evidências durante a execução.

Este documento descreve 20 cenários funcionais planejados. O protótipo automatiza CT01–CT20 na API e repete CT07, CT08, CT09 e CT18 na interface, totalizando 24 execuções. Isso valida somente o protótipo, não o sistema oficial de referência.
