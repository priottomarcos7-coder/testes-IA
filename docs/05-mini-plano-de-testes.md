# 5. Mini Plano de Testes

## Objetivo

Validar que usuários com livros em atraso superior a 7 dias sejam bloqueados automaticamente e que o bloqueio impeça novas reservas e renovações, seja corretamente apresentado e seja removido conforme as regras definidas.

## Escopo

### Incluído

- Cálculo do atraso.
- Bloqueio automático.
- Persistência do bloqueio.
- Novas reservas.
- Renovações.
- Perfil do usuário.
- Painel administrativo.
- Lista de bloqueados.
- Motivo.
- Dias de atraso.
- Desbloqueio automático.
- Desbloqueio manual.
- Permissões.
- Tratamento de erros.
- Integração entre API e interface.
- Regressão.

### Fora do escopo inicial

Funcionalidades não relacionadas ao fluxo de empréstimos, reservas, usuários e administração, salvo quando afetadas pela nova regra.

## Cenários principais

1. 6 dias de atraso: não bloquear.
2. 7 dias: validar regra de limite.
3. 8 dias: bloquear.
4. Usuário bloqueado: impedir reserva.
5. Usuário bloqueado: impedir renovação.
6. Exibir status, motivo e dias.
7. Devolução: desbloquear quando não houver outro atraso elegível.
8. Dois livros atrasados: manter bloqueio enquanto necessário.
9. Administrador autorizado: permitir desbloqueio manual.
10. Usuário sem permissão: negar alteração.

## Estratégia de validação

A validação deve começar pela API/backend, pois é onde as regras de negócio e persistência podem ser verificadas de forma direta. Depois devem ser realizados testes de integração e interface.

Testes exploratórios devem procurar comportamentos não previstos. Por fim, a regressão deve garantir que usuários regulares continuem podendo reservar e renovar normalmente.

## Critérios de entrada

- Requisitos disponíveis.
- Regra do limite de 7 dias esclarecida.
- Ambiente de testes funcional.
- Massa de dados preparada.
- Endpoints e permissões disponíveis.

## Critérios de saída

- Cenários críticos aprovados.
- Regras de bloqueio e desbloqueio validadas.
- API e interface consistentes.
- Regressão executada.
- Nenhum defeito crítico/alto sem tratamento ou aceite formal.

## Evidências

Para cada teste devem ser armazenados, quando aplicável:

- dados utilizados;
- requisição;
- resposta da API;
- prints da interface;
- logs;
- resultado esperado;
- resultado obtido;
- evidência de aprovação ou defeito.
