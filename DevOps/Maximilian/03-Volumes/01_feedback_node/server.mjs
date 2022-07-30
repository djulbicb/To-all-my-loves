import express from "express";
import fs from "fs";
import path from "path";
import bodyparser from 'body-parser';
import {fileURLToPath} from 'url';
import { exists } from "fs";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
app.use(bodyparser.urlencoded({ extended: false }));
app.use(express.static('public'));
app.use('/feedback', express.static('feedback'));

app.get("/", (req, res) => {
    const filepath = path.join(__dirname, 'pages', 'feedback.html');
    console.log(filepath)
    res.sendFile(filepath);
})

app.get("/exists", (req, res) => {
    const filepath = path.join(__dirname, 'pages', 'exists.html');
    return res.sendFile(filepath)
})

app.post("/create", async (req, res) => {
    const title = req.body.title;
    const content = req.body.text;
    const adjTitle = title.toLowerCase();

    const tempFilePath = path.join(__dirname, 'temp', adjTitle + '.txt');
    const finalFilePath = path.join(__dirname, 'feedback', adjTitle + '.txt');

    await fs.writeFile(tempFilePath, content, (e)=>{console.log(e)});
    exists(finalFilePath, async (exists) => {
        if (exists) {
            res.redirect('/exists');
            return;
        } else {
            await fs.copyFile(tempFilePath, finalFilePath, (e)=>{console.log(e)});
            await fs.unlink(tempFilePath, (e)=>{console.log(e)});
            res.redirect('/');
            return;
        }
        res.redirect('/');
    });

    
})
console.log(process.env.SOME_PORT)
app.listen(process.env.SOME_PORT)
