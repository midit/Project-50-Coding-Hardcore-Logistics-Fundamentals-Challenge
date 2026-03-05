import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

def visualize_data(df):
    df['price'] = pd.to_numeric(df['price'])
    df['Price_Category'] = df['price'].apply(lambda x: 'Budget' if x < 35 else 'Premium')
    
    plt.style.use('ggplot')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.hist(df['price'], bins=10, color='skyblue', edgecolor='black')
    ax1.set_title('Розподіл цін книг')
    ax1.set_xlabel('Ціна (£)')
    ax1.set_ylabel('Кількість')

    category_stats = df.groupby('Price_Category')['price'].mean()
    category_stats.plot(kind='bar', ax=ax2, color=['#2ecc71', '#e67e22'])
    ax2.set_title('Середня ціна за категоріями')
    ax2.set_ylabel('Середня ціна (£)')
    
    plt.tight_layout()
    plt.savefig('Phase_4_Engineering/other/Day_39/day_39_report.png')
    print("[+] Графік збережено як day_39_report.png")

def to_df(file_path):
    try:
        conn = sqlite3.connect(file_path)
        df = pd.read_sql("SELECT * FROM BOOKS", conn)
        conn.close()
        return df
    except Exception as e:
        print("[!] Помилка:", e)
        return None

if __name__ == "__main__":
    db_path = 'Phase_4_Engineering/other/Day_34/sql.db'
    df = to_df(db_path)

    if df is not None:
        visualize_data(df)