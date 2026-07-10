from abc import ABC, abstractmethod


class InterfaceProxy(ABC):
    
    @abstractmethod
    def download_video(self, url) -> dict:
        pass