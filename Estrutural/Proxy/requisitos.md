# Desafio: Sistema de Download de Vídeos da Web

## Cenário
Você está desenvolvendo um módulo para uma aplicação que faz o download de arquivos de vídeo pesados da internet (como se fosse um cliente do YouTube ou Vimeo).

### Requisitos
1) A Classe Real (VideoDownloader): Ela tem um método chamado download_video(url). Toda vez que esse método é chamado, ele simula uma conexão de rede demorada (você pode usar time.sleep(2)) e baixa o vídeo da internet.
2) O Problema: Baixar o mesmo vídeo várias vezes seguidas consome muita banda e deixa o sistema lento.
3) Sua Missão com o Proxy: Criar uma classe intermediária (VideoDownloaderProxy) que tenha a mesma interface (o mesmo método download_video).
   a) Quando o usuário pedir um vídeo, o Proxy deve verificar se o vídeo já foi baixado antes (usando um cache na memória, como um dicionário Python).
   b) Se já foi baixado, o Proxy retorna o vídeo instantaneamente do cache.
   c) Se não foi baixado, o Proxy repassa a tarefa para a classe real (VideoDownloader), armazena o resultado no cache e depois entrega ao usuário.
