FROM  webhippie/php-caddy:latest-arm32v6

MAINTAINER wktadmin <w@wktadmin.com>

EXPOSE 8080

WORKDIR /srv/www

ENV DB_HOST='$_ENV("DB_HOST")'\
    DB_USER='$_ENV("DB_USER")'\
    DB_PASSWD='$_ENV("DB_PASSWD")'\
    DB_NAME='$_ENV("DB_NAME")' \
    CONIFG_PATH='/srv/www/config.php' \
    CSRF='$_ENV("CSRF")'

RUN rm index.html && git clone https://github.com/MoeNetwork/Tieba-Cloud-Sign.git /srv/www
RUN    rm -r /var/cache/apk
RUN    rm -r /usr/share/man
RUN echo "* * * * * /usr/bin/php7 /srv/www/do.php" >> /etc/crontabs/root
ENTRYPOINT sed -i ''"$(cat ${CONIFG_PATH} -n | grep "DB_HOST" | awk '{print $1}')"'c '"$(echo "define('DB_HOST','${DB_HOST}');")"'' ${CONIFG_PATH} && \
              sed -i ''"$(cat ${CONIFG_PATH} -n | grep "DB_USER" | awk '{print $1}')"'c '"$(echo "define('DB_USER','${DB_USER}');")"'' ${CONIFG_PATH} && \
               sed -i ''"$(cat ${CONIFG_PATH} -n | grep "DB_PASSWD" | awk '{print $1}')"'c '"$(echo "define('DB_PASSWD','${DB_PASSWD}');")"'' ${CONIFG_PATH} && \
              sed -i ''"$(cat ${CONIFG_PATH} -n | grep "DB_NAME" | awk '{print $1}')"'c '"$(echo "define('DB_NAME','${DB_NAME}');")"'' ${CONIFG_PATH} && \
              sed -i ''"$(cat ${CONIFG_PATH} -n | grep "ANTI_CSRF" | awk '{print $1}')"'c '"$(echo "define('ANTI_CSRF',"${CSRF}");")"'' ${CONIFG_PATH} && \
              cat ${CONIFG_PATH} && \
              crond && \
              /bin/s6-svscan /etc/s6
