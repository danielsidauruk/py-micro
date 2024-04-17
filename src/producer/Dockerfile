FROM python:3.11

WORKDIR /app

COPY producer.py .

RUN pip install redis

CMD ["python", "producer.py"]