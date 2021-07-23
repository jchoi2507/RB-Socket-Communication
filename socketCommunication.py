import socket
import sys
import time
import threading

HEADER = 64
FORMAT = 'utf-8'
host = ''
port = 5678
server = socket.gethostbyname(socket.gethostname())
print(server)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created.")

s.bind((server, port))

def handleClient(conn, addr):
    print(f"New Connection: {addr} connected.")

    connected = True
    while connected:
        msg = conn.recv(HEADER).decode(FORMAT)
        print(msg)

def start():
    s.listen()
    print("Server is listening...")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handleClient,args=(conn, addr))
        thread.start()
        print(f"Active connections: {threading.activeCount() - 1}")


start()
