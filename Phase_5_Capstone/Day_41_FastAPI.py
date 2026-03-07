import sqlite3
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Book Store API")
DB_PATH = 'Phase_4_Engineering/other/Day_34/sql.db'

class Book(BaseModel):
    id: int
    title: str
    price: float
    stock: str

def get_db():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

@app.get("/books", response_model=List[Book])
async def read_books(db: sqlite3.Connection = Depends(get_db)):
    cursor = db.execute("SELECT id, title, price, stock FROM BOOKS")
    books = cursor.fetchall()
    return [dict(book) for book in books]

@app.get("/books/{book_id}", response_model=Book)
async def read_book(book_id: int, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.execute("SELECT id, title, price, stock FROM BOOKS WHERE id = ?", (book_id,))
    book = cursor.fetchone()
    if book is None:
        raise HTTPException(status_code=404, detail="Книгу не знайдено")
    return dict(book)