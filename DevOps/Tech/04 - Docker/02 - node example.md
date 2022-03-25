**Working with mongo**
```
docker pull mongo
docker pull mongo-express
```

# Docker network
Docker po defaultu kreira isolated network za container. Za primer mongo i mongo express kreiramo zajednicki custom network, nema potrebe za **--net**.
Ako su dva containera u istom networku mogu da komuniciraju preko njihovog imena (**--name**) .

Outside of the docker network, communicaiton can be done over localhost. 
Containeri koji su deo zajednickog networka komuniciraju preko imena (**name**)

# Rucno startovanje mongo dockera
```
docker network ls
docker network create mongo-network
docker network ls

# da se assignuje networku containeru
docker run -p 27017:27017 -d -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=password --name mongodb --net mongo-network mongo
docker run -d \ 
-p 27017:27017 \ 
-e MONGO_INITDB_ROOT_USERNAME=admin \
-e MONGO_INITDB_ROOT_PASSWORD=password \
--name mongodb \ 
--net mongo-network \ 
mongo

docker run -d -p 8081:8081 -e ME_CONFIG_MONGODB_ADMINUSERNAME=admin -e ME_CONFIG_MONGODB_ADMINPASSWORD=passowrd --net mongo-network --name mongo-express -e ME_CONFIG_MONGODB_SERVER=mongodb mongo-express 
docker run -d \
-p 8081:8081 \
-e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
-e ME_CONFIG_MONGODB_ADMINPASSWORD=passowrd \
--net mongo-network \
--name mongo-express \
-e ME_CONFIG_MONGODB_SERVER=mongodb \
mongo-express 
```


# Kreiranje node aplikacije
```
# setup projekta
npm init
npm install mongo
npm install mongo-express
npm install

# startovanje
node start 
node server.js
```

# Using docker compose
Run command
```
docker-compose -f .\mongo-docker-compose.yaml up
```
**mongo-docker-compose.yaml**
```
version: '3'
services:
  mongodb:
    image: mongo
    ports:
      - 27017:27017
    environment:
      - MONGO_INITDB_ROOT_USERNAME=admin
      - MONGO_INITDB_ROOT_PASSWORD=password
  mongo-express:
    image: mongo-express
    ports:
      - 8080:8080
    environment:
      - ME_CONFIG_MONGODB_ADMINUSERNAME=admin
      - ME_CONFIG_MONGODB_ADMINPASSWORD=passowrd
      - ME_CONFIG_MONGODB_SERVER=mongodb
```
# Create custom docker image
Dockerfile is blueprint for creating docker images.
```
FROM node
ENV MONGO_DB_USERNAME=admin \
    MONGO_DB_PWD=password
RUN mkdir -p /home/app
COPY . /home/app
CMD ["node", "/home/app/server.js"]
```

**Buildovanje custom image**
```
docker build -t my-app:1.0 . 
docker run -p 3000:3000 my-app:1.0

docker rm <hash>
docker rmi <hash>
docker ps -a | grep my-app

docker exec -it <id> /bin/sh
docker exec -it <id> /bin/bash
# ls
# env
```
