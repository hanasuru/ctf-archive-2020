FROM php:7.3-apache
RUN mkdir /app

COPY ./app/* /app/
WORKDIR /app
COPY php.ini /usr/local/etc/php/php.ini
CMD php -S 0.0.0.0:80
