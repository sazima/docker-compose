FROM node:alpine
EXPOSE 3000

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories \
    && apk add --no-cache --virtual .fetch-deps \
        g++ \
        git \
        make \
        python \
    && git clone --depth=1 https://gitee.com/mirrors/YApi.git /vendors \
    && cd /vendors && npm install --production --registry https://registry.npm.taobao.org \
    && apk del .fetch-deps
WORKDIR /vendors
ENTRYPOINT ["node", "server/app.js"]
