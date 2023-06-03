#!/Users/navanath.navaskar/rabbitmqenv/bin/python3

import pika

# Create connection 
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

# Create channel
channel = connection.channel()

# create exchange of type fanout
channel.exchange_declare(exchange='logger', exchange_type='fanout')

# Create queue with empty name, exchange will create it with unique name. we can get name later
# Make this queue temporary set exclusive=True
result = channel.queue_declare(queue='', exclusive=True)

queue_name = result.method.queue

# Bind exchange and queue
channel.queue_bind(exchange='logger', queue=queue_name)

print('[G] Waiting for loggs. Press Ctrl + C to exit.')

def callback(ch, method, properties, body):
    print("[L] {}".format(body))
    print("Method : {}".format(method))
    print("Properties : {}".format(properties))
    print("Channel : {}".format(ch))

channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True
)

channel.start_consuming()