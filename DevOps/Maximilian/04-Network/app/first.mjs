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


