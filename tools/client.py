#!/usr/bin/python           # This is client.py file
import sys
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = sys.argv[1]          #'173.16.1.200'  # Get local machine name
port = int(sys.argv[2])     #12345                # Reserve a port for your service.
st = sys.argv[3]            #'client  testing'

s.connect((host, port))
byt=st.encode()
s.send(byt)

print (s.recv(1024).decode())
s.close()                     # Close the socket when done

#e.g. python client.py 173.16.1.200 12345 'testing from yockgen client'
