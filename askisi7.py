import pyowm
print "Μάθε τον καιρό της ημέρας για μια τοποθεσία"
print "Δώσε την συντεταγμένη χ της τοποθεσίας"
lat=raw_input()
print "Δώσε την συντεταγμένη y της τοποθεσίας"
lon=raw_input()
# my API-key
owm = pyowm.OWM('0c06eaa709d4acd9e3f246de52dda363')
observation = owm.weather_at_place(lat,lon)
w = observation.get_weather()
temperature = w.get_temperature('celsius')  
wind = w.get_wind()
rain=w.get_rain()
print(w)
print(wind)
print(temperature)
print(rain)
if rain=="raining":
   print "I'm singing in the rain"
if temperature>"20":
    print "nice..."
if temperature<"5":
   print "brrrr"

#import  webbrowser
#webbrowser.open('openweathermap.org')
#webbrowser.open('api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}')
