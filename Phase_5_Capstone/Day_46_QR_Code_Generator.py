import os
import qrcode
import requests
from io import BytesIO
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw
from urllib.parse import urljoin, urlparse


def fetch_logo(url, headers):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        print(f"[!] Помилка під час отримання відповіді від {url}: {e}")
        return None

    for rel in ['apple-touch-icon', 'icon']:
        link = soup.find("link", rel=lambda x: x and rel in x.lower())
        if link and link.get('href'):
            icon_url = urljoin(url, link.get('href'))
            break
    else:
        icon_url = urljoin(url, "/favicon.ico")

    try:
        logo_res = requests.get(icon_url, headers=headers, timeout=5)
        logo_res.raise_for_status()
        return Image.open(BytesIO(logo_res.content)).convert("RGBA")
    except Exception as e:
        print(f"[!] Помилка під час знаходження лого: {e}")
        return None


def fit_logo_to_square(logo: Image.Image, size: int, padding_ratio: float = 0.15) -> Image.Image:
    padding = int(size * padding_ratio)
    inner = size - padding * 2

    logo_ratio = logo.width / logo.height
    if logo_ratio >= 1:
        new_w = inner
        new_h = int(inner / logo_ratio)
    else:
        new_h = inner
        new_w = int(inner * logo_ratio)

    logo_resized = logo.resize((new_w, new_h), Image.Resampling.LANCZOS)

    container = Image.new("RGBA", (size, size), (255, 255, 255, 255))

    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    radius = size // 8
    draw.rounded_rectangle([0, 0, size - 1, size - 1], radius=radius, fill=255)
    container.putalpha(mask)

    x = (size - new_w) // 2
    y = (size - new_h) // 2
    container.paste(logo_resized, (x, y), mask=logo_resized)

    return container


def code_generator(url, save_path):
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/91.0.4472.124 Safari/537.36'
        )
    }

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGBA')
    qr_w, qr_h = qr_img.size

    logo = fetch_logo(url, headers)

    if logo:
        logo_size = qr_w // 5
        logo_container = fit_logo_to_square(logo, logo_size)
        pos = ((qr_w - logo_size) // 2, (qr_h - logo_size) // 2)
        qr_img.paste(logo_container, pos, mask=logo_container)
    else:
        print(f"[!] Лого для {url} не знайдено. Генерація QR-Коду без лого.")

    os.makedirs(save_path, exist_ok=True)

    domain = urlparse(url).netloc
    clean_name = domain.replace('www.', '').replace('.', '_')
    full_path = os.path.join(save_path, f"{clean_name}.png")

    qr_img.convert('RGB').save(full_path)
    print(f"[+] QR-Код збережно до: {full_path}")


if __name__ == "__main__":
    path = "Phase_5_Capstone/other/Day_46"
    sites = [
        "https://sternenkofund.org",
        "https://monobank.ua",
        "https://cargofy.com"
    ]
    for site in sites:
        code_generator(site, path)