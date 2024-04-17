FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV REDIS_HOST redis

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir Flask redis

EXPOSE 5001

CMD ["python", "app.py"]
