FROM node
WORKDIR /app

COPY ./package.json /app/package.json
RUN npm install

RUN mkdir -p node_modules/.cache && chmod -R 777 node_modules/.cache

COPY ./ /app/

CMD ["npm", "start"]