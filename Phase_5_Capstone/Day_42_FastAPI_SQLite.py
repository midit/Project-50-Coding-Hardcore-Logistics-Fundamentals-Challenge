from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List

DB_URL = "sqlite:///Phase_4_Engineering/other/Day_34/sql.db"
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class BookDB(Base):
    __tablename__ = "BOOKS"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    price = Column(Float)
    stock = Column(String)

class BookCreate(BaseModel):
    title: str
    price: float
    stock: str = "In stock"

class Book(BookCreate):
    id: int
    class Config:
        from_attributes = True

app = FastAPI(title="Book Store CRUD")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/books", response_model=List[Book])
def read_books(db: Session = Depends(get_db)):
    return db.query(BookDB).all()

@app.post("/books", response_model=Book)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = BookDB(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_update: BookCreate, db: Session = Depends(get_db)):
    db_book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in book_update.model_dump().items():
        setattr(db_book, key, value)
    db.commit()
    return db_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return {"message": "Book deleted successfully"}