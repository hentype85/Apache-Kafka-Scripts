from confluent_kafka import Consumer, KafkaError

# configuracion del consumidor Kafka
config = {
    'bootstrap.servers': 'localhost:9092',  # Cambia esto a la dirección de tu servidor Kafka
    'group.id': 'my-consumer-group',  # Puedes cambiar el nombre del grupo según tus necesidades
    'auto.offset.reset': 'earliest'  # Esto establece el inicio desde el principio
}

# objeto consumidor Kafka
consumer = Consumer(config)

# suscripcion al tema
topic = 'mi_topico'
consumer.subscribe([topic])

try:
    while True:
        msg = consumer.poll(1.0)  # Espera un segundo por mensajes

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print('Fin de la partición, continuando...')
            else:
                print('Error en el mensaje: {}'.format(msg.error()))
        else:
            print('Mensaje recibido: {}'.format(msg.value().decode('utf-8')))

except KeyboardInterrupt:
    pass

finally:
    consumer.close()
