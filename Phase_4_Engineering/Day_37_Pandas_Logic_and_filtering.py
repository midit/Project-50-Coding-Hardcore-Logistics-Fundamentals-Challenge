import pandas as pd
import sqlite3

def pandas_logic(file_path):
    try:
        sqliteConnection = sqlite3.connect(file_path)

        dataset = pd.read_sql("SELECT * FROM BOOKS", sqliteConnection)
        df = pd.DataFrame(dataset)

        df = df.rename(columns={'title': 'Book_Title', 'price': 'Price_GBP'})

        df['Price_GBP'] = pd.to_numeric(df['Price_GBP'])

        books_search = df[(df['Price_GBP'] > 20) & (df['Price_GBP'] < 50)]
        print("Книги, ціна яких більша за £20 та менша за £50:")
        print(books_search)

        df['Price_Category'] = df['Price_GBP'].apply(lambda x: 'Budget' if x < 35 else 'Premium')
        stats = df.groupby('Price_Category')['Price_GBP'].agg(['count', 'mean', 'sum'])
        print("Групуванні по ціновій категорії (Бюджетні та Преміум):")
        print(stats)

        sqliteConnection.close()
        return df
    except Exception as e:
        print("[!] Помилка:", e)
        return None

if __name__ == "__main__":
    db_path = 'Phase_4_Engineering/other/Day_34/sql.db'
    pandas_logic(db_path)