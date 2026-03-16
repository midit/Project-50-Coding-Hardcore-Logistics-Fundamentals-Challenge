import os
import time
import logging
import httpx
import asyncio
from typing import Optional, List, Dict

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('Phase_4_Engineering/other/Day_32/currency.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

CURRENCY_CODES = {
    "USD": 840,
    "EUR": 978,
    "PLN": 985,
    "UAH": 980
}

_cache = {"data": None, "timestamp": 0}
CACHE_TTL = 60 

async def get_all_rates() -> Optional[List[Dict]]:
    """Отримує курси валют з кешуванням."""
    current_time = time.time()
    
    if _cache["data"] and (current_time - _cache["timestamp"] < CACHE_TTL):
        logging.info("Отримання курсів з кешу.")
        return _cache["data"]

    url = "https://api.monobank.ua/bank/currency"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=10.0)
            
            if response.status_code == 200:
                logging.info("[+] Дані отримані від Monobank.")
                _cache["data"] = response.json()
                _cache["timestamp"] = current_time
                return _cache["data"]
            
            elif response.status_code == 429:
                logging.warning("[!] Rate limit: забагато запитів.")
                return _cache["data"] 
            
            return None
    except Exception as e:
        logging.error(f"Помилка мережі: {e}")
        return None

def currency_converter(data: List[Dict], code_a: int, code_b: int = 980) -> str:
    """Знаходить курс для пари валют."""
    if not data:
        return "Дані недоступні (спробуйте пізніше)"

    for c in data:
        if c['currencyCodeA'] == code_a and c['currencyCodeB'] == code_b:
            buy = c.get('rateBuy')
            sell = c.get('rateSell')
            cross = c.get('rateCross')

            result = f"Купівля: {buy}, Продаж: {sell}" if buy else f"Крос-курс: {cross}"
            logging.info(f"Пара {code_a}/{code_b}: {result}")
            return result
    
    return "Валютну пару не знайдено"

async def main():
    rates = await get_all_rates()
    
    usd_rate = currency_converter(rates, CURRENCY_CODES["USD"], CURRENCY_CODES["UAH"])
    eur_rate = currency_converter(rates, CURRENCY_CODES["EUR"], CURRENCY_CODES["UAH"])
    
    print(f"USD/UAH: {usd_rate}")
    print(f"EUR/UAH: {eur_rate}")

if __name__ == "__main__":
    asyncio.run(main())