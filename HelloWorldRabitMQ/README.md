# Basic Producer Consumer using RabbitMQ

### Install RabitMQ server on you server and start it. Follow steps given below for RabbitMQ installation:
##### 1. Windows : https://www.rabbitmq.com/install-windows.html
##### 2. MAC : https://www.rabbitmq.com/install-homebrew.html
##### 3. Debian and Ubuntu : https://www.rabbitmq.com/install-debian.html
##### 4. RPM based Linux : https://www.rabbitmq.com/install-rpm.html
##### 5. EC2 : https://www.rabbitmq.com/ec2.html

### Use http://localhost:15672/#/ to login to RabbitMQ server using username as "guest" and password as "guest"

### Install Python3.10 and create virtual environment

### Install pika library of python using below command:
        pip3.10 install pika

### How to run app:
    1. run consumer.py in one terminal, it will wait for message to be present in queue named 'hello'
    2. run producer.py in other terminal, it will produce message into queue 'hello'


