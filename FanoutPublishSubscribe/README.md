# Fanout Messages to All Consumers Subscribed to Queue

Here message will be delivered to all consumers. This pattern is called is Publish/Subscribe.

Lets build simple logging system where logs will be sent to multiple receivers like one receiver will store log while other will display them on Screen. In this approach, published messages will be broadcast to all the receivers.

### What is Exchange: 
The producer can only send messages to an exchange. One side of the exchange receives messages from producers and the other side pushes them to queues. The exchange must know exactly what to do with a message it receives. Should it be appended to a particular queue? Should it be appended to many queues? Or should it get discarded. The rules for that are defined by the exchange type. Exchange type can be topic, direct, headers and fanout.

Lets create Exchange:

  channel.exchange_declare(exchange='logs', exchange_type='fanout')

After Creating Exchange, we need to create temporary queues that can be deleted when connections are terminated. We just need live logs so need to make queues permanent.

  result = channel.queue_declare(queue='', exclusive=True)

Using exclusive=True, we tell RabbitMQ to delete queues after connections are closed.





