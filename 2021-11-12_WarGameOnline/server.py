#server script should be running before clients can connect

import socket
from _thread import *
from player import Player
import pickle

server = '192.168.2.87' #get your ip address with ipconfig in command prompt
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket:
try:
    s.bind((server, port))
except socket.error as e:
    str(e)


s.listen(2) #clients the server's gonna be listen if there is someone on that port (maximum of 2 in this case)
print('Waiting for a connection, Server Started')

players = [Player(0, 0, 50, 50,(255, 0, 0)), Player(0, 0, 50, 50,(0, 0, 255))]

#thread is another process that runs in the background
def threaded_client(conn, player): #player stands for current player
    # to be sure that we did connect
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048)) #this number represent the amount of bits its trying to receive. if error increase this number by multiplying. The larger this number, the longer it takes to receive.
            players[player] = data

            if not data:
                print('Disconnected')
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print('Received: ', data)
                print('Sending :', reply)
            
            # encodes our string into a bytes object
            conn.sendall(pickle.dumps(reply))
        except:
            break
    
    print('Lost connection')
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept() #accepts any incoming connections and stores the connection(object) and the address (IP)
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1