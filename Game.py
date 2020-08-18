from player import player
import numpy as np
from methods import (
                     bingo_matrix_man,
                     check_bingo
                     )


class games:
    def __init__(self, id, maximum):
        self.game_id = id
        self.max = maximum
        self.players = []
        self.ready = False
        self.GAME_PLAYERS = {}
        self.victory_list = []
        self.went = {}
        self.alternate = np.asarray(range(self.game_id*self.max,(self.game_id+1)*self.max))
        self.index = 0
        self.client_side_entry = {}

    def add_player(self, p_id):

        self.players.append(p_id)
        self.GAME_PLAYERS[p_id] = player()
        self.client_side_entry[p_id] = False
        self.went[p_id] = False

    def client_side_entry_detail(self,p_id,machine):
        if machine == "1":
            # play with machine
            self.GAME_PLAYERS[p_id].machine_player = True
            self.client_side_entry[p_id] = True
        elif machine == "0":
            # play with other humans
            self.client_side_entry[p_id] = True
            
    def reset(self):

        # delete player profiles
        for key in self.GAME_PLAYERS:
            del self.GAME_PLAYERS[key]

        # delete players list
        del self.players[:]

    def connected(self):
        return self.ready

    def reset_went(self):

        for key in self.went:
            self.went[key] = False
        
        temp = self.alternate[self.index]
        for key in self.went:
            if key != (temp+1):
                self.went[key] = True

        self.index = self.index + 1
        if self.index == self.max:
            self.index = 0

        # if self.alternate:
        #     self.went[2] = True
        #     self.alternate = False
        # else:
        #     self.went[1] = True
        #     self.alternate = True

    def everyone_went(self):
        flag = 0
        for key in self.went:
            if self.went[key]:
                flag = 1
            else:
                flag = 0
                break
        if flag == 1:
            self.reset_went()
