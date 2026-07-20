# Observer - Monitor de Estoque

## Desafio

### Cenário

Você está desenvolvendo um sistema para uma loja virtual.

Alguns produtos permanecem indisponíveis durante determinado período e diversos clientes desejam ser avisados quando o item voltar ao estoque.

### Problema

A classe responsável pelo estoque não deve conhecer como cada cliente será notificado (e-mail, SMS, push notification, etc.).

Adicionar essas responsabilidades diretamente na classe de estoque torna o sistema difícil de manter e expandir.

### Objetivo

Criar uma classe responsável pelo controle de estoque (`Inventory`) que notifique automaticamente todos os interessados quando um produto voltar a ficar disponível.

### Requisitos

O Subject (`Inventory`):

- Deve permitir registrar observadores.
- Deve permitir remover observadores.
- Deve notificar todos os observadores quando houver alteração na quantidade disponível de um produto.

A abstração (`Observer`):

- Deve definir um método chamado `update(product)`.

Os Observers:

- Devem implementar a interface `Observer`.
- Cada observador deve executar uma ação diferente ao receber a notificação.

### Regras de funcionamento

- Apenas quando um produto sair de indisponível para disponível os observadores devem ser notificados.
- Todos os observadores cadastrados devem receber a atualização.
- O estoque não deve conhecer como cada observador utiliza a informação recebida.

### Restrições

- Utilize o padrão **Observer**.
- O Subject deve depender apenas da abstração `Observer`.
- Deve ser possível adicionar novos observadores sem modificar a implementação do estoque.
