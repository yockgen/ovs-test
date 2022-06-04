#!/usr/bin/python           # This is client.py file
import sys
import socket               # Import socket module

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM )         # Create a socket object
host = sys.argv[1]          #'173.16.1.200'  # Get local machine name
port = int(sys.argv[2])     #12345                # Reserve a port for your service.
st = sys.argv[3]            #'client  testing'

addr=(host, port)
byt=st.encode()
s.sendto(byt,addr)

print (s.recvfrom(1024))


#e.g. python client-udp.py 173.16.1.200 12345 'testing from yockgen client'
