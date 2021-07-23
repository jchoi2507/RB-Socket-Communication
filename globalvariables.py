import socket

        ## Initialization ##

HEADER = 64
FORMAT = 'utf-8'
host = ''
port = 5678
server = socket.gethostbyname(socket.gethostname())

commandsArr = ["move1", "move2", "move3", "move4", "shake1", "shake2", "shake3", "shake4",
               "return1", "return2", "return3", "return4"]
