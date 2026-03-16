import os
import logging
from urllib.parse import urlparse
from fastapi import FastAPI, Security, HTTPException, Depends
from fastapi.security.api_key import APIKeyHeader
from fastapi.responses import FileResponse
from starlette.status import HTTP_403_FORBIDDEN

API_KEY = os.getenv("HUB_API_KEY", "super_secret_key_50")
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

from Phase_5_Capstone.Day_46_QR_Code_Generator import code_generator
from Phase_4_Engineering.Day_31_Weather_Fetcher import get_weather
from Phase_4_Engineering.Day_32_Currency_Converter import get_all_rates, currency_converter
from Phase_3_OOP.Day_30_HTTP_Request import http_request as get_joke

app = FastAPI(
    title="🚀 Coding Hardcore Portfolio API",
    version="1.1.0",
    description="Final Capstone Hub for 50 Days Challenge"
)

logger = logging.getLogger("hub_logger")

async def validate_key(header_key: str = Security(api_key_header)):
    if header_key == API_KEY:
        return header_key
    logger.warning(f"Unauthorized access attempt with key: {header_key}")
    raise HTTPException(
        status_code=HTTP_403_FORBIDDEN, 
        detail="Access Denied: Invalid API Key"
    )

@app.get("/weather/{city}", dependencies=[Depends(validate_key)], tags=["Services"])
async def api_weather(city: str):
    logger.info(f"Fetching weather for: {city}")
    result = await get_weather(city)
    return {"result": result}

@app.get("/joke", dependencies=[Depends(validate_key)], tags=["Fun"])
async def api_joke():
    joke = get_joke("https://v2.jokeapi.dev/joke/Programming?type=single")
    return {"joke": joke}

@app.get("/system/status", dependencies=[Depends(validate_key)], tags=["Monitoring"])
async def api_sys_status():
    import psutil
    return {
        "cpu": f"{psutil.cpu_percent()}%",
        "ram": f"{psutil.virtual_memory().percent}%",
        "disk": f"{psutil.disk_usage('/').percent}%"
    }

@app.get("/generate_qr/", dependencies=[Depends(validate_key)], tags=["Services"])
async def api_generate_qr(url: str):
    save_path = "Phase_5_Capstone/other/Day_46"
    os.makedirs(save_path, exist_ok=True)
    
    code_generator(url, save_path)
    domain = urlparse(url).netloc.replace('www.', '').replace('.', '_')
    file_path = f"{save_path}/{domain}.png"
    
    if os.path.exists(file_path):
        return FileResponse(file_path)
    raise HTTPException(status_code=500, detail="QR Generation failed")

@app.get("/currency/{code_a}/{code_b}", dependencies=[Depends(validate_key)], tags=["Services"])
async def api_currency(code_a: int, code_b: int):
    data = await get_all_rates()
    if data is None:
        raise HTTPException(status_code=429, detail="Monobank API limit reached.")
        
    result = currency_converter(data, code_a, code_b)
    return {"exchange_rate": result}