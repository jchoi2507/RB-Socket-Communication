## Socket communication & establishment module

import socket
import globalvariables as g
import sys
import time
import threading

#Creating a socket communication
def createSocket():
    print (50 * "-")
    print(f"Socket successfully created. Server IP: {g.server}")
    g.s.bind((g.server, g.port))

#Function send an encoded string message to the RB UI (server -> client)
def sendMessage(conn, message):
    encodedMessage = message.encode()
    conn.send(encodedMessage)

#Function that connects server and client
def handleClient(conn, addr):
    print(f"New connection at: {addr}")
    connected = True

    while connected:
        movement = input("Enter movement (move/shake/return): \n")
        basketNum = input("Enter basket number: \n")
        g.message = movement + basketNum

        sendMessage(conn, g.message) #Sending the encoded message to client

        print("Command executing: " + movement + " basket " + basketNum)
        print(50 * "-")

#Actually running the program, with a thread that constantly sends string messages to the RB UI
def establishCommunication():
    createSocket()
    g.s.listen()
    print("Server is listening...")

    while True:
        conn, addr = g.s.accept()
        thread = threading.Thread(target=handleClient,args=(conn, addr))
        thread.start()
        print(f"Active connections: {threading.activeCount() - 1}")
        print(50 * "-")
