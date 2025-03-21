# Сборка
FROM python:3.9-slim-buster AS builder

WORKDIR /app

COPY requirements.txt .
# Используем кэширование слоев
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы приложения
COPY . .

# Финальный образ
FROM python:3.9-slim-buster

WORKDIR /app

# Копируем зависимости из этапа builder
COPY --from=builder /app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8800"]

# Если uvicorn установлен внутри venv:
# CMD ["/bin/bash", "-c", "source /app/.venv/bin/activate && uvicorn app.main:app --host 0.0.0.0 --port 8800"]