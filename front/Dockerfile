
FROM node:14-alpine

WORKDIR /usr/src/app

COPY app/package.json ./

RUN yarn install

COPY app/. ./

RUN yarn run build
WORKDIR /app
RUN rm -rf node_modules 

EXPOSE 3000

CMD [ "node", "build" ]
