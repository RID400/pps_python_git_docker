# Fase de resolución de dependencias
FROM python:slim as builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Fase de ejecución
FROM builder as runner

COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]
