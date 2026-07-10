# Proxy virtual - Sistema de Download de Vídeos

## Desafio

### Cenário

Você está desenvolvendo um módulo para uma aplicação que faz o download de arquivos de vídeo pesados da internet (como se fosse um cliente do YouTube ou Vimeo).

### Problema

Baixar o mesmo vídeo várias vezes seguidas consome muita banda e deixa o sistema lento.

### Objetivo

Criar uma classe intermediária (VideoDownloaderProxy) que tenha a mesma interface (o mesmo método download_video).

### Requisitos

A Classe Real (VideoDownloader):

- Deve possuir um método chamado `download_video(url)`.

- Simular uma conexão de rede demorada utilizando `time.sleep(2)`.

- Retornar o conteúdo do vídeo após o download.

### Regras de fucionamento

- Quando o usuário pedir um vídeo, o Proxy deve verificar se o vídeo já foi baixado antes.

- Se já foi baixado, o Proxy retorna o vídeo instantaneamente do cache.

- Se não foi baixado, o Proxy repassa a tarefa para a classe real (VideoDownloader), armazena o resultado no cache e depois entrega ao usuário.

### Restrições

- O cliente não deve acessar diretamente a classe `VideoDownloader`.

- O Proxy deve manter a mesma interface da classe real.

- O cache deve permanecer apenas em memória.
