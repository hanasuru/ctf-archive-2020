FROM php:7.2-apache
RUN mkdir /app
COPY ./app/index.php /app/index.php
COPY ./app/flag.php /app/flag.php
WORKDIR /app
CMD php -S 0.0.0.0:80
