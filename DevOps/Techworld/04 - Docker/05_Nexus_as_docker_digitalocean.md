# Start up nexus as docker container

1. Create better droplet
```
Get better droplet
- Ubuntu
- Shared 
- Regular Intel with SSD
- 20$
 ```
2. Change name of droplet
docker-nexus

3. Add network firewall to droplet

4. Install docker
```
ssh root@555.55.555.555
apt update
snap install docker
docker 
```

5. Start up `sonatype/nexus3` docker
```
docker volume create --name nexus-data
docker run -d -p 8081:8081 --name nexus -v nexus-data -e CONTEXT_PATH=/  sonatype/nexus3
apt install net-tools
netstat -lpnt
555.55.555.555:8081

# Troubleshoot:
Q: nexus docker "Problem accessing /. Reason:"
A: -e CONTEXT_PATH=/
```

6. Check nexus container user

User nexus is by default created
```
docker exec -it nexus /bin/bash
whoami
exit
```

to view this, if not info in readme.
in dockerhub > tags > to see dockerfile
USER nexus on bottom

# 7. Where is data
```
docker volume ls
docker inspect nexus-data

# nexus-data on server
/var/snap/docker/common/var-lib-docker/volumes/nexus-data/_data

# nexus-data in container
ls nexus-data/
```
