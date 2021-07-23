## Main executable python file
    # Connects Python IDE to RB UI through socket communication via LAN (PC = server, RB tablet = client)

from socketCommunication import *
from globalvariables import *
from tkinter import *

establishCommunication()

#to do: UI buttons w/ tkinter
