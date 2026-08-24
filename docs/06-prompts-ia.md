# 6. Prompts Utilizados com IA

A Inteligência Artificial foi utilizada como ferramenta de apoio e não como fonte única de decisão.

## Prompt 1 – Análise de requisitos

> Analise esta história de usuário de um sistema de biblioteca como um QA e identifique ambiguidades, perguntas para o time de produto e regras de negócio que precisam ser detalhadas.

## Prompt 2 – Cenários

> Gere cenários de teste para uma funcionalidade que bloqueia automaticamente usuários com livros em atraso por mais de 7 dias. Inclua cenários positivos, negativos, de limite, erro e múltiplos empréstimos.

## Prompt 3 – Estratégia

> Crie uma estratégia de testes para essa funcionalidade considerando testes funcionais, API, interface, exploratórios, integração e regressão. Explique a importância de cada abordagem.

## Prompt 4 – Riscos

> Identifique os principais riscos de qualidade de uma funcionalidade de bloqueio automático por atraso de livros e sugira formas de mitigá-los.

## Prompt 5 – Revisão crítica

> Revise os cenários de teste gerados anteriormente como um QA experiente. Identifique lacunas, especialmente nos limites de 7 dias, múltiplos livros, desbloqueio automático, permissões administrativas e inconsistências entre API e interface.

## Prompt 6 – Plano final

> Transforme a análise, os cenários, a estratégia e os riscos em um mini plano de testes claro para apresentação a um líder técnico.

## Refinamento dos prompts

O processo foi iterativo. Primeiro foram levantadas ambiguidades e cenários gerais. Depois foram solicitados refinamentos para cobrir:

- limites;
- cenários negativos;
- erros;
- múltiplos livros;
- permissões;
- desbloqueio automático;
- integração API/interface;
- regressão.

As respostas foram revisadas e adaptadas antes de serem incorporadas ao plano.

## Uso crítico da IA

A IA ajudou a ampliar a cobertura de ideias, mas algumas respostas não devem ser tratadas como requisitos. Por exemplo, o comportamento exato no 7º dia precisa ser confirmado com o produto, pois a expressão "mais de 7 dias" pode ter interpretação diferente da regra implementada.

Também foi considerado que sugestões de testes devem ser confrontadas com o sistema real, seus endpoints, regras e critérios de aceite.
