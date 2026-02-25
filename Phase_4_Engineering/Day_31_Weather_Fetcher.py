import os
import requests
from dotenv import load_dotenv

load_dotenv("Phase_4_Engineering/other/Day_31/.env")
key = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city_name):
    params = {
        'q': city_name,
        'appid': key,
        'units': 'metric',
        'lang': 'ua' 
    }   
    url = "https://api.openweathermap.org/data/2.5/weather"
    response = requests.get(url, params=params)

    data = response.json()
    if response.status_code == 200:
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        desc = data['weather'][0]['description']
        print(f"🌍 {city_name}: {temp}°C, {desc}. Вологість: {humidity}%, Вітер: {wind} м/с")
    else:
        print(f"[!] Помилка для міста {city_name}: {data.get('message')}")

if __name__ == "__main__":
    get_weather("Київ")
    get_weather("Cologne")
    get_weather("Bydgoszcz")