# RabbitMQ
A simple rabbit message queue python project which shows the publish and subscription of a topic and connection to the server.
# Prerequisite
Install Rabbit MQ server and start the server
https://www.rabbitmq.com/download.html.

# Run 
Start the receiver using the below command before starting the sender.  
```python Receiver.py```  
Start the sender  
```python sender.py```  

#Output  
```python Receive.py
 [*] Waiting for messages. To exit press CTRL+C
 [x] Received b'Hi this is 1Message'
 [x] Received b'Hi this is 2Message'
 [x] Received b'Hi this is 3Message'
 [x] Received b'Hi this is 4Message'
 [x] Received b'Hi this is 5Message'
 [x] Received b'Hi this is 6Message'
 ......    
 
