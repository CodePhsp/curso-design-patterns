# Proxy virtual

Controla o acesso ao objeto original, permitindo a execução de algo antes ou depois do pedido chegar ao objeto original.

## Aplicação

- Controle de acesso
- Logs
- Cache
- Lazy instantiation
- Lazy evaluation

## Relação com SOLID

DIP - Dependency inversion principal

OCP - Open/Close Principal

## Variações do Proxy

**proxy virtual:** controla acesso a recursos que podem ser caros para criação ou utilização.

**proxy remoto:** controla acesso a recursos que estão em servidores remotos.

**proxy de proteção:** controla acesso a recursos que possam necessitar autenticação ou permissão.

**proxy inteligente (smart proxy):** controla acesso ao objeto real, executa, também, tarefas adicionais para saber quando e como executar determinadas ações.
