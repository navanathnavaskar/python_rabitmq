#!/Users/navanath.navaskar/rabbitmqenv/bin/python3

import pika
import sys

# Create connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

# Create channel
channel = connection.channel()

# Connect to exchange
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

# Queue
result = channel.queue_declare('', exclusive=True)

queue_name = result.method.queue

binding_keys = sys.argv[1:]

if not binding_keys:
    sys.stderr.write("Usage : {} [binding_key] ...\n ".format(sys.argv[0]))
    sys.exit(1)

# bind key to queue
for bk in binding_keys:
    channel.queue_bind(
        exchange='topic_logs',
        queue=queue_name,
        routing_key=bk
    )

print("Waiting for logs... Press ctrl + C to exit.")

def callback(ch, method, properties, body):
    print("[X] Received : {} from {}".format(body, method.routing_key))

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()