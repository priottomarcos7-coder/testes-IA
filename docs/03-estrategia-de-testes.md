# 3. Estratégia de Testes

## Testes funcionais

Validar diretamente as regras de negócio:

- aplicação do bloqueio;
- impedimento de novas reservas;
- impedimento de renovações;
- exibição do status;
- exibição do motivo;
- desbloqueio automático;
- desbloqueio manual.

São essenciais para confirmar se a funcionalidade atende à história de usuário.

## Testes de API

Validar os endpoints relacionados a:

- usuários;
- empréstimos;
- reservas;
- bloqueios;
- desbloqueios;
- permissões.

Devem ser verificadas respostas HTTP, payloads, mensagens, persistência e autorização.

## Testes de interface

Validar:

- perfil do usuário;
- painel administrativo;
- lista de bloqueados;
- motivo;
- quantidade de dias em atraso;
- mensagens;
- ações administrativas.

## Testes exploratórios

Explorar combinações não previstas, como:

- múltiplos livros;
- devoluções em sequência;
- datas próximas ao limite;
- atualização de dados;
- repetição de operações;
- sessões simultâneas;
- diferentes perfis de acesso.

## Testes de integração

Verificar a comunicação entre:

`Empréstimos -> cálculo de atraso -> bloqueio -> reservas/renovações -> interface administrativa`

O objetivo é encontrar inconsistências entre os componentes.

## Testes de regressão

Executar testes das funcionalidades relacionadas a:

- cadastro de usuários;
- empréstimos;
- devoluções;
- reservas;
- renovações;
- administração.

A nova regra não deve impedir operações de usuários que estão em situação regular.

## Testes de segurança e autorização

Confirmar que:

- somente administradores autorizados podem remover bloqueios;
- usuários comuns não conseguem alterar o próprio status;
- endpoints administrativos estão protegidos;
- tentativas não autorizadas retornam erro adequado.

## Ordem sugerida

1. Validar requisitos e ambiguidades.
2. Preparar massa de dados.
3. Testar API/backend.
4. Testar integração.
5. Testar interface.
6. Executar testes exploratórios.
7. Executar regressão.
8. Registrar evidências e defeitos.
