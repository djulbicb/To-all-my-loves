# Arguments and environment properties
Docker support build argument and runtime environment variables. Argument available during Dockerfile build, variables during Dockerfile build and runtime.

## Environment properties
- Define `ENV SOME_PORT 2000` in Dockerfile.
- Access variable in code via `proces.env.SOME_PROPERTY`. 
- `docker run -p 3000:1500 -e SOME_PORT=1500 -d --rm --name feedback feedback`

### package.json
```
{
  "name": "feedback",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "start": "cross-env NODE_ENV=dev && nodemon server.mjs",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "body-parser": "^1.20.0",
    "cross-env": "^7.0.3",
    "express": "^4.18.1",
    "nodemon": "^2.0.19"
  }
}
```
### Dockerfile
```
FROM node
WORKDIR /app
COPY ./package.json /app/package.json
RUN npm install
COPY . .

ENV SOME_PORT 2000
EXPOSE $SOME_PORT

CMD ["npm", "start"]
```

### server.js
```
console.log(process.env.SOME_PORT)
app.listen(process.env.SOME_PORT)
```

### command
```
docker run -p 3000:1500 -e SOME_PORT=1500 -d --rm --name feedback feedback
```

# Load environment prop via file
### .env
```
PORT=2000
SOME_PROPERTY=whatever
```
### command
```
docker run -p 3000:1500 -e SOME_PORT=1500 --env-file ./.env -d --rm --name feedback feedback
```

# Build arguments
With this you can build different version of the same image
### Dockerfile
```
ARG DEFAULT_PORT=2000
ENV SOME_PORT $DEFAULT_PORT
```
### command
```
docker run -p 3000:1500 -e SOME_PORT=1500 --build-arg DEFAULT_PORT=8000 -d --rm --name feedback feedback
```