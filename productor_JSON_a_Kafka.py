from confluent_kafka import Producer
import json

# configuracion del productor Kafka
config = {
    'bootstrap.servers': 'localhost:9092',  # Cambia esto a la direccion de tu servidor Kafka
}

# objeto productor Kafka
producer = Producer(config)

# nombre del tema al que enviar los mensajes
topic = 'mi_topico'  # cambia esto al nombre de tu tema

try:
    with open('infocasas.json', 'r') as file:
        data = json.load(file)

    # enviar el diccionario al tema
    producer.produce(topic, key=None, value=json.dumps(data))

except FileNotFoundError:
    print("El archivo JSON no fue encontrado.")
except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # asegura que todos los mensajes pendientes se envien antes de salir
    producer.flush()