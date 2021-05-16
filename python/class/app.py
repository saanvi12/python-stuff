import socket
import sys

# SERVER = socket.gethostbyname(socket.gethostname())
SERVER = '45.251.233.69'
PORT = 5050
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


# send("Hello World")
# input()
# send("Check Check")
# input()
# send("Yooooo")
# send(DISCONNECT_MESSAGE)
try:
	while  True:
		send(input("Entter You Message"))
except keyboardInterrupt as err:
	send(DISCONNECT_MESSAGE)
	sys.exit()