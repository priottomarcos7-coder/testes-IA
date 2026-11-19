# Aplicação demonstrativa e testes automatizados

## Escopo

O repositório agora inclui uma aplicação demonstrativa própria para validar a regra de bloqueio por empréstimos em atraso. Ela não é o sistema oficial da EBAC: é um ambiente controlado de estudo criado para tornar os cenários reproduzíveis.

## Regra adotada

A história descreve bloqueio para atraso **maior que 7 dias**. Portanto, a implementação considera 8 dias ou mais como elegível e exatamente 7 dias como não elegível. Essa decisão operacionaliza a frase da história; em um produto real, a regra deve ser confirmada com Produto.

## Tecnologias

- Node.js e Express para API REST;
- arquivo JSON local para persistência demonstrativa;
- Cypress para automação de API;
- HTML/JavaScript para telas demonstrativas de perfil e painel;
- GitHub Actions para execução contínua.

## Executar localmente

```bash
npm install
npm start
```

Em outro terminal:

```bash
npm test
```

A API fica em `http://localhost:3000`. O painel estático está em `/admin.html` e o perfil em `/profile.html?id=2`. O servidor também possui rotas alternativas `/api/ui/admin` e `/api/ui/profile/:id`.

## Massa de dados

O endpoint `POST /api/test/reset` restaura dados conhecidos para execução repetível. Endpoints sob `/api/test` existem exclusivamente para simulação em ambiente local de estudo e não devem ser expostos em produção.

## Cenários

A suíte contém 20 testes de API em `cypress/e2e/api.cy.js` e 4 testes de interface em `cypress/e2e/interface.cy.js`, totalizando 24 execuções. CT07, CT08, CT09 e CT18 são exercitados em mais de uma camada. CT02 implementa a interpretação literal de “mais de 7 dias”: exatamente 7 dias não bloqueia; em produto real, confirmar o critério com Produto. CT19 valida reserva e renovação para usuário regular.

## Limitações conhecidas

- Persistência em JSON é adequada apenas para demonstração local, não para concorrência ou produção.
- A autenticação administrativa é simulada por cabeçalho `x-role`; não equivale a autenticação segura.
- A falha da rotina é simulada por endpoint de teste.
- A interface é intencionalmente simples e serve para validar apresentação dos estados.
- CT16 valida leituras sucessivas no mesmo processo, não a recuperação após reinicialização do servidor.
- A interface estática é acessível diretamente; a verificação de `x-role` protege endpoints administrativos, mas é apenas simulação e não autenticação real.
- O desbloqueio manual pode remover o bloqueio mesmo com empréstimo elegível; a prioridade entre ação manual e regra automática precisa de definição de Produto.

## Evidências

Os resultados reais devem ser obtidos executando `npm test` localmente ou consultando o workflow do GitHub Actions após o push. Não considerar testes aprovados apenas porque estão escritos.
