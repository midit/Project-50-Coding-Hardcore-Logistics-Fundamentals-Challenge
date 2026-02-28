import json
import sqlite3

class DatabaseManager:
    def __init__(self, database_path):
        self.database_path = database_path

    def __enter__(self):
        try:
            self.sqliteConnection = sqlite3.connect(database_path)
            print("[+] DB Init")
    
        except sqlite3.Error as error:
            print("[!] Щось пішло не так -", error)
        
        return self.sqliteConnection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.sqliteConnection.commit()
            print("[+] DB Saved")
            self.sqliteConnection.close()
            print("[+] DB Connection Closed")
    
        except sqlite3.Error as error:
            print("[!] Щось пішло не так -", error)

def create_table(json_path, database_path):

    with DatabaseManager(database_path) as cursor:
        table_creation_query = """
            CREATE TABLE IF NOT EXISTS BOOKS (
                id INTEGER PRIMARY KEY, 
                title TEXT,
                price REAL,
                stock TEXT
            );
        """
        cursor.execute(table_creation_query)

        try:
            with open(json_path, "r") as f:
                data = json.load(f)
            for b in data:
                sql_query = 'INSERT INTO BOOKS (title, price, stock) VALUES (?, ?, ?)'

                book_title = b['title']
                book_price = float(b['price'].replace("£", ""))
                book_stock = b['stock']

                cursor.execute(sql_query, (book_title, book_price, book_stock))
            
        except FileNotFoundError:
            return []


if __name__ == "__main__":
    database_path = 'Phase_4_Engineering/other/Day_34/sql.db'
    json_path = 'Phase_4_Engineering/other/Day_33/books.json'
    
    create_table(json_path, database_path)