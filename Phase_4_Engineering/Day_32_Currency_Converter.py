import os
import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='Phase_4_Engineering/other/Day_32/currency.log',
    encoding='utf-8'
)

def get_all_rates():
    url = "https://api.monobank.ua/bank/currency"
    response = requests.get(url)

    if response.status_code == 200:
        logging.info("[+] Дані успішно отримані від Monobank!")
        return response.json()
    else:
        logging.error(f"[!] Помилка API: {response.status_code} - {response.text}")
        return None

def currancy_converter(data, codeA, codeB):
    if not data: return
    for c in data:
        if c['currencyCodeA'] == codeA and c['currencyCodeB'] == codeB:
            buy = c.get('rateBuy')
            sell = c.get('rateSell')
            cross = c.get('rateCross')

            if buy and sell:
                msg = f"Купівля: {buy}, Продаж: {sell}"
            else:
                msg = f"Крос-курс: {cross}"
            
            logging.info(f"[$$] Валюта {codeA}/{codeB}: {msg}")
            # print(f"[+] {codeA}/{codeB} записано в лог")
            return msg
    
    return "Валютну пару не знайдено"

if __name__ == "__main__":
    # хі-хі-хі
    # for i in range(1,11):
    all_data = get_all_rates()

    currancy_converter(all_data, 840, 980)
    currancy_converter(all_data, 985, 980)