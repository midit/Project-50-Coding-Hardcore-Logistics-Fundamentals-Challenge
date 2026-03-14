import sys
import os
from urllib.parse import urlparse
from fastapi import FastAPI, Security, HTTPException, Depends
from fastapi.security.api_key import APIKeyHeader
from fastapi.responses import FileResponse
from starlette.status import HTTP_403_FORBIDDEN

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Phase_5_Capstone.Day_46_QR_Code_Generator import code_generator
from Phase_4_Engineering.Day_31_Weather_Fetcher import get_weather
from Phase_4_Engineering.Day_32_Currency_Converter import get_all_rates, currancy_converter
from Phase_3_OOP.Day_30_HTTP_Request import http_request as get_joke

app = FastAPI(title="💻 Coding Hardcore Portfolio API")

API_KEY = "super_secret_key_50"
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

async def validate_key(header_key: str = Security(api_key_header)):
    if header_key == API_KEY:
        return header_key
    raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Access Denied: Invalid API Key")

@app.get("/weather/{city}", dependencies=[Depends(validate_key)])
async def api_weather(city: str):
    result = await get_weather(city)
    return {"result": result}

@app.get("/joke", dependencies=[Depends(validate_key)])
async def api_joke():
    joke = get_joke("https://v2.jokeapi.dev/joke/Programming?type=single")
    return {"joke": joke}

@app.get("/system/status", dependencies=[Depends(validate_key)])
async def api_sys_status():
    import psutil
    return {
        "cpu": f"{psutil.cpu_percent()}%",
        "ram": f"{psutil.virtual_memory().percent}%",
        "disk": f"{psutil.disk_usage('/').percent}%"
    }

@app.get("/generate_qr/", dependencies=[Depends(validate_key)])
async def api_generate_qr(url: str):
    save_path = "Phase_5_Capstone/other/Day_46"
    code_generator(url, save_path)
    
    domain = urlparse(url).netloc.replace('www.', '').replace('.', '_')
    file_path = f"{save_path}/{domain}.png"
    
    return FileResponse(file_path)

@app.get("/currency/{code_a}/{code_b}", dependencies=[Depends(validate_key)])
async def api_currency(code_a: int, code_b: int):
    data = get_all_rates()
    if data is None:
        raise HTTPException(status_code=429, detail="Monobank API limit reached. Try again in 1 minute.")
        
    result = currancy_converter(data, code_a, code_b)
    return {"exchange_rate": result}