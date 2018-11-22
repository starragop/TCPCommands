import socket
import sys
import cmds

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', 5566)
sock.bind(server_address)
sock.listen(1)
BUFFERSIZE=128

while True:
    connection, client_address = sock.accept()
    try:
        while True:
            data = connection.recv(BUFFERSIZE)
            function=getattr(cmds,data)
            function(arg1)
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()
