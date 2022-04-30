# Prerequisites 
- sudo apt update
- sudo apt install curl
- sudo apt install default-jre
- sudo apt install default-jdk


- sudo apt-get install build-essential
- https://brew.sh/
- /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
- - brew install scala

# Kafka download
Should be same version as scala (2.13)
```
https://kafka.apache.org/downloads
tar -xvzf kafka.tgz
```

Broker
Producer
Consumer
# for custom settings
./config folder
# for broker
cat server.properties

# to start up kafka
bin

# windows
has batch files

# Topics
- Broker wraps topics
- Topics - named feed or category of messages.
- Ordered sequence (by time). Immutable events.
- Data as events is arch style (Event sourcing).
- Each message has timestamp and referencable identifier and binary payload
- **Message Offset**: Each consumer has a bookmark of last read message. Offset is the message identifier
- Different consumers have different offset positions. And they pick if stay, go back or go forward.
- Kafka doesnt have issue with slow consumers and message retention. Kafka retains all message within time period.
- Default retention period is 168 hours. It can be specified on per-topic.

# Start up
```
# start up zookeper
bin/zookeper-server-start.sh config/zookeeper.properties
telnet localhost 2181

# start up broker
bin/kafka-server-start.sh config/server.properties

# create topic
bin/kafka-topics.sh --create --topic my_topic -zookeper localhost:2181 --replication-factor 1 --partitions 1
```