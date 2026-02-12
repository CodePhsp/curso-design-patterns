from realSubject import ExternalWeatherService
from weatherServiceProxy import WeatherServiceProxy


service = ExternalWeatherService()
proxy = WeatherServiceProxy(service)

print(proxy.get_temperature("Manaus"))
print(proxy.get_temperature("Manaus"))