FROM node
WORKDIR /bojan
COPY ./package.json /bojan
RUN npm install
COPY . /bojan
CMD ["node", "app.mjs"]