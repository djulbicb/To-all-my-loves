# Kafka
In the beginning its easy, move data from source to target. But later there are multiple targets and sources, multiple protocols, data formats....
This problem is solved by **decoupling using apache Kafka**.

**Data streams** is real-time data transfer. Kafka is data transportation mechanism.

Stuff like:
- website events
- pricing data
- financial transactions
- user interactions
- messaging system
- activity tracking
- gather metrics from different locations
- application logs gathering
- stream processing
- integration with spark, flink, storm, hadoop
- micro service pub/sub

Target systems are:
- database
- analytics
- email system
- audit

### Examples:
- Netflix: Recommendations for tv.
- Uber: Gather user, taxi, trip data in real time and compute, forecast demand. Surge pricing in real time
- Linkedin: Prevent spam, collect interactions to make connection recommendations.

### Order of tutorials to take:
- **Kafka for Beginners**: Base knowledge 
- **Kafka Connect API**: Import/Export to/from Kafka
- **Kafka Streams API**: Process and transform data withing Kafka
- **ksqlDB**: Write Kafka streams like using SQL
- **Confluent Components**: Rest Proxy and Schema Registry
- **Kafka Security**: Intergrate app with Kafka Security
- **Kafka Monitoring and Operations**: Prometheus and Grafana to monitor Kafka
- **Kafka Cluster Setup & Administration**: Deep understanding of Kafka & Zookeper
- **Confluent Certifications** for Developers/Operators Practice Exams

# Prerequisites
Requires isntalled Java and Scala.
```
apt update
apt install curl
apt install default-jre
apt install default-jdk
apt-get install build-essential
brew install scala
```

## Kafka download
Should be same version as scala (2.13)
```
https://kafka.apache.org/downloads
tar -xvzf kafka.tgz
```

# Start up
[Kafka quickstart](https://kafka.apache.org/quickstart)

## Start up Kafka on Linux with Zookeeper
### Add kafka bins
Download kafka binaries
```
nano .bashrc.rc
~/Documents/dev/kafka_2.13-3.1.0/bin
PATH="$PATH:~/Documents/dev/kafka_2.13-3.1.0/bin"

source .bashrc.rc
kafka-topics.sh
```
#### Start up zookeeper
```
# start zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties
```
#### Start up 2x brokers
```
bin/kafka-server-start.sh config/server-1.properties
bin/kafka-server-start.sh config/server-2.properties

//config/server-1.properties:
broker.id=1
listeners=PLAINTEXT://:9093
log.dir=/tmp/kafka-logs-1
 
//config/server-2.properties:
broker.id=2
listeners=PLAINTEXT://:9094
log.dir=/tmp/kafka-logs-2
min.insync.replicas=1
```
#### Create topic
```
bin/kafka-topics.sh --create --topic quick --partitions 3 --replication-factor 3 --min-insync-replicas 1 --bootstrap-server localhost:9092
bin/kafka-topics.sh --describe --topic quick --bootstrap-server localhost:9092
```
#### Write to topic
```
bin/kafka-console-producer.sh --topic quick --bootstrap-server localhost:9092
```
#### Read to topic
```
bin/kafka-console-consumer.sh --topic quick --from-beginning --bootstrap-server localhost:9092
```
