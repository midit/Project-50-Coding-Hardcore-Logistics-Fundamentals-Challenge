import os
import time
import psutil
import logging

logging.basicConfig(
    filename='Phase_5_Capstone/other/Day_45/sys_alerts.log', 
    level=logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

WARNING_STATUS = False

def system_monitor(cpu=True, virtual_memory=True, disk=True, ram_threshold=47.3):
    global WARNING_STATUS

    cpu_data = f"CPU: {psutil.cpu_percent(interval=0.1)}%" if cpu else "0%"
    ram_p = psutil.virtual_memory().percent if virtual_memory else "0%"

    if ram_p > ram_threshold:
        virtual_memory_data = f"[WARNING] VRAM: {ram_p}%"
        if not WARNING_STATUS:
            logging.warning(f"High RAM usage: {ram_p}%")
            WARNING_STATUS = True
    else:
        virtual_memory_data = f"VRAM: {ram_p} %"
        WARNING_STATUS = False
    
    disk_data = f"DISK: {psutil.disk_usage('/').percent}%" if disk else 0

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{cpu_data:<5}, {virtual_memory_data:<5}, {disk_data:<5}")

if __name__ == "__main__":
    while True:
        system_monitor()
        time.sleep(1)