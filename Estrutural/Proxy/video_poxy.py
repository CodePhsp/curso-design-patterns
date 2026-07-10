from interface_proxy import InterfaceProxy


class VideoProxy(InterfaceProxy):
    
    def __init__(self, service: InterfaceProxy):
        self._service = service
        self._cache = {}
        
    def download_video(self, url) -> dict:
        if url in self._cache:
            print('Do cache:', url)
        
            return self._cache[url]
        
        print(f'Proxy: {url} não foi encotrada no cache.')
        video = self._service.download_video(url)
        self._cache[url] = video
        
        return video