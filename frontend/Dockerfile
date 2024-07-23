FROM node:22-alpine3.19

RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app

WORKDIR /home/node/app

COPY --chown=node:node . .

RUN npm install

USER node

EXPOSE 3000

CMD [ "npm", "run", "dev"]
