import pandas as pd
import numpy as np
import sqlite3

def data_cleaning(file_path):
    try:
        sqliteConnection = sqlite3.connect(file_path)

        dataset = pd.read_sql("SELECT * FROM BOOKS", sqliteConnection)
        df = pd.DataFrame(dataset)

        df.loc[0, 'price'] = np.nan
        df = pd.concat([df, df.iloc[[5]]], ignore_index=True)

        print(f"[i] Рядків до очищення: {len(df)}")

        df = df.drop_duplicates()
        print(f"[+] Після drop_duplicates(): {len(df)}")

        print(f"[i] Кількість порожніх цін до: {df['price'].isnull().sum()}")
        
        df['price'] = df['price'].fillna(df['price'].mean())
        
        print(f"[+] Кількість порожніх цін після fillna: {df['price'].isnull().sum()}")

        sqliteConnection.close()
        return df
    except Exception as e:
        print("[!] Помилка:", e)
        return None

if __name__ == "__main__":
    db_path = 'Phase_4_Engineering/other/Day_34/sql.db'
    data_cleaning(db_path)