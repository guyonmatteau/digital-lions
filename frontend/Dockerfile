FROM node:lts-alpine

RUN npm install -g http-server typescript

WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# Compile TypeScript files
RUN tsc

# build app for production with minification
RUN npm run build

EXPOSE 5173
CMD [ "npm", "run", "dev", "--", "--host", "--port", "5173"]
