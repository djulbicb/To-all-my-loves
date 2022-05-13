# Start
If you install using apt, brew ... commands are kafka-topics. If its installed via binaries then kafka-topics.sh

### Kafka download
Should be same version as scala (2.13)
```
https://kafka.apache.org/downloads
tar -xvzf kafka.tgz
```

### Starting kafka with zookeeper 
Config folder contains properties file services. ie. folder `/tmp` is specified for data location.
```
zookeeper-server-start.sh config/zookeeper.properties
kafka-server-start.sh config/server.properties
```

### Start up Kafka on Linux with KRaft Mode (no zk)
Not production ready. Good for one broker
```
# generate uuid for cluster and copy to second command
kafka-storage.sh random-uuid
kafka-storage.sh format -t <uuid> -c config/kraft/server.properties
kafka-server-start.sh config/kraft/server.properties
```

### Start multiple brokers
```
bin/kafka-server-start.sh config/server-1.properties
bin/kafka-server-start.sh config/server-2.properties

//config/server-1.properties:
broker.id=1
listeners=PLAINTEXT://:9093
log.dir=/tmp/kafka-logs-1
```
# Commands
## `kafka-topics.sh`
When defining name for a topic character `_` and `.` are interchangeable. (first_topic == first.topic;).

In earlier replication and partitions param were required. Now it has default
```
# connect to bootstrap server
kafka-topics --bootstrap-server localhost:9092 --list
kafka-topics --bootstrap-server localhost:9092 --create --topic first_topic

kafka-topics --bootstrap-server localhost:9092 --create --topic first_topic --partitions 3

kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic first_topic

kafka-topics.sh --bootstrap-server localhost:9092 --describe

kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic first_topic
```

## `kafka-console-producer.sh`
By default we are creating messages without keys, so messages are distributed on all partitions.
```
kafka-topics --bootstrap-server localhost:9092 --topic first_topic --partitions 3 --create
kafka-console-producer --bootstrap-server localhost:9092
message 1
message 2
CTRL+C

kafka-console-producer --bootstrap-server localhost:9092 --topic first_topic --producer-property acks=all
message 3

kafka-console-producer --bootstrap-server localhost:9092 --topic non-exisiting-topic
kafka will create a topic and define leader

kafka-topics --bootstrap-server localhost:9092 --describe new_topic


# with keys
kakfa-console-producer --bootstrap-server localhost:9092 --topic first --property parse.key=true --property key.separator=:
example key:value
user_id_1234:Stephane
hello >>> Kafka Exception no key
```

# Kafka-console-consumer.sh
```
# by default reads at end, ignores before messages.
# write new message after starting 
kafka-console-consumer --bootstrap-server localhost:9092 --topic first_topic

kafka-console-consumer --bootstrap-server localhost:9092 --topic first_topic --from-beginning
# when you read it, messages will look its random. It actually in order withing partitions

# display key, values and timestamp in consumer
kafka-console-consumer --bootstrap-server localhost:9092 --topic first_topic --formatter kafka.tools.DefaultMessageFormatter --property print.timestamp=true --property print.key=true --property print.value=true --from-beginning
```

# Concumser groups
```
# have consumer and producer and topic withy 3 partitions. Only one consumer per parttition

# create two consumers with consumer group
kafka-console-producer --bootstrap-server localhost:9092 --topic first_topic --group my-group
message
it will go one consumer not the other one.

# create second consumer group, one consumer


# describe groups 
kafka-consumer-groups --bootstrap-server localhost:9092 --describe --group my-group
- shut down consumers
make consumer and 4 messages
and describe

kafka-consumer-groups --bootstrap-server localhost:9092 --list
kafka-consumer-groups --bootstrap-server localhost:9092 --describe --group consome-consumer-123

make new consumer without group and list it. it is emphemeral
kafka-consumer-groups --bootstrap-server localhost:9092 --list
```

# Reset offsets
```
kafka-consumer-groups --bootstrap-server localhost:9092 --list
kafka-consumer-groups --bootstrap-server localhost:9092 --describe --group my-group
kafka-consumer-groups --bootstrap-server localhost:9092 --group my-group --reset-offsets --to-earlist --execute --all-topics

# reads all messages now
kafka-console-consumer ---bootstrap-server localhost:9092 --topic first --group my_group

kafka-consumer-groups --bootstrap-server localhost:9092 --group my-group --reset-offsets --shift-by -2 --execute --all-topics
```


