# Network
Types of communications:
- with internet (enabled by default)
- with localhost (via docker port)
- with other containers (via network)

## SCENARIO 1: LOCAL DEVELOPMENT
### docker
```
docker run -p 27017:27017 --name mongo mongo
```
### .env
```
SECOND_APP_URL=localhost
SECOND_APP_PORT=4000
DB_MONGO_APP=localhost
DB_MONGO_PORT=27017
```

### package.json
```
{
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start-first": "nodemon first.mjs"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "axios": "^0.27.2",
    "body-parser": "^1.20.0",
    "dotenv": "^16.0.1",
    "express": "^4.18.1",
    "mongodb": "^4.8.1",
    "nodemon": "^2.0.19"
  }
}
```
### second.mjs 
```
import express from "express"

const app = express();

app.get("/api", (req, res) => {
    const response = {
        app: "Second app",
        endpoint: "/api",
        method: "GET"
    }
    res.send(JSON.stringify(response));
})

app.post("/api", (req, res) => {
    const response = {
        app: "Second app",
        endpoint: "/api",
        method: "POST"
    }
    res.send(JSON.stringify(response));
})

app.listen("4000")
```
start backend
```
npm run start-second
```

### first.mjs
```
import express from "express"
import axios from "axios";
import { MongoClient } from "mongodb";
import dotenv from 'dotenv';

dotenv.config();
console.log(process.env)

const app = express();

// OPTION 1: INTERNET
app.get("/", (req, res) => {
    res.send("Love <3")
})
app.get("/users", async (req, res) => {
    await axios.get("https://jsonplaceholder.typicode.com/users").then(data => {
        const apiContent = data.data;
        res.send(apiContent)
    }).catch(e => {
        console.log(e)
        res.send("Api not working")
    })
})

// OPTION 2: BACKEND APP 
app.get("/second-app", async (req, res) => {
    await axios.get(`http://${process.env.SECOND_APP_URL}:${process.env.SECOND_APP_PORT}/api`).then(response => {
        res.send(response.data)
    }).catch(err => {
        console.log(err)
        res.send("Second api GET not working")
    })
})
app.post("/second-app", async (req, res) => {
    await axios.get(`http://${process.env.SECOND_APP_URL}:${process.env.SECOND_APP_PORT}/api`).then(response => {
        res.send(response.data)
    }).catch(err => {
        console.log(err)
        res.send("Second api POST not working")
    })
})

// OPTION 3: MONGO
let iteration = 0;
const url = `mongodb://${process.env.DB_MONGO_APP}:${process.env.DB_MONGO_PORT}`;
const client = new MongoClient(url);
const dbName = 'myProject';
const dbCollection = "documents";

app.get("/mongo", async (req, res) => {
   await client.connect();
   console.log('Connected successfully to server');
   const db = client.db(dbName);
   const collection = await db.collection(dbCollection).find({}).toArray()
   console.log('Fetched data from Mongo');
   res.send(collection);
})
app.post("/mongo", async (req, res) => {
    await client.connect();
   console.log('Connected POST successfully to server');
   const db = client.db(dbName);

   iteration = iteration + 1;
   db.collection(dbCollection).insertOne({
        iteration: iteration,
        word: "Love"
   })
   res.send( `Item saved ${iteration}`)
})

app.listen("2000")
```

## SCENARIO 2: App is dockerized, contact localhost
On windows/mac string `host.docker.internal` references to localhost. On Linux `172.17.0.1` 

Second app is running on localhost with `npm run start-second`. First app contacts second app endpoint `/second-app`.
### Dockerfile.first
```
FROM node

WORKDIR /app
COPY ./package.json /app/package.json
RUN npm install

COPY ./ /app

ENV RUN_ENV=456
ENV DOCKERFILE_ENV=789

CMD ["npm", "run", "start-first"]

=========================================================
commands:
docker build -f Dockerfile.first -t first-app .
docker run -p 2000:2000 -d --rm -e SECOND_APP_URL=172.17.0.1 -e RUN_ENV=123 --name first first-app
```

## SCENARIO 3: Both apps are dockerized
Done in two ways
- by contacting container port directly
- by placing all containers in same network and contacting via container name

### Contact container port directly
In inspect logs field `IPAddress` shows container address.
```
docker run -d -p 27017:27017 --name mongo mongo

docker inspect mongo
"GlobalIPv6Address": "",
"GlobalIPv6PrefixLen": 0,
"IPAddress": "172.17.0.3",
"IPPrefixLen": 16,
"IPv6Gateway": "",

docker run -p 2000:2000 -d --rm -e DB_MONGO_APP=172.17.0.3 -e SECOND_APP_URL=172.17.0.1 -e RUN_ENV=123 --name first first-app
```

### Use network
Unlike volumes which are created automatically when used for first time - network have to be defined first.
```
docker network create my-net
docker run -d -p 27017:27017 --rm --network my-net --name mongo mongo
docker run -p 2000:2000 -d --rm --network my-net -e DB_MONGO_APP=mongo -e SECOND_APP_URL=172.17.0.1 -e RUN_ENV=123 --name first first-app
```