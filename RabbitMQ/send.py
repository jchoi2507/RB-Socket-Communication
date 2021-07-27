import pika
import sys

#Establishing connection
connection = pika.BlockingConnection(pika.ConnectionParameters("127.0.0.1")) #Change localhost to different name or IP
channel = connection.channel()                                               #to connect to different machines

#Obtaining desired message to send
def obtainMessage():
    k = input("Enter the message you would like to send.\n")
    return k

channel.queue_declare(queue="hello")

while True:
    message = obtainMessage()
    if (message == "quit"):
        sys.exit(0)
    channel.basic_publish(exchange='', routing_key="hello", body=message)
    print("Sent the following message: ", message)
    print(50 * "*")

connection.close()
