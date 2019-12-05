FROM webhippie/php-caddy

MAINTAINER xxx <szlszl35622@gmail.com>

EXPOSE 8080

WORKDIR /srv/www

ENV DB_HOST='127.0.0.1'\
    DB_USER='root'\
    DB_PASSWD=''\
    DB_NAME='tiebacloud' \
    CONIFG_PATH='/srv/www/config.php' \
    CSRF='true'


RUN rm -rf /srv/www/* && \
    git clone --depth=1 https://github.com/magicblack/maccms10.git  /srv/www && \
    rm -r /var/cache/apk && \
    rm -r /usr/share/man && \
    ls

# RUN echo "* * * * * /usr/bin/php7 /srv/www/do.php" >> /etc/crontabs/root

ENTRYPOINT  crond && \
              /bin/s6-svscan /etc/s6
