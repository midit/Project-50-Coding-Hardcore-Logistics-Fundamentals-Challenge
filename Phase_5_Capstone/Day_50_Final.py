import os
import subprocess
import time
import webbrowser
import sys

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    header = """
    ==================================================
    🚀 PROJECT 50: FINAL RELEASE - THE BEAST HUB
    ==================================================
    Status: 50/50 [████████████████████] 100%
    ==================================================
    """
    print(header)

def run_command(command, description):
    print(f"🔄 {description}...")
    try:
        subprocess.run(command, shell=True, check=True, capture_output=True)
        print(f"✅ {description} завершено успішно.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Помилка під час {description}: {e}")
        return False

def launch_beast():
    clear_console()
    print_header()

    docker_dir = "Phase_5_Capstone/other/Day_49"
    
    if not os.path.exists(docker_dir):
        print(f"⚠️ Помилка: Директорія {docker_dir} не знайдена!")
        return

    os.chdir(docker_dir)

    print("🐋 Підготовка Docker-контейнера...")
    
    run_command("docker-compose down", "Зупинка старих контейнерів")
    
    print("🏗️ Збирання образу та запуск (це може зайняти час)...")
    try:
        subprocess.run("docker-compose up -d --build", shell=True, check=True)
        print("🚀 Контейнер успішно запущений у фоновому режимі!")
    except subprocess.CalledProcessError:
        print("❌ Не вдалося запустити Docker. Переконайся, що Docker Desktop запущено.")
        return

    print("⏳ Очікування ініціалізації API (10 секунд)...")
    for i in range(10, 0, -1):
        sys.stdout.write(f"\rВідкриття через {i} сек...")
        sys.stdout.flush()
        time.sleep(1)
    
    print("\n\n🌐 Відкриваємо інструменти перевірки:")
    
    urls = [
        "http://localhost:8000/docs",
        "http://localhost:8000/docker/status"
    ]

    for url in urls:
        print(f"🔗 Відкриття: {url}")
        webbrowser.open(url)
        
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Завершення сесії... Зупинка контейнера...")
        subprocess.run("docker-compose down", shell=True)
        print("🏁 Project 50 офіційно завершено!")

if __name__ == "__main__":
    launch_beast()