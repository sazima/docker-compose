FROM node:alpine
RUN apk add git &&\
    git clone --depth=1 https://github.com/YMFE/yapi.git /vendors && \
    apk del git
WORKDIR /vendors
COPY docker-entrypoint.sh .
RUN npm install --production --registry https://registry.npm.taobao.org
EXPOSE 30000
ENTRYPOINT ["node", "server/app.js"]

