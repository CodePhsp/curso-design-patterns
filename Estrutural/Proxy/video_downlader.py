from interface_proxy import InterfaceProxy
import time


class VideoDownloader(InterfaceProxy):
    def download_video(self, url: str) -> dict:
        print('Baixando video')
        time.sleep(2)
        
        video = {
            'url': url,
        }
        
        return video