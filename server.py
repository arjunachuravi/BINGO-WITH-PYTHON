import socket
from _thread import start_new_thread
from Game import games
import pickle
from methods import check_bingo,modify_grid

def Convert(string): 
    li = list(string.split(" ")) 
    return li 

class server:
    def __init__(self, num):
        self.SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.43.180"
        self.port = 5555
        self.count = 0
        self.max = num
        self.game = {}

    def initiate(self):
        self.server_role_play()
        self.looper()

    def server_role_play(self):
        try:
            self.SOCKET.bind((self.server, self.port))
            self.SOCKET.listen()
            print("waiting for players . . .")
        except socket.error as e:
            print(e)

    def looper(self):

        game_id = 0

        while True:
            conn, addr = self.SOCKET.accept()
            print("connected to", addr)
            self.count = self.count + 1
            game_id = (self.count - 1) // self.max
            if game_id not in self.game:
                self.game[game_id] = games(game_id,self.max)
            if self.count % self.max == 0:
                self.game[game_id].add_player(self.count)
                self.game[game_id].ready = True
                self.game[game_id].reset_went()
            else:
                self.game[game_id].add_player(self.count)
                self.game[game_id].ready = False
            ###################################################
            start_new_thread(self.client_process, (conn, self.count, game_id))

    def client_process(self, conn, p_id, game_id):
        count = 0
        conn.send(str.encode(str(p_id)))  # hello-token
        print("game id == ", game_id)
        reply = ""
        while True:
            try:
                data = conn.recv(4096).decode()
                if game_id in self.game:
                    if not data:
                        print("disconnected")
                        break
                    else:
                        if data == "reset":
                            self.game[game_id].reset()
                            count = 0

                        elif data == "check":
                            check_bingo(self.game[game_id].victory_list,self.game[game_id].GAME_PLAYERS)
                            #if player is a winner remove his identity and exit user thread
                            print("debug -->vlist-->",self.game[game_id].victory_list)

                        
                        elif (("0" in Convert(data)) or ("1" in Convert(data))) and count == 0 :
                            self.game[game_id].client_side_entry_detail(p_id,Convert(data)[0])
                            count = 1

                        elif data != "get":
                            data = int(data)
                            modify_grid(self.game[game_id].GAME_PLAYERS,data)
                            self.game[game_id].went[p_id] = True
                            self.game[game_id].everyone_went()

                        reply = self.game[game_id]
                        conn.sendall(pickle.dumps(reply))
            except:
                break

        print("lost connection with person", p_id)
        try:
            del self.game[game_id]
            print("closing game..", game_id)
        except:
            pass
        self.count = self.count - 1
        conn.close()


m = server(2)

m.initiate()
