from realSubject import weatherService


class WeatherServiceProxy(weatherService):
    def __init__(self, real_service: weatherService):
        self._real_service = real_service
        self._cache = {}

    def get_temperature(self, city: str) -> float:
        if city in self._cache:
            print('Retornando do cache')
            return self._cache[city]
        
        print('Proxy: Chamda não encontrada no cache')
        temperature = self._real_service.get_temperature(city)
        self._cache[city] = temperature
        return temperature