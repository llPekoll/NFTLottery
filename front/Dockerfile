FROM node:14-alpine

WORKDIR /lottery

COPY lottery/package.json /lottery

RUN yarn install

COPY lottery/. /lottery

RUN yarn run build
WORKDIR /lottery
RUN rm -rf node_modules 

EXPOSE 3000
