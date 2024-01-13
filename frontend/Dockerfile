FROM node:lts-alpine

RUN mkdir -p /project/frontend
WORKDIR /project/frontend

COPY package*.json .

RUN npm install

COPY . .

CMD [ "npm", "run", "dev" ]
