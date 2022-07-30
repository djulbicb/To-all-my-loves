import express from 'express'
import {body, h1} from './boilerplate.mjs'
import * as html from './boilerplate.mjs'
import bodyParser from 'body-parser'

const app = express()

app.use(bodyParser.json())
app.use(express.static('public'))

let data = {}

app.get("/", (req, res) => {
    console.log("/")

    const lis = Object.keys(data).map(key => {
        return html.li(key + ":" + data[key])
    })
    console.log(lis)

    const content = html.body(html.h1("Hello!") + html.p("Love you <3") + html.ul(lis))
    res.send(content)
})

app.post("/", (req, res) => {
    data = {...data, ...req.body};
    console.log(data);
    res.sendStatus(200);
})

app.listen(3000)