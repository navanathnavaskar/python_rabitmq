#!/Users/navanath.navaskar/rabbitmqenv/bin/python3

import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()

channel.exchange_declare(exchange='direct_log', exchange_type='direct')

# create queue that will be deleted once connection are closed
result = channel.queue_declare(queue='', exclusive=True)

queue_name = result.method.queue

severities = sys.argv[1:]

if not severities:
    sys.stderr.write("Usage : %s [info] [error] [warning]", sys.argv[0])
    sys.exit(0)
    
for severity in severities:
    channel.queue_bind(exchange='direct_log', routing_key=severity, queue=queue_name)
    
print("[G] Waiting for logs. Press Ctrl + C TO EXIT.")

def callback(ch, method, properties, body):
    print("[S] %r %r" %(method.routing_key, body))

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
