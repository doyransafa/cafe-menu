FROM node:lts-alpine

WORKDIR /project/frontend

COPY package.json .
RUN npm i

COPY . .

EXPOSE 8080

CMD ["npm", "run", "dev"]
