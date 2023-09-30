
Descargar Apache Kafka y descomprimir:
```
wget https://archive.apache.org/dist/kafka/2.2.0/kafka_2.11-2.2.0.tgz
tar -xzf kafka_2.11-2.2.0.tgz
```

Instala Java OpenJDK 11 y JDK (Java Development Kit):
```
sudo apt install openjdk-11-jre-headless
sudo apt install default-jdk
```

Instalar confluent-kafka para Python3
```
pip install confluent-kafka
```

Accede al directorio de Kafka:
```
cd kafka_2.11-2.2.0
```

configurar ZooKeeper:
se recomienda crear una carpeta especifica para configurar dataDir en lugar de /tmp/zookeeper,
para asegurarte de que los datos de ZooKeeper no se borren automaticamente.
original: dataDir=/tmp/zookeeper
editada:  dataDir=/ruta/de/tu/eleccion
```
root@1be86383f47d:~/probando/kafka_2.11-2.2.0/config# cat zookeeper.properties
````
`inicio ZooKeeper` (necesita estar funcionando antes de iniciar kafka):
```
root@1be86383f47d:~/probando/kafka_2.11-2.2.0# ./bin/zookeeper-server-start.sh ./config/zookeeper.properties
```

configurar Kafka:
* cada nodo kafka (broker) que se vaya a arrancar tiene que tener un id unico
  (broker.id=0 para un nodo , broker.id=1 para otro y asi..)
* se puede crear otra carpeta de logs
  log.dirs=/tmp/kafka-logs
* se puede cambiar conexion del localhost por la ip de la maquina con el nodo (broker)
  zookeeper.connect=localhost:2181
* si estoy probando contenedores en la misma maquina tengo que configurar listeners
  listeners=PLAINTEXT://:9092 por listeners=PLAINTEXT://172.17.0.5:9092 
  (172.17.0.5 es un ejemplo la ip de la propia maquina)


`inicio kafka`:
```
root@1be86383f47d:~/probando/kafka_2.11-2.2.0# ./bin/kafka-server-start.sh ./config/server.properties
```

####################################
########### Para pruebas ###########
####################################

ejecutar el producer en un tab:
```
./bin/kafka-console-producer.sh --broker-list localhost:9092 --topic mi_topico
```

ejecutar el consumer en otro tab:
```
para ver toda la lista del topic:
./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic mi_topico --from-beginning
```