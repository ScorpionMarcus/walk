import requests
import json
import pytemperature

city_id = '5393049'
api_key = '36ecd63d8f5f00b01952ed66e5ecc659'
api_url = f'http://api.openweathermap.org/data/2.5/weather?id={city_id}&APPID={api_key}'

data = json.loads(requests.get(api_url).text)
k = data['main']['temp']
temp = pytemperature.k2f(k)

if temp > 85:
    print(f"The temperature is {temp} degrees fahrenheit...too hot to walk.")
elif temp < 50:
    print(f"The temperature is {temp} degrees fahrenheit...too cold to walk.")
else:
    print(f"The temperature is {temp} degrees fahrenheit...we can walk.")