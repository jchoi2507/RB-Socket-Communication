## Module for initialization and global variables

import socket

        ## Initialization ##

HEADER = 64
FORMAT = 'utf-8'
host = ''
port = 5678
server = socket.gethostbyname(socket.gethostname())
message = " "
basketNum = " "
action = " "

commandsArr = ["move1", "move2", "move3", "move4", "shake1", "shake2", "shake3", "shake4",
               "return1", "return2", "return3", "return4"]

        ## Socket initialization ##

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
