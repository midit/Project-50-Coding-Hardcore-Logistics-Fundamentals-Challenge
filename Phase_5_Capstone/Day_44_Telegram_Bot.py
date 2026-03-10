import os, sys
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Phase_4_Engineering.Day_31_Weather_Fetcher import get_weather

load_dotenv("Phase_5_Capstone/other/Day_44/.env")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

class WeatherState(StatesGroup):
    waiting_for_city = State()

@dp.message(Command("start"))
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer("🌤️ Привіт! Напиши назву міста, щоб дізнатися погоду")
    await state.set_state(WeatherState.waiting_for_city)

@dp.message(Command("stop"))
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer("🌤️ Щоб почати - напиши /start")
    await state.clear()

@dp.message(WeatherState.waiting_for_city)
async def process_city(message: types.Message, state: FSMContext):
    city = message.text

    report = await get_weather(city)
    await message.answer(report)
    await message.answer("🌤️ Впиши інше місто або /stop для виходу:")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())