import os
import aiohttp
import asyncio
from typing import Optional
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv("Phase_4_Engineering/other/Day_31/.env")
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

class WeatherData(BaseModel):
    temp: float = Field(alias="main", list_alias="temp")
    description: str = Field(alias="weather")

    @classmethod
    def parse_response(cls, data: dict):
        return {
            "temp": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }

async def get_weather(city_name: str, session: Optional[aiohttp.ClientSession] = None) -> str:
    """Отримує дані про погоду асинхронно."""
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'ua'
    }

    own_session = session is None
    if own_session:
        session = aiohttp.ClientSession()

    try:
        async with session.get(BASE_URL, params=params) as response:
            if response.status == 200:
                data = await response.json()
                parsed = WeatherData.parse_response(data)
                return f"🌍 {city_name}: {parsed['temp']}°C, {parsed['description']}."
            
            elif response.status == 401:
                return "⚠️ Помилка авторизації: Перевірте API Key."
            else:
                return f"⚠️ Місто '{city_name}' не знайдено або помилка сервера."
                
    except aiohttp.ClientError as e:
        return f"📡 Помилка мережі: {str(e)}"
    finally:
        if own_session:
            await session.close()

async def main():
    cities = ["Київ", "Cologne", "Bydgoszcz"]
    async with aiohttp.ClientSession() as session:
        tasks = [get_weather(city, session) for city in cities]
        results = await asyncio.gather(*tasks)
        for res in results:
            print(res)

if __name__ == "__main__":
    asyncio.run(main())