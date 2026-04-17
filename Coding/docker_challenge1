FROM python:3.11-slim

RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/*

WORKDIR /challenge

COPY challenge1-easy.py .

RUN useradd -m ctf && chown -R ctf:ctf /challenge
USER ctf

EXPOSE 1337

CMD ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:'python3 -u challenge1-easy.py'"]
