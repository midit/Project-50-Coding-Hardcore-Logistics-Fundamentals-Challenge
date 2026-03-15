FROM python:3.13-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*

COPY Phase_5_Capstone/other/Day_49/requirements.txt .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "Phase_5_Capstone.Day_49_Docker:app", "--host", "0.0.0.0", "--port", "8000"]