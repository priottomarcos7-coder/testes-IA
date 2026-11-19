# 6. Prompts Utilizados com IA

A Inteligência Artificial foi utilizada como ferramenta de apoio à análise e à geração de ideias. As respostas precisam ser verificadas contra a história de usuário, as regras confirmadas e o comportamento real do sistema.

## Prompt 1 – Análise de requisitos

> Analise esta história de usuário de um sistema de biblioteca como um QA e identifique ambiguidades, perguntas para o time de produto e regras de negócio que precisam ser detalhadas. Não invente regras que não estejam descritas.

## Prompt 2 – Geração de cenários

> Gere cenários de teste para uma funcionalidade que bloqueia automaticamente usuários com livros em atraso por mais de 7 dias. Inclua cenários positivos, negativos, de limite, erro e múltiplos empréstimos. Para cada cenário, informe pré-condições, dados, ação e resultado esperado. Destaque o que depende de confirmação do produto.

## Prompt 3 – Estratégia

> Crie uma estratégia de testes para essa funcionalidade considerando testes funcionais, API, interface, exploratórios, integração e regressão. Explique o objetivo de cada abordagem e quais riscos ela ajuda a reduzir.

## Prompt 4 – Análise de riscos

> Identifique os principais riscos de qualidade de uma funcionalidade de bloqueio automático por atraso de livros. Classifique impacto e sugira formas de mitigação. Não assuma detalhes técnicos que não foram fornecidos.

## Prompt 5 – Revisão crítica

> Revise os cenários de teste como um QA. Procure lacunas nos limites de 7 dias, múltiplos livros, desbloqueio automático, permissões administrativas, persistência e inconsistências entre API e interface. Aponte também cenários redundantes e resultados esperados vagos.

## Prompt 6 – Plano de testes

> Com base na história, cenários, estratégia e riscos fornecidos, monte um mini plano de testes com objetivo, escopo, critérios de entrada e saída, dados necessários, evidências e limitações. Separe requisitos confirmados de pontos pendentes.

## Exemplo documentado de refinamento

O exemplo abaixo ilustra como um pedido genérico pode ser refinado para obter cenários mais úteis. É um exemplo de aplicação do método, não uma transcrição literal de conversa com uma ferramenta específica.

### Pedido inicial

> Gere testes para a regra que bloqueia usuários com livros atrasados há mais de 7 dias.

### Limitação identificada na primeira abordagem

Um pedido tão amplo pode produzir apenas o caminho principal e deixar de fora situações importantes, como o limite exato, múltiplos empréstimos e a regularização do usuário.

### Prompt refinado

> Atue como QA e amplie a cobertura dessa regra. Inclua usuários com 6, 7 e 8 dias de atraso; usuários com mais de um livro; devolução de apenas um dos livros; bloqueio e desbloqueio; tentativa de reserva e renovação por usuário bloqueado; falhas no processamento automático; e permissões administrativas. Para cada caso, informe pré-condições, dados de teste, ação e resultado esperado. Quando a história não definir o comportamento, marque como “Pendente de confirmação do produto” em vez de criar uma regra.

### Revisão humana aplicada

- Mantido o cenário de 8 dias como exemplo de bloqueio inequívoco segundo a expressão “mais de 7 dias”.
- Mantido o cenário de 6 dias como controle negativo.
- Marcado o cenário de exatamente 7 dias como pendente de confirmação.
- Incluídos casos de múltiplos empréstimos para evitar desbloqueio indevido.
- Incluída validação de autorização para ações administrativas.
- Resultados vagos foram substituídos por condições observáveis sempre que os requisitos permitem.

## Refinamento dos prompts

O processo foi organizado em ciclos:

1. Solicitar análise inicial da história.
2. Identificar lacunas e ambiguidades.
3. Pedir cenários com dados, pré-condições e resultados.
4. Solicitar revisão crítica para localizar lacunas.
5. Comparar as sugestões com os requisitos disponíveis.
6. Atualizar a documentação somente após avaliação.

## Uso crítico da IA

A IA ajuda a ampliar possibilidades e acelerar a organização das ideias, mas não define a regra de negócio. O comportamento exato no 7º dia, por exemplo, precisa ser confirmado com produto, pois a expressão “mais de 7 dias” não deve ser alterada por suposição.

As sugestões também precisam ser confrontadas com o sistema real, seus endpoints, permissões, critérios de aceite e limitações técnicas. Nenhum cenário deste documento deve ser apresentado como executado sem evidência de execução.
