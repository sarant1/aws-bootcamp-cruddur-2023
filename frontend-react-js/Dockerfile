FROM node:16.18

ENV PORT=3000

WORKDIR /frontend-react-js

COPY package.json .
COPY package-lock.json .
RUN npm install

COPY . .

ENV NODE_ENV=development

EXPOSE ${PORT}
CMD ["npm", "start"]