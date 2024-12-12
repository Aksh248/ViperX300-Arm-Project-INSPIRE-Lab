# Import socket module 
import socket			 

# Create a socket object 
s = socket.socket()		 

# Define the port on which you want to connect 
port = 1234			
while True:
    # connect to the server on local computer 
    s.connect(('172.24.16.118', port)) 
    # receive data from the server and decoding to get the string.
    print (s.recv(1024))
    # close the connection
    if KeyboardInterrupt:
        break 
s.close()	 
