FROM python:3.12-alpine

RUN adduser -D -u 1000 chal

WORKDIR /home/chal

COPY chall1.py .
RUN chmod 755 chall1.py && chown chal:chal chall1.py

USER chal

EXPOSE 9999

CMD ["socat", "-T", "60", "TCP-LISTEN:9999,reuseaddr,fork", "EXEC:python3 chall1.py,stderr"]
