#server script should be running before clients can connect

import socket
from _thread import *
import pickle
from game import Game

server = '192.168.2.87'  # get your ip address with ipconfig in command prompt
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket:
try:
    s.bind((server, port))
except socket.error as e:
    str(e)


s.listen()  # clients the server's gonna be listen if there is someone on that port (maximum of 2 in this case)
print('Waiting for a connection, Server Started')

connected = set()
games = {}
idCount = 0

def threaded_client(conn, p, gameId): #is set up for every client
    global idCount
    conn.send(str.encode(str(p)))

    reply = ''
    while True:
        try: #want to make sure that the server keeps running in case of an error.
            data = conn.recv(4096).decode()

            if gameId in games:
                game = games[gameId] #checks id the game still exists. If player disconnects, game will be removed.

                if not data:
                    break
                else:
                    if data == 'reset':
                        game.reset()

                    elif data != 'get':
                        game.play(p, data)
                    
                    reply = game
                    conn.sendall(pickle.dumps(reply)) #package up the game in a sendable form and send it to clients.
            else:
                break
        except:
            break
    print('Lost connection')

    try:
        del games[gameId]
        print('Closing Game', gameId)

    except:
        pass

    idCount -= 1
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2 #every two players connected, gameId is increased by one.
    if idCount % 2 == 1:
        games[gameId] = Game(id)
        print('Creating a new game...')
    else:
        games[gameId].ready == True
        p = 1


    start_new_thread(threaded_client, (conn, p, gameId))
