Kafka is distributed commit log.

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
[Kafka quickstart](https://kafka.apache.org/quickstart)
```
# start up zookeper
./bin/zookeeper-server-start.sh config/zookeeper.properties 
telnet localhost 2181

# start up broker
./bin/kafka-server-start.sh config/server.properties 

# create topic
bin/kafka-topics.sh --create --topic books --bootstrap-server localhost:9092
cd /tmp/kafka-logs/books-0

# check topics
bin/kafka-topics.sh --list --bootstrap-server localhost:9092

# create messages with producers.sh
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic books
Message 1
Message 2
Message 3
Anything goes...

# consumer
bin/kafka-console-consumer.sh --topic books --from-beginning --bootstrap-server localhost:9092
```

# Log == Partitions
Number of partitions is configurable. Partitions enable fault tolerance and scalability.
Some partitions are on some brokers. 

The more partitions, more problems for zookeeper.
Global messaging order in topic is problematic
In that case you need single partition for topic.
or use consumer groups and handle order processing
with more partitions handling of master partitions to copy can be slower

Replication factor should be set to n-1. Minimum of 2-3. ISR in-sync replication metric.
If isr is equal to replication factor, than its in healthy state.

```
bin describe topic

start 3 brokers with 3 server-n.properties files

topic repl-factor 3 partition 1
describe topic and will see leader and replication

producer.sh --broker-list localhost:9092...
close one broker and desribe topic
add message
describe
return broker
describe
```

# Intelij
maven 1.8
com.package
project name
pom < kafka dependecies
org.apacke.kafka
kafka clients
version 8.10

expend kafka client lib, clients package(namespace)

// type contract
Properties props = new Properties();
props.put("bootsrap.servers", "BROKER-1:9092, BROKER-2:9093);
props.put("key.serializer", "org.apacke.kafka.common.serialization.StringSerializer")
props.put("value.serializer", "org.apacke.kafka.common.serialization.StringSerializer")

KafkaProducer prod = new KafkaProducer(props);

// ProducerRecord is the message
// Must match type contract
ProducerRecord(String topic, Integer partition, Long timestamp, K key, V value)

When adding to partition, it has 4 strategies
direct
round-robin
key-mod hash
custom