from abc import ABC, abstractmethod


class weatherService(ABC):

    @abstractmethod
    def get_temperature(self, city: str) -> float: ...