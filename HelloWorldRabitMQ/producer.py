#!/Users/navanath.navaskar/rabbitmqenv/bin python3

import pika

# Create connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

# Create channel
channel = connection.channel()

# Create queue for sending messages
channel.queue_declare(queue='hello')

i = 0
while i < 10:
    channel.basic_publish(exchange='', routing_key='hello', body=f"Hello Friend {i}" )
    i = i + 1
    print("Sent Hello Friends successfully !")
    
connection.close()
