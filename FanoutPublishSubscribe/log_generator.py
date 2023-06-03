#!/Users/navanath.navaskar/rabbitmqenv/bin/python3

import pika
import sys

# Create connection to RabbitMQ host
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

# Create Channel
channel = connection.channel()

# Create Exchange named logger and type as Fanout to send message to all queues 
channel.exchange_declare(exchange='logger', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World"

# Publish message to exchange with routing_key as empty, exchange will create temporary 
# queues and push msg to all queues
channel.basic_publish(exchange='logger', routing_key='', body=message)

print("[S] Sent Log : {}".format(message))

connection.close()



