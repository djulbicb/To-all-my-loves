FROM node
WORKDIR /app
COPY ./package.json /app/package.json

RUN npm install

COPY . .

ARG DEFAULT_PORT=2000

ENV SOME_PORT $DEFAULT_PORT

EXPOSE $SOME_PORT

CMD ["npm", "start"]