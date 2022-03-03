# Create droplet, upload java app and expose to outside [56 57]

> Create account. Use promo code`SAMMY60DAY`

1. Build project
   https://github.com/djulbicb/echo4j
```
./gradlew build     > ./build/libs/java.jar
maven package       > ./target/java.jar
```
2. Create droplet

![](img\01_droplet_header.png) 
```
# create droplet in digital ocean
DO > Droplets > Create Ubuntu droplet
              > Shared CPU, Regular Intel with SSD
              > Frankfurt
              > Add SSH keys
              
# create ssh key. In /home/.ssh
ssh-keygen

# change security ssh
DO > Settings > Security > SSH
https://cloud.digitalocean.com/account/security?i=f5a382
```

3. Set up networking

By default server is closed to external connection. 
No firewall rules that allow connection to port on server. We need to add Inbound SSH and Custom Inbound Port

Inbound is on which ports is connection allowed. Outbound na koje servere moze da se posalje request.
```
Select droplet > Networking > Firewalls: Edit > Create firewall rule
                                              > SSH - TCP - 22 - Sources: specify only my IP address or range  
                                              > Assign networking to droplet
                                              # for IO Type in google what is my IP address
                                              
Expose app port
Select Droplet > Networking > Select Firewall > New Custom TCP Port 8080 to all ip4, ip6 
```

4. SSH to server, and SCP

```
ssh root@555.55.55.55
apt install openjdk-8-jre-headless
exit

scp .\target\echo-0.0.1-SNAPSHOT.jar root@555.55.55.55:/root

ssh root@555.55.55.55
java -jar echo-0.0.1-SNAPSHOT.jar
# runs in background
java -jar echo-0.0.1-SNAPSHOT.jar &
```

5. Go to app - Enjoy
```
http://555.55.55.55:8080/I%20love%20you
```
![](img/02_droplet_test_iloveyou.png)

6. Close app
```
ps aux | grep java
kill <id>

apt install net-tools
netstat -lpnt
```
