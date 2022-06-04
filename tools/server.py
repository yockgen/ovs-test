#!/usr/bin/python           # This is server.py file
import sys
import socket               # Import socket module

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         # Create a socket object
host = sys.argv[1]          #'173.16.1.200'       #socket.gethostname() # Get local machine name
port = int(sys.argv[2])          #12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
print ("host ",host)
print ("port ", port)

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from ', addr)
   talkerMsg  = c.recv(1024).decode()
   print('receiving:' ,talkerMsg )

   strMsg = 'server response:' +  talkerMsg
   c.send(strMsg.encode())
   c.close()                # Close the connection

#e.g. python server.py 173.16.1.200 12345
