FROM python:alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
    && addgroup -S app && adduser -S app -G app \
    && chown -R app:app .

COPY . .

USER app

CMD ["python", "main.py"]