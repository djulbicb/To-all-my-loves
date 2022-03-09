# Typical CI/CD process
1. project code
2. commit to git
3. Jenksins build docker
4. pushes to repo
5. deployed to dev server using jenkins
6. test app on server

# Docker image
That is the actual package, application, configuration, scripts... To je artifact that is movable
When an image is pulled and started, a container is created

# Docker containers
- Container is a virtual environment that hosts application. 
- A way to package application with all dependencies and configuration. Portable artifact.
- Container is layers of images.
- Base images are mostly linux base image like alpine.
- Application image is on top. In the middle is configuration.

**Starting docker containers**
```
docker run postgres:9.6
docker ps

docker run -p outside:inside redis
docker run -p 1234:6379 -d redis
docker stop <id>

# rerun stopped container
docker start <id>

# name redis
docker run -d -p 6001:6379 --name red-instance redis

# run command
docker exec -it <id> /bin/bash

# docker logs
docker images
docker ps
docker logs <id>
docker logs <name_of_container>

docker logs <id> | tail
# stream logs
docker logs <id> -f
```




