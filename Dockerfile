# Fase de resolución de dependencias
FROM python:slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Fase de ejecución
FROM python:slim

WORKDIR /app

COPY --from=builder /app /app

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
