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