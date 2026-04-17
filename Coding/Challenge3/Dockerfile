FROM php:8.2-alpine
RUN apk add --no-cache python3 socat
RUN adduser -D -u 1000 chal
WORKDIR /home/chal
COPY coding_challenge3.py flag.txt ./
RUN chmod 755 coding_challenge3.py && \
    chmod 444 flag.txt && \
    chown chal:chal coding_challenge3.py flag.txt
USER chal
EXPOSE 80
CMD ["socat", "-T", "60", "TCP-LISTEN:80,reuseaddr,fork", "EXEC:python3 coding_challenge3.py,stderr"]
