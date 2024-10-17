FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y build-essential \
    && pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

COPY .env .env

ENV PYTHONUNBUFFERED 1

CMD ["python", "src/main.py"]
