FROM node:18

WORKDIR /ui

# Copy package.json and package-lock.json
COPY package*.json /ui/

RUN npm install

COPY . .

CMD ["npm", "start"]
