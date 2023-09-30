from confluent_kafka import Producer

# configuracion del productor Kafka
config = {
    'bootstrap.servers': 'localhost:9092',  # Cambia esto a la dirección de tu servidor Kafka
}

# objeto productor Kafka
producer = Producer(config)

# Nombre del tema al que enviar los mensajes
topic = 'mi_topico'  # Cambia esto al nombre de tu tema

try:
    while True:

        # Leer el mensaje desde la entrada estandar
        mensaje = input("> ")

        # envia el mensaje al tema
        producer.produce(topic, key=None, value=mensaje)

except KeyboardInterrupt:
    pass
finally:
    producer.flush()  # Asegura que todos los mensajes pendientes se envíen antes de salir
