# Project Note: kafka tutorial

>[[kafka] 카프카 시작하기 튜토리얼](https://devuna.tistory.com/88)

## Install 

>[Kafka download](https://kafka.apache.org/downloads)

or 

```shell
# wget example
$ wget https://downloads.apache.org/kafka/2.7.0/kafka_2.13-2.7.0.tgz
```

설치 후 압축 해제 

```shell
$ tar -xzf kafka_2.13-2.7.0.tgz
```

## start 

zookeeper 서버 먼저 실행 후, kafka 서버 실행

```shell
# 리눅스의 경우 
$ bin/kafka-server-start.sh config/server.properties 

# 윈도우의 경우 
$ \bin\windows>kafka-server-start.bat ../../config/server.properties
```

topic 생성 / 조회 / 삭제 

```shell
# 생성
$ kafka-topics.bat --create --bootstrap-server localhost:9092 --replication-factor 1 -partitions 1 --topic test-topic

# topic list 확인
$ kafka-topics.bat --list --bootstrap-server localhost:9092

# topic 상세 조회 
$ kafka-topics.bat --describe --topic test-topic --bootstrap-server localhost:9092

# 삭제 
$ kafka-topics.bat --delete --topic test-topic --bootstrap-server localhost:9092
```

producer & consumer test

```shell
# producer
$ kafka-console-producer.bat --broker-list localhost:9092 --topic test-topic

# consumer 
$ kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic test-topic --from-beginning
```



## Java producer 

maven depency 를 추가한 뒤, 필요한 클래스를 import 한 상태이다. 

```java
private void sendThreadDumps () {
    Properties configs = new Properties();
    try {
        configs.put("client.id", InetAddress.getLocalHost().getHostName());
    } catch (UnknownHostException e) { // getLocalHost() 로 부터 
        throw new RuntimeException(e);
    }
    // 카프카 브로커의 주소 목록은 2개 이상의 ip 와 port 를 설정하도록 권장하고 있다.
    configs.put("bootstrap.servers", "localhost:9092");
    // 나머지 key, value 에 대해 직렬화 설정
    configs.put("key.serializer",
                "org.apache.kafka.common.serialization.StringSerializer");
    configs.put("value.serializer",
                "org.apache.kafka.common.serialization.StringSerializer");
    
    // 카프카 프로듀서 인스터스 생성
    KafkaProducer< String, String > producer = new KafkaProducer < String,
    String >(configs);
    // 카프카가 제공하는 전송 객체 사용
    // final ProducerRecord<K, V> record = new ProducerRecord<>(topic, key, value);
    // final ProducerRecord<K, V> record = new ProducerRecord<>(topic, value); 
    ProducerRecord<String, String> record = new ProducerRecord < String, String >
        ("test-topic", "Hello"); // kafka 명령어로 생성한 test-topic 에 간단하게 Hello 전송 
    // send() API returns a future which can polled to get result of send()
    Future<RecordMetadata> future = producer.send(record);
    producer.close();
}
```

- 위 메서드를 실행한 뒤, 로컬에서 `kafka-console-consumer` 로 메시지 전송 여부를 확인 가능하다. 

