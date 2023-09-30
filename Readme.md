
Descargar Apache Kafka:
```
wget https://archive.apache.org/dist/kafka/2.2.0/kafka_2.11-2.2.0.tgz
```

Descomprime el archivo descargado:
```
tar -xzf kafka_2.11-2.2.0.tgz
```
##########################################################################

Instala Java OpenJDK 11:
```
sudo apt install openjdk-11-jre-headless
```

Instala el JDK (Java Development Kit):
```
sudo apt install default-jdk
```

##########################################################################

Accede al directorio de Kafka:
```
cd kafka_2.11-2.2.0
```

##########################################################################

configurar nodo zookeeper:
* se puede crear una carpeta distinta para configurar dataDir
  dataDir=/tmp/zookeeper

ruta:
```
root@1be86383f47d:~/probando/kafka_2.11-2.2.0/config# cat zookeeper.properties

```

inicio zookeeper:
```
root@1be86383f47d:~/probando/kafka_2.11-2.2.0# ./bin/zookeeper-server-start.sh ./config/zookeeper.properties
```

##########################################################################

configurar nodo kafka:
* cada nodo (broker) que se vaya a arrancar tiene que tener un id unico
  (broker.id=0 para un nodo , broker.id=1 para otro y asi..)

* se puede crear otra carpeta de logs
  log.dirs=/tmp/kafka-logs

* conexion cambiar el localhost por la ip de la maquina con el nodo (broker)
  zookeeper.connect=localhost:2181

* si estoy probando contenedores en la misma maquina tengo que configurar listeners
  listeners=PLAINTEXT://:9092 por listeners=PLAINTEXT://172.17.0.5:9092 
  (172.17.0.5 es un ejemplo la ip de la propia maquina)

ruta:
```
root@1be86383f47d:~/probando/kafka_2.11-2.2.0/config# cat server.properties

```

inicio nodo (broker) en kafka:
```
root@1be86383f47d:~/probando/kafka_2.11-2.2.0# ./bin/kafka-server-start.sh ./config/server.properties

```

##########################################################################

probar producer:
```
./bin/kafka-console-producer.sh --broker-list localhost:9092 --topic mi_topico
```

probar consumer:
```
para ver toda la lista del topic:
./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic mi_topico --from-beginning
```




