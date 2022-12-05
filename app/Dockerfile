FROM python:alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
    && chown -R 1000:0 .

COPY . .

USER 1000

CMD ["python", "main.py"]