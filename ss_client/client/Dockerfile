FROM python:3.6-alpine
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories &&\
 apk update && \
 apk add linux-headers gcc make openssl-dev  libc-dev  &&\
 pip install shadowsocks gevent -i https://pypi.tuna.tsinghua.edu.cn/simple &&\
 sed -i 's/cleanup/reset/g' /usr/local/lib/python3.6/site-packages/shadowsocks/crypto/openssl.py
COPY client.py /app/client.py
WORKDIR /app/
CMD python  client.py
