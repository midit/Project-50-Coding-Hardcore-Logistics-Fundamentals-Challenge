import requests

url = "http://127.0.0.1:8000/add_expense/"

expenses = [
    {"date": "2026-03-01", "category": "Food", "amount": 120.5, "description": "Сільпо (продукти)"},
    {"date": "2026-03-02", "category": "Food", "amount": 450.0, "description": "Вечеря з Expirenza"},
    {"date": "2026-03-02", "category": "Transport", "amount": 500.0, "description": "Окко (Pulls 95)"},
    {"date": "2026-03-03", "category": "Rent", "amount": 12000.0, "description": "Оплата житла"},
    {"date": "2026-03-04", "category": "Entertainment", "amount": 300.0, "description": "Планета Кіно (Дюна 3)"},
    {"date": "2026-03-05", "category": "Food", "amount": 85.0, "description": "Кава в Idealist"},
    {"date": "2026-03-06", "category": "Health", "amount": 640.0, "description": "Аптека Доброго Дня"},
    {"date": "2026-03-07", "category": "Transport", "amount": 120.0, "description": "Uklon до вокзалу"},
    {"date": "2026-03-08", "category": "Entertainment", "amount": 1500.0, "description": "Квіти та подарунки"},
    {"date": "2026-03-09", "category": "Health", "amount": 2200.0, "description": "Стоматологія (чистка)"},
    {"date": "2026-03-10", "category": "Food", "amount": 320.0, "description": "Новус (продукти)"},
    {"date": "2026-03-11", "category": "Subscriptions", "amount": 199.0, "description": "YouTube Premium"}
]

for item in expenses:
    response = requests.post(url, json=item)
    print(f"Adding {item['category']}: {response.status_code}")