from video_downlader import VideoDownloader
from video_poxy import VideoProxy


downloader = VideoDownloader()
proxy = VideoProxy(downloader)

print(proxy.download_video('www.youtube.com'))

print(proxy.download_video('www.youtube.com'))