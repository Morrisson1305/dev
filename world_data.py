import datetime
import pyowm
from geopy.geocoders import Nominatim

geo_locator = Nominatim(user_agent="Elinam Tech")
location_name = input('Enter the city you want to find: ').upper()
location = geo_locator.geocode(location_name)


print('\nAddress of ', location_name)
print(location.address)
print('\n geographical Situation (latitude && longitude)'.upper(), '\n')
print((location.latitude, location.longitude))
print()
print('detailed information about the location'.upper())
print(location.raw)
print()

# this portion of the code prints the time for the search.

print('Time for the search is:'.upper(), end=": "); print(datetime.datetime.now())
print()
# this portion of the code prompts the user about the weather conditions of the location.


apiKey = '3901eae877f62d68f8d37ca8a1de03df'
owm = pyowm.OWM(apiKey)
observation = owm.weather_at_place(location_name)
w = observation.get_weather()
print()
print( location_name,'weather report'.upper())
print()
print('speed of the wind'.upper(), w.get_wind())
print('the humidity'.upper(), w.get_humidity())
print('the pressure'.upper(), w.get_pressure())
print('temperature'.upper(), w.get_temperature())
