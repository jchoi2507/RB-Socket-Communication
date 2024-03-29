import pika
import sys
import os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="hostIP"))
    channel = connection.channel()

    channel.queue_declare(queue="hello")

    def callback(channel, method, properties, body):
        print("Received %r" % body)
        print(50 * "*")

    channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)
    print("Waiting for messages...")
    channel.start_consuming()

if (__name__ == "__main__"):
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
