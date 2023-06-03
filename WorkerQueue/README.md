# Work Queue to ditribute works among workers

The main idea behind work queue is to avoid resource intensive tasks run immediately on worker and wait for it to complete. Task will be scheduled on queue and sent as message to worker. Worker will pick the task and execute it in the background. When there are multiple workers, tasks will be shared among them.

### Message durability
We have learned how to make sure that even if the consumer dies, the task isn't lost. But our tasks will still be lost if RabbitMQ server stops.

When RabbitMQ quits or crashes it will forget the queues and messages unless you tell it not to. Two things are required to make sure that messages aren't lost: we need to mark both the queue and messages as durable.

First, we need to make sure that the queue will survive a RabbitMQ node restart. In order to do so, we need to declare it as durable:

    channel.queue_declare(queue='hello', durable=True)

### Fair dispatch
You might have noticed that the dispatching still doesn't work exactly as we want. For example in a situation with two workers, when all odd messages are heavy and even messages are light, one worker will be constantly busy and the other one will do hardly any work. Well, RabbitMQ doesn't know anything about that and will still dispatch messages evenly.

This happens because RabbitMQ just dispatches a message when the message enters the queue. It doesn't look at the number of unacknowledged messages for a consumer. It just blindly dispatches every n-th message to the n-th consumer.

Producer -> Queue -> Consuming: RabbitMQ dispatching messages.
In order to defeat that we can use the Channel#basic_qos channel method with the prefetch_count=1 setting. This uses the basic.qos protocol method to tell RabbitMQ not to give more than one message to a worker at a time. Or, in other words, don't dispatch a new message to a worker until it has processed and acknowledged the previous one. Instead, it will dispatch it to the next worker that is not still busy.

    channel.basic_qos(prefetch_count=1)

### How to run 
1. Open 4 terminal and run consumer.py from 3 of them.
2. Now run producer.py from 4th terminal and specify multiple dots(.) in argument 
    python3 producer.py Pune........
3. Now you can produce mutiple messages and check consumer is getting them one by one.

