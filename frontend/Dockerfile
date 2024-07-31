FROM node:20.12.2

WORKDIR /usr/src/app

COPY package.json ./

RUN npm install --omit=dev

COPY . .

RUN npm run build

CMD [ "npm", "run", "dev" ]
