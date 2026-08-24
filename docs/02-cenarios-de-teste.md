# 2. Cenários de Teste

| ID | Tipo | Cenário | Resultado esperado |
|---|---|---|---|
| CT01 | Positivo | Usuário com 8 dias de atraso | Usuário é bloqueado automaticamente |
| CT02 | Limite | Usuário com exatamente 7 dias de atraso | Comportamento segue a regra definida pelo produto |
| CT03 | Limite/Negativo | Usuário com 6 dias de atraso | Usuário não é bloqueado |
| CT04 | Positivo | Usuário sem atraso | Usuário permanece desbloqueado |
| CT05 | Negativo | Usuário bloqueado tenta nova reserva | Reserva é recusada |
| CT06 | Negativo | Usuário bloqueado tenta renovar | Renovação é recusada |
| CT07 | Positivo | Bloqueio no perfil | Perfil apresenta status e motivo |
| CT08 | Positivo | Bloqueio no painel administrativo | Administrador visualiza o bloqueio |
| CT09 | Positivo | Lista de usuários bloqueados | Lista apresenta usuário, motivo e dias de atraso |
| CT10 | Positivo | Devolução do livro atrasado | Bloqueio é removido automaticamente quando não há outro atraso elegível |
| CT11 | Regra/Negativo | Usuário devolve um de dois livros atrasados | Continua bloqueado se outro livro atender à regra |
| CT12 | Positivo | Administrador remove bloqueio manualmente | Bloqueio é removido conforme regra definida |
| CT13 | Negativo | Usuário sem permissão tenta desbloquear | Operação é negada |
| CT14 | Erro | Falha no cálculo dos dias de atraso | Sistema não cria bloqueio incorreto e registra o erro |
| CT15 | Erro | Falha na rotina automática | Sistema trata/reprocessa a falha conforme regra |
| CT16 | Positivo | Reinicialização após bloqueio | Status permanece consistente |
| CT17 | Integração | API x interface | Status da API corresponde ao apresentado na interface |
| CT18 | Positivo | Mensagem de bloqueio | Mensagem informa claramente motivo e restrições |

## Cenários detalhados em Gherkin

### CT01 – Bloqueio após mais de 7 dias

```gherkin
Cenário: Bloquear usuário com livro atrasado há mais de 7 dias
  Dado que o usuário possui um livro com 8 dias de atraso
  Quando o sistema processar a regra de bloqueio
  Então o usuário deve ser bloqueado
  E o motivo deve indicar o atraso do livro
  E a quantidade de dias de atraso deve ser apresentada
```

### CT02 – Limite de 7 dias

```gherkin
Cenário: Validar o limite de 7 dias
  Dado que o usuário possui um livro com exatamente 7 dias de atraso
  Quando o sistema processar a regra de bloqueio
  Então o comportamento deve seguir a regra definida pelo produto
```

### CT05 – Usuário bloqueado tentando reservar

```gherkin
Cenário: Impedir nova reserva para usuário bloqueado
  Dado que o usuário está bloqueado
  Quando ele tentar realizar uma nova reserva
  Então a reserva deve ser recusada
  E uma mensagem adequada deve informar o motivo
```

### CT06 – Usuário bloqueado tentando renovar

```gherkin
Cenário: Impedir renovação para usuário bloqueado
  Dado que o usuário está bloqueado
  Quando ele tentar renovar
  Então a operação deve ser recusada
```

### CT10 – Desbloqueio após devolução

```gherkin
Cenário: Remover bloqueio após devolução
  Dado que o usuário está bloqueado por atraso
  E não possui outro livro que mantenha a condição de bloqueio
  Quando o livro for devolvido
  Então o bloqueio deve ser removido automaticamente
```

### CT11 – Outro livro continua atrasado

```gherkin
Cenário: Manter bloqueio quando outro livro continua atrasado
  Dado que o usuário possui dois livros atrasados
  E ambos atendem à regra de bloqueio
  Quando o usuário devolver apenas um livro
  Então o usuário deve continuar bloqueado
```

### CT13 – Usuário sem permissão

```gherkin
Cenário: Impedir remoção de bloqueio sem autorização
  Dado que o usuário não possui permissão administrativa
  Quando tentar remover um bloqueio
  Então a operação deve ser recusada
```
