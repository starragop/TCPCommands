import socket
import sys

IP = '192.168.88.24'
PORT = 5566
BUFFERSIZE = 1024
command=sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(command)
data = s.recv(BUFFERSIZE)
s.close()

print "Command sent: ", data
