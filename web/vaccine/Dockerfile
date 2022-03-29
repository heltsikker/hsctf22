FROM ubuntu:18.04

RUN apt update && \
    DEBIAN_FRONTEND=noninteractive apt install -y \
        apache2 \
        libapache2-mod-php \
        php \
        php-sqlite3


COPY src/ /var/www/html
RUN rm /var/www/html/index.html

COPY vaccine.sqlite /vaccine.sqlite
RUN chmod 444 /vaccine.sqlite

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh


EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]
