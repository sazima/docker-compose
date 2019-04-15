FROM node
RUN git clone --depth=1 https://github.com/YMFE/yapi.git /vendors
WORKDIR /vendors
RUN npm install --production --registry https://registry.npm.taobao.org 
EXPOSE 30000
ENTRYPOINT ["node", "server/app.js"]

