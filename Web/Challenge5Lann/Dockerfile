FROM php:8.1-apache
RUN docker-php-ext-install mysqli
COPY index.html /var/www/html/index.html
COPY login.php /var/www/html/login.php
EXPOSE 80
