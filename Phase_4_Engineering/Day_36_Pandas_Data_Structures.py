import pandas as pd
import sqlite3

def pandas_readsql(file_path):
    try:
        sqliteConnection = sqlite3.connect(file_path)

        dataset = pd.read_sql("SELECT * FROM BOOKS", sqliteConnection)
        df = pd.DataFrame(dataset)

        df = df.rename(columns={'title': 'Book_Title', 'price': 'Price_GBP'})

        df['Price_GBP'] = pd.to_numeric(df['Price_GBP'])

        print("[+] df.info()")
        df.info()

        print("[+] df.describe()")
        print(df.describe())

        print("[+] df.memory_usage(deep=True)")
        df.memory_usage(deep=True)

        sqliteConnection.close()
        return df
    except Exception as e:
        print("[!] Помилка:", e)
        return None

if __name__ == "__main__":
    db_path = 'Phase_4_Engineering/other/Day_34/sql.db'
    pandas_readsql(db_path)