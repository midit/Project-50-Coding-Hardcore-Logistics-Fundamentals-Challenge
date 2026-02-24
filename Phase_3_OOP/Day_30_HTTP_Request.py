import requests

def http_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json() 
        return "ЖАРТ: "+data.get('joke', "[!] Поле joke не знайдено")
    else:
        return "[!] Щось пішло не так."
        

if __name__ == "__main__":
    print(http_request("https://v2.jokeapi.dev/joke/Programming?type=single"))