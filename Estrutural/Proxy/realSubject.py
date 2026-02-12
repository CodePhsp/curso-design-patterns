import time
import random
from interfaceSubject import weatherService


class ExternalWeatherService(weatherService):
    def get_temperature(self, city: str) -> float:
        print('Chamando API externa...')
        time.sleep(2)

        return round(random.uniform(10,35), 2)
    