FROM python:3.11-slim
RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/*
WORKDIR /challenge
COPY idk.py .
COPY blackbox.bin .
...
