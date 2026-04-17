FROM php:8.2-alpine
RUN apk add --no-cache socat iputils && adduser -D -u 1000 chal
WORKDIR /home/chal
COPY server.py flag.txt ./
RUN chmod 444 flag.txt && chown chal:chal server.py flag.txt
USER chal
EXPOSE 9999
CMD ["socat", "-T", "60", "TCP-LISTEN:9999,reuseaddr,fork", "EXEC:python3 server.py,stderr"]
