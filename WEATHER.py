from pyowm import OWM
i=input()

owm = OWM('390de9c60eca7c44db96dd4abd9d691b')
mgr = owm.weather_manager()
observation = mgr.weather_at_place(i)
w = observation.weather
print(w)