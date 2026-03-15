import logging
import os
from contextlib import asynccontextmanager
from Phase_5_Capstone.Day_48_Portfolio_API import app

LOG_DIR = "/app/Phase_5_Capstone/other/Day_49"
LOG_FILE = os.path.join(LOG_DIR, "system_logs.log")

logger = logging.getLogger("docker_logger")
logger.setLevel(logging.INFO)

if logger.hasHandlers():
    logger.handlers.clear()

file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
file_handler.setFormatter(logging.Formatter("🐳 [DOCKER LOG] %(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("🐳 [DOCKER LOG] %(message)s"))
logger.addHandler(console_handler)

@asynccontextmanager
async def lifespan(app):
    logger.info("The Beast is containerized! API is starting inside Docker...")
    logger.info(f"Log file initialized at: {LOG_FILE}")
    yield
    logger.info("Shutting down Docker container...")

app.router.lifespan_context = lifespan

@app.get("/docker/status")
async def docker_status():
    logger.info("Status check requested via API")
    return {
        "status": "running",
        "log_file": LOG_FILE,
        "logs_present": os.path.exists(LOG_FILE)
    }