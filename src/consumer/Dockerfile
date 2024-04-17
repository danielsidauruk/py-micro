FROM python:3.11

WORKDIR /app

COPY consumer.py .

RUN pip install redis

CMD ["python", "consumer.py"]
