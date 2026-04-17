FROM php:8.2-apache

RUN apt-get update && apt-get install -y iputils-ping --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -u 1000 chal

COPY index.php /var/www/html/index.php
COPY flag.txt /flag.txt

RUN chmod 444 /flag.txt

EXPOSE 80

CMD ["apache2-foreground"]
