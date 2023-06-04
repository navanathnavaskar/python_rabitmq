#!/Users/navanath.navaskar/rabbitmqenv/bin/python3

import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()

# create direct exchange
channel.exchange_declare(exchange='direct_log', exchange_type='direct')

# get severity
severity = sys.argv[1] if len(sys.argv) > 1 else "info"

# get message 
message = ' '.join(sys.argv[2:]) or "Hello World"

channel.basic_publish(exchange='direct_log', routing_key=severity, body=message)

print("[X] Sent %s %s",severity, message)

connection.close()