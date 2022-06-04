#!/usr/bin/python           # This is server.py file
import sys
import socket               # Import socket module

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)         # Create a socket object
host = sys.argv[1]          #'173.16.1.200'       #socket.gethostname() # Get local machine name
port = int(sys.argv[2])          #12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
print ("host ",host)
print ("port ", port)


while True:
    bytesAddressPair = s.recvfrom(1024)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)

    print("Receiving:",clientMsg)
    print("IP:",clientIP)


    # Sending a reply to client
    s.sendto(message, address)


#e.g. python3 server-udp.py 173.16.1.200 12345

