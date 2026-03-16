import logging
import os
from contextlib import asynccontextmanager
from Phase_5_Capstone.Day_48_Portfolio_API import app

LOG_DIR = os.getenv("LOG_PATH", "/app/Phase_5_Capstone/other/Day_49")
LOG_FILE = os.path.join(LOG_DIR, "system_logs.log")

def setup_logging():
    os.makedirs(LOG_DIR, exist_ok=True)
    hub_logger = logging.getLogger("hub_logger")
    hub_logger.setLevel(logging.INFO)

    formatter = logging.Formatter("🐳 [%(levelname)s] %(asctime)s - %(message)s")

    file_h = logging.FileHandler(LOG_FILE, encoding='utf-8')
    file_h.setFormatter(formatter)
    hub_logger.addHandler(file_h)

    console_h = logging.StreamHandler()
    console_h.setFormatter(formatter)
    hub_logger.addHandler(console_h)
    
    return hub_logger

logger = setup_logging()

@asynccontextmanager
async def lifespan(app_instance):
    logger.info("--- THE BEAST AWAKENS ---")
    logger.info(f"Log path: {LOG_FILE}")
    yield
    logger.info("--- THE BEAST FALLS ASLEEP ---")

app.router.lifespan_context = lifespan

@app.get("/docker/status", tags=["Monitoring"])
async def docker_status():
    logger.info("Docker health status checked.")
    return {
        "status": "online",
        "container_mode": True,
        "logging_active": os.path.exists(LOG_FILE)
    }