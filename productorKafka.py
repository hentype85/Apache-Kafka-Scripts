from confluent_kafka import Producer

# configuracion del productor Kafka
config = {
    'bootstrap.servers': 'localhost:9092',  # cambia esto a la direccion de tu servidor Kafka
}

# objeto productor Kafka
producer = Producer(config)

# nombre del tema al que enviar los mensajes
topic = 'mi_topico'  # cambia esto al nombre de tu tema

try:
    while True:

        # leer el mensaje desde la entrada estandar
        mensaje = input("> ")

        # envia el mensaje al tema
        producer.produce(topic, key=None, value=mensaje)

except KeyboardInterrupt:
    pass
finally:
    # asegura que todos los mensajes pendientes se envien antes de salir
    producer.flush()
