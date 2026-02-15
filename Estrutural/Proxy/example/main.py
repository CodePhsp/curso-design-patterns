from realSubject import ExternalWeatherService
from weatherServiceProxy import WeatherServiceProxy


service = ExternalWeatherService()
proxy = WeatherServiceProxy(service)

print(proxy.get_temperature("Manaus"), end='\n\n\n')
print(proxy.get_temperature("Manaus"))