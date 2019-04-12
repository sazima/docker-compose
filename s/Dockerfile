FROM python:3.6-alpine
RUN apk add gcc make openssl-dev &\
pip install shadowsocks
RUN sed -i 's/cleanup/reset/g' /usr/local/lib/python3.6/site-packages/shadowsocks/crypto/openssl.py
COPY config.json /ss/config.json
CMD ["ssserver", "-c", "/ss/config.json", "start"]
