import json
import sqlite3
import os

class DatabaseManager:
    def __init__(self, database_path):
        self.database_path = database_path

    def __enter__(self):
        try:
            self.sqliteConnection = sqlite3.connect(self.database_path)
            return self.sqliteConnection.cursor()
        except sqlite3.Error as error:
            print("[!] Помилка підключення:", error)
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is None:
                self.sqliteConnection.commit()
            else:
                self.sqliteConnection.rollback()
            self.sqliteConnection.close()
        except sqlite3.Error as error:
            print("[!] Помилка закриття:", error)

def initialize_db(json_path, database_path):
    with DatabaseManager(database_path) as cursor:
        cursor.execute("DROP TABLE IF EXISTS BOOKS")
        cursor.execute("DROP TABLE IF EXISTS AUTHORS")

        cursor.execute("""
            CREATE TABLE AUTHORS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE
            )
        """)
        
        cursor.execute("""
            CREATE TABLE BOOKS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,=
        """)

        cursor.execute("INSERT OR IGNORE INTO AUTHORS (name) VALUES (?)", ("Unknown Artist",))
        cursor.execute("SELECT id FROM AUTHORS WHERE name = ?", ("Unknown Artist",))
        author_id = cursor.fetchone()[0]

        try:
            with open(json_path, "r", encoding='utf-8') as f:
                data = json.load(f)
            
            for b in data:
                title = b['title']
                price = float(b['price'].replace("£", ""))
                stock = b['stock']
                
                cursor.execute(
                    "INSERT INTO BOOKS (title, price, stock, author_id) VALUES (?, ?, ?, ?)",
                    (title, price, stock, author_id)
                )
            print(f"[+] БД ініціалізована. Завантажено {len(data)} книг.")
        except FileNotFoundError:
            print("[!] Файл JSON не знайдено.")

def search_books(database_path, search_term):
    with DatabaseManager(database_path) as cursor:
        query = "SELECT title, price FROM BOOKS WHERE title LIKE ?"
        cursor.execute(query, (f"%{search_term}%",))
        results = cursor.fetchall()
        
        print(f"\nРезультати пошуку для '{search_term}':")
        for row in results:
            print(f"- {row[0]} (£{row[1]})")

def get_library_report(database_path):
    with DatabaseManager(database_path) as cursor:
        query = """
            SELECT BOOKS.title, AUTHORS.name 
            FROM BOOKS 
            JOIN AUTHORS ON BOOKS.author_id = AUTHORS.id
        """
        cursor.execute(query)
        results = cursor.fetchall()
        
        print("\nЗвіт по бібліотеці (JOIN):")
        for row in results:
            print(f"Книга: {row[0]} | Автор: {row[1]}")

if __name__ == "__main__":
    db_path = 'Phase_4_Engineering/other/Day_34/sql.db'
    j_path = 'Phase_4_Engineering/other/Day_33/books.json'
    
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    initialize_db(j_path, db_path)
    search_books(db_path, "Light")
    get_library_report(db_path)