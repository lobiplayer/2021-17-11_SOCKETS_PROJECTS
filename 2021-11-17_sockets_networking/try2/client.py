import socket
import pickle

HEADER = 64  # bytes #the size of the message that is coming in
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = '192.168.2.87'
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #set up socket
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    reply = pickle.loads(client.recv(2048*2))  # prints the response
    print(type(reply))
    for message in reply:
        print(message)

while True:
    send(input('...'))

while True:
    reply = pickle.loads(client.recv(2048*2))