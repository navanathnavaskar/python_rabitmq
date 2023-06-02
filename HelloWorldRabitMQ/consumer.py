#!/Users/navanath.navaskar/rabbitmqenv/bin python3

import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    
    def callback(ch, method, properties, body):
        print("[*] Received Info - {}".format(body))
    
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    
    print("[*] Waiting for messages. Click Ctrl + C to exit.")
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted By User')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
            