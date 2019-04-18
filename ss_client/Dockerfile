FROM python:3.6-alpine
RUN apk add gcc make openssl-dev & pip install shadowsocks
RUN sed -i 's/cleanup/reset/g' /usr/local/lib/python3.6/site-packages/shadowsocks/crypto/openssl.py
COPY config.json /app/config.json
COPY client.py /app/client.py
WORKDIR /app/
CMD python -i client.py
