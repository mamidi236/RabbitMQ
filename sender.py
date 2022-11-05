#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')) # server ip to be given
channel = connection.channel()

channel.queue_declare(queue='rabbitMQ') # messaging queue name

for i in range(1,50):
    channel.basic_publish(exchange='', routing_key='rabbitMQ', body='Hi this is '+str(i) + ' Message')  # publish message event




print(" Sender execution completed")
connection.close()