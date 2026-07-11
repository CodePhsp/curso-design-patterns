# Strategy - Processamento de Arquivos

## Desafio

### Cenário

Você está desenvolvendo um módulo responsável pelo processamento de arquivos em uma aplicação.

O sistema precisa suportar diferentes formas de processamento, como imagens (`.png` e `.jpg`) e documentos PDF (`.pdf`). Cada tipo de arquivo possui um algoritmo específico, mas a forma como o processamento é realizado pode variar ao longo do tempo.

### Problema

Centralizar todos os algoritmos de processamento em uma única classe torna o código difícil de manter e impede a reutilização dos algoritmos em outros contextos.

### Objetivo

Criar uma classe responsável pelo processamento (`FileService`) que delegue a responsabilidade do processamento para uma estratégia (`FileStrategy`), permitindo alterar o algoritmo de execução sem modificar a classe principal.

### Requisitos

A abstração `FileStrategy`:

- Deve definir um método chamado `process_file(file)`.

A estratégia de imagens `ImageStrategy`:

- Deve implementar o processamento de arquivos de imagem (`.png` e `.jpg`).

A estratégia de documentos `PdfStrategy`:

- Deve implementar o processamento de arquivos PDF (`.pdf`).

A classe de contexto `FileService`:

- Deve receber uma implementação de `FileStrategy` por meio do construtor.
- Deve delegar o processamento do arquivo para a estratégia recebida.

### Regras de funcionamento

- O `FileService` deve conhecer apenas a abstração `FileStrategy`.
- As estratégias devem ser intercambiáveis.
- A troca de estratégia não deve exigir alterações na implementação do `FileService`.

### Restrições

- Utilize o padrão **Strategy**.
- Não implemente lógica de seleção de estratégia dentro do `FileService`.
- Todas as estratégias devem compartilhar a mesma interface.
- O código deve favorecer baixo acoplamento e alta coesão.
