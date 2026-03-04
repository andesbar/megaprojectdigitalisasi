FROM php:8.2-apache

# Install driver Postgres & Aktifkan modul SSL, vhost_alias, dan rewrite
RUN apt-get update && apt-get install -y libpq-dev \
    && docker-php-ext-install pdo pdo_pgsql pgsql \
    && a2enmod vhost_alias ssl rewrite
