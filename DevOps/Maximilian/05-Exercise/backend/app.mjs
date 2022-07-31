import express from "express";
import mongoose from "mongoose";
import fs from "fs";
import path from "path";
import {fileURLToPath} from 'url';
import bodyParser from "body-parser";
import morgan from "morgan";
import Goal from "./model/Goal.mjs";
import cors from "cors"

const app = express()
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const accessLogStream = fs.createWriteStream(
    path.join(__dirname, 'logs', 'access.log'),
    { flags: 'a' }
);
app.use(morgan('combined', { stream: accessLogStream }));
app.use(bodyParser.json());
// app.use(cors({
//     origin: '*'
// }));

app.use((req, res, next) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  next();
});

app.get("/goals", async (req, res) => {
    console.log("TRYING TO FETCH GOALS")
    
    try {
        const goals = await Goal.find();
        res.status(200).json({
            goals: goals.map((goal) => ({
                id: goal.id,
                text: goal.text
            }))
        })
        console.log("FETCHED GOALS")
    } catch(err) {
        console.log("ERROR FETCHING GOALS")
        console.log(err.message)
        res.status(500).json({message: "Failed to load goals"})
    }
})

app.post("/goals", async(req, res) => {
    const goalText = req.body.text;
    const goal = new Goal({
        text: goalText
    });

    if (!goalText || goalText.trim().length === 0) {
        console.log('INVALID INPUT - NO TEXT');
        return res.status(422).json({ message: 'Invalid goal text.' });
      }

    try {
        await goal.save()
        res.status(201)
           .json({message: "Goal saved", goal: {id: goal.id, text: goal.text}});
    } catch (err) {
        console.log("ERROR FETCHING GOALS")
        res.status(500)
            .json({message: "Failed to save goal"})
    }
})

app.delete('/goals/:id', async (req, res) => {
    console.log('TRYING TO DELETE GOAL');
    try {
      await Goal.deleteOne({ _id: req.params.id });
      res.status(200).json({ message: 'Deleted goal!' });
      console.log('DELETED GOAL');
    } catch (err) {
      console.error('ERROR FETCHING GOALS');
      console.error(err.message);
      res.status(500).json({ message: 'Failed to delete goal.' });
    }
  });

mongoose.connect(
    `mongodb://localhost:27017/course-goals`,
    {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    },
    (err) => {
      if (err) {
        console.error('FAILED TO CONNECT TO MONGODB');
        console.error(err);
      } else {
        console.log('CONNECTED TO MONGODB!!');
        app.listen(2000);
      }
    }
  );