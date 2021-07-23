import socket
import sys
import time
import threading

HEADER = 64
FORMAT = 'utf-8'
host = ''
port = 5678
server = socket.gethostbyname(socket.gethostname())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created. Server IP: ", server)

s.bind((server, port))

def sendMessage(conn, addr, msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    conn.send(send_length)
    conn.send(message)

def handleClient(conn, addr):
    print("New connection at: ", addr)

    connected = True
    while connected:

        ##For receiving and printing messages:

        #msg = conn.recv(HEADER).decode(FORMAT)
        #print(msg)

        ##For sending messages to the RB UI:

        msg = input("Enter desired basket movement.")
        sendMessage(conn, addr, msg)

def start():
    s.listen()
    print("Server is listening...")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handleClient,args=(conn, addr))
        thread.start()
        print(f"Active connections: {threading.activeCount() - 1}")

start()

