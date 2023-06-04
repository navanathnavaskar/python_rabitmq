# Subscribe to subset of messages

Using Fanout exchange, we can broadcast messages to all queues in exchange. But sometime we don't want to get all messages. We may need to store only Error messages to disk and ignore all other using first receiver. We may need to display all messages to screen using one receiver.

# Direct exchange
Our logging system from the previous tutorial broadcasts all messages to all consumers. We want to extend that to allow filtering messages based on their severity. For example we may want the script which is writing log messages to the disk to only receive critical errors, and not waste disk space on warning or info log messages.

We will use a direct exchange instead. The routing algorithm behind a direct exchange is simple - a message goes to the queues whose binding key exactly matches the routing key of the message.

