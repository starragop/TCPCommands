import socket

IP = '192.168.88.24'
PORT = 5566
BUFFERSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print('~~CONNECTED~~')
while True:
    userinput = input('->')
    if userinput != '':
        s.send(userinput)
        data = s.recv(BUFFERSIZE)
        if data == True:
            print(data)
        else:
            break
s.close()
print('~~CONNECTION CLOSED~~')
