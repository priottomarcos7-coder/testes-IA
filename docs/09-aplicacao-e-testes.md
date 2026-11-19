# Aplicação demonstrativa e execução dos 20 cenários

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

A API fica em `http://localhost:3000`. A interface administrativa está em `/api/ui/admin` e o perfil em `/api/ui/profile/2`.

## Massa de dados

O endpoint `POST /api/test/reset` restaura dados conhecidos para execução repetível. Endpoints sob `/api/test` existem exclusivamente para simulação em ambiente local de estudo e não devem ser expostos em produção.

## Cenários

A suíte `cypress/e2e/api.cy.js` contém um teste automatizado para cada ID CT01–CT20. CT02 interpreta o requisito “mais de 7 dias” como limite exclusivo. CT19 valida reserva e renovação permitidas para um usuário regular com empréstimo ativo na massa de dados.

## Limitações conhecidas

- Persistência em JSON é adequada apenas para demonstração local, não para concorrência ou produção.
- A autenticação administrativa é simulada por cabeçalho `x-role`; não equivale a autenticação segura.
- A falha da rotina é simulada por endpoint de teste.
- A interface é intencionalmente simples e serve para validar apresentação dos estados.
- CT19 deverá ser ampliado quando a aplicação demonstrativa incluir fluxo completo de criação de empréstimo.

## Evidências

Os resultados reais devem ser obtidos executando `npm test` localmente ou consultando o workflow do GitHub Actions após o push. Não considerar testes aprovados apenas porque estão escritos.
