import socket
import sys
import cmddb
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('0.0.0.0', 5566)
sock.bind(server_address)
sock.listen(1)
BUFFERSIZE=128

while True:
    connection, client_address = sock.accept()
    try:
        while True:
            data = connection.recv(BUFFERSIZE)
            cmddb.power(data)
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()
