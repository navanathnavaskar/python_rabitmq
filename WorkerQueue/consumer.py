#!/Users/navanath.navaskar/rabbitmqenv/bin/python3

import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

print("[X] Waiting for messages.  Press Ctrl + C to exit.")

def callback(ch, method, properties, body):
    print("[X] Received %s", body.decode())
    time.sleep(body.count(b'.'))
    print("[X] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    
channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()