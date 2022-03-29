FROM node:17-buster-slim

WORKDIR /app

COPY package.json /app
COPY package-lock.json /app

RUN npm ci
COPY . /app

USER node
ENTRYPOINT ["npm", "start"]
