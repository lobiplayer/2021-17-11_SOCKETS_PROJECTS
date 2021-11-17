import socket
import threading
import pickle

HEADER = 64 #bytes #the size of the message that is coming in
PORT = 5050
# SERVER = '192.168.2.87'
SERVER = socket.gethostbyname(socket.gethostname()) #does the same as hardcoded
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

chat = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #created a socket #over the internet, method is sock stream

server.bind(ADDR) #ip + port is binded to the socket

def handle_client(conn, addr): #this is going to run for EACH client individually
    print(f'[NEW CONNECTION] {addr} connected.')

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) #wait until something is sent over the socket
        if msg_length: #ckecks if there is something in the message

            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False #stop the loop
        
            print(f'[{addr}] {msg}')
            chat.append(f'[{addr}] {msg}')

        conn.sendall(pickle.dumps(chat))
    
    conn.close() # close the connection with this client

def start(): #handles new connections
    server.listen()
    print(f'[LISTENING] Server is listening on {SERVER}')
    while True:  # loop that continiously listens
        conn, addr = server.accept()  # wait on sthis line for a new connection to the server
        #when a new client connects:
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.active_count() - 6}') #tells us the amount of threads


print('[STARTING] server is starting...')
start()