import os
import aiohttp
from dotenv import load_dotenv

load_dotenv("Phase_4_Engineering/other/Day_31/.env")
key = os.getenv("OPENWEATHER_API_KEY")

async def get_weather(city_name):
    params = {
        'q': city_name,
        'appid': key,
        'units': 'metric',
        'lang': 'ua' 
    }   
    url = "https://api.openweathermap.org/data/2.5/weather"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            data = await response.json()
            if response.status == 200:
                temp = data['main']['temp']
                desc = data['weather'][0]['description']
                return f"🌍 {city_name}: {temp}°C, {desc}."
            else:
                return f"⚠️ Місто {city_name} не знайдено."
    
    # - - - - Old Implementation - - - -
    # response = requests.get(url, params=params)

    # data = response.json()
    # if response.status_code == 200:
    #     temp = data['main']['temp']
    #     humidity = data['main']['humidity']
    #     wind = data['wind']['speed']
    #     desc = data['weather'][0]['description']
    #     print(f"🌍 {city_name}: {temp}°C, {desc}. Вологість: {humidity}%, Вітер: {wind} м/с")
    # else:
    #     print(f"[!] Помилка для міста {city_name}: {data.get('message')}")

if __name__ == "__main__":
    get_weather("Київ")
    get_weather("Cologne")
    get_weather("Bydgoszcz")