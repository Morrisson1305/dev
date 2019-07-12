import pyowm

city = input('Enter a city: ')
# country = input('Enter a country: ')
# city2 = input('Enter another city: ')
# country2 = input('Enter another country: ')
print()

apiKey = '3901eae877f62d68f8d37ca8a1de03df'
owm = pyowm.OWM(apiKey)
observation = owm.weather_at_place(city)
w = observation.get_weather()


# observation2 = owm.weather_at_place(city2, country2)
# w = observation.get_weather()

print('weather report'.upper())
print()
print('speed of the wind'.upper(), w.get_wind())
print('the humidity'.upper(), w.get_humidity())
print('the pressure'.upper(), w.get_pressure())
print('temperature'.upper(), w.get_temperature())

