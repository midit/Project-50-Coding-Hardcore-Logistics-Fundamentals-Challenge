import os
import json
import requests
from bs4 import BeautifulSoup

def fetch_content(url):
    try:
        r = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (platform; rv:gecko-version) Gecko/gecko-trail Firefox/firefox-version'})
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("[!] Щось пішло не так")

def save_content(file_path, data):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print("[+] Дані успішно збережені!")
    except:
        print("[!] Щось пішло не так")

def scrape_data(url, file_path):
    soup = BeautifulSoup(fetch_content(url), 'html.parser')

    books = []

    for pod in soup.find_all('article', class_='product_pod'):
        if pod:
            title = pod.h3.a['title'].strip()
            price_tag = pod.find('p', class_='price_color').text.strip()
            stock_availability = pod.find('p', class_='instock availability').text.strip()

            book_data = {
                'title': title if title else "N/A",
                'price': price_tag if price_tag else "N/A",
                'stock': stock_availability if stock_availability else "N/A"
            }
            books.append(book_data)
        
    for i, b in enumerate(books):
        print(f"{i+1}. {b['title']} - {b['price']} [{b['stock']}]")

    save_content(file_path, books)

if __name__ == "__main__":
    url = "https://books.toscrape.com/"
    file_path = 'Phase_4_Engineering/other/Day_33/books.json'

    scrape_data(url, file_path)