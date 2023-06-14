#!/Users/navanath.navaskar/rabbitmqenv/bin/python3

import pika
import sys

# Create connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

# create channel
channel = connection.channel()

# create exchange of type topic
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

# get routing key from command line arg
routing_key = sys.argv[1] if len(sys.argv) > 2 else 'basic.info'

message = ' '.join(sys.argv[2:]) or "Hello World"

# Publish message to queue
channel.basic_publish(
    exchange='topic_logs',
    routing_key=routing_key,
    body=message
)

print("Sent: {} to {} queue".format(message, routing_key))

connection.close()
