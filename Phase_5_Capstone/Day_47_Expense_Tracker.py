import os
import uvicorn
from pydantic import BaseModel, Field
from fastapi import FastAPI
from fastapi.responses import FileResponse
import matplotlib.pyplot as plt
import pandas as pd
import logging

logging.basicConfig(
    filename='Phase_5_Capstone/other/Day_47/expense_log.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

app = FastAPI(title="💸 Expense Tracker")
DATA_FILE = "Phase_5_Capstone/other/Day_47/expense.csv"

if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=['date', 'category', 'amount', 'description'])
    df.to_csv(DATA_FILE, index=False)

class ExpenseSchema(BaseModel):
    date: str = Field(..., example="2026-03-13")
    category: str = Field(..., example="Food")
    amount: float = Field(..., gt=0)
    description: str

@app.post("/add_expense/")
async def add_expense(expense: ExpenseSchema):
    try:
        data = [[expense.date, expense.category, expense.amount, expense.description]]
        df = pd.DataFrame(data)
        df.to_csv(DATA_FILE, mode="a", header=False, index=False)
        
        logging.info(f"[+] Додано: {expense.category} - {expense.amount}")
        return {"status": "success", "data": expense}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/get_summary/")
async def get_summary():
    try:
        df = pd.read_csv(DATA_FILE)
        stats = df.groupby('category')['amount'].agg(['sum', 'mean', 'count'])
        total_sum = stats['sum'].sum()
        stats['percentage'] = (stats['sum'] / total_sum * 100).round(2)
        
        return {
            "total_expenses": total_sum,
            "detailed_stats": stats.to_dict(orient="index")
        }
    except Exception as e:
        return {"status": "error", "message": "Файл порожній або відсутній"}

@app.get("/get_chart/")
async def get_chart():
    try:
        df = pd.read_csv(DATA_FILE)
        summary = df.groupby('category')['amount'].sum()

        plt.figure(figsize=(10, 6))
        summary.plot(kind='pie', autopct='%1.1f%%', startangle=140, colormap='viridis')
        plt.title("Розподіл витрат за категоріями")
        plt.ylabel("")


        chart_path = "Phase_5_Capstone/other/Day_47/chart.png"
        plt.savefig(chart_path)
        plt.close()

        return FileResponse(path=chart_path, media_type="image/png")
    
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/export/")
async def export_data():
    try:
        return FileResponse(path=DATA_FILE, filename="my_expenses.csv", media_type="text/csv")
    
    except Exception as e:
        print(f"[!] Щось пішло не так: {e}")
