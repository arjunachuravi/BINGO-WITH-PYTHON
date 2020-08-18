import numpy as np
import random

class player:
    def __init__(self):
        self.r = [] # avoid redundant row check
        self.c = [] # avoid redundant column check
        self.d = [] # avoid redundant diagonal check
        self.machine_player = False # player is machine or not
        self.player_array = np.asarray(random.sample(range(1,26),25)) # bingo matrix 1-D array
        self.player_passbook = 0 # B-I-N-G-O counter
        self.alternator = True

    # bingo matrix 2-D array
    def player_matrix(self):
            return self.player_array.reshape(5,5)

    # load iter val of row to avoid redundant looping and bingo count
    def load_row(self,rx):
        self.r.append(rx)
    def load_col(self,cx):
        self.c.append(cx)
    def load_dgl(self,dx):
        self.d.append(dx)

    # check for iter val of row to avoid redundant looping and bingo count
    def check_row(self,rx):
        if rx in self.r:
            return True
        else:
            return False
    def check_col(self,cx):
        if cx in self.c:
            return True
        else:
            return False
    def check_dgl(self,dx):
        if dx in self.d:
            return True
        else:
            return False

    # machine logic

    def computerlogic(self):
        blk_rx = []
        blk_cx = []
        prior = -1
        choose_r = True
        choose_c = False

        results = [ np.count_nonzero(self.player_matrix() == 0,axis=1), np.count_nonzero(self.player_matrix() == 0,axis=0) ]
        
        for i in range(5):
            if results[0][i] == 5:
                results[0][i] = -1
            if results[1][i] == 5:
                results[1][i] = -1  
                
        if max(results[0]) == max(results[1]):
            if self.alternator == True:
                prior = np.argmax(results[1])
                choose_r = True
                choose_c = False
                self.alternator = False
            else:
                prior = np.argmax(results[1])
                choose_r = False
                choose_c = True
                self.alternator = True
        elif max(results[0]) > max(results[1]):
            prior = np.argmax(results[0])
            choose_r = True
            choose_c = False
            self.alternator = False
        else:
            prior = np.argmax(results[1])
            choose_r = False
            choose_c = True
            self.alternator = True


        for i in range(5):
            if prior >= 0 and prior not in blk_rx:
                i  = prior
            if i not in blk_rx and choose_r:
                if self.player_matrix()[i][0] == 0 or self.player_matrix()[i][1] == 0 or self.player_matrix()[i][2] == 0 or self.player_matrix()[i][3] == 0 or self.player_matrix()[i][4] == 0:
                    if self.player_matrix()[i][0] == 0 and self.player_matrix()[i][1] == 0 and self.player_matrix()[i][2] == 0 and self.player_matrix()[i][3] == 0 and self.player_matrix()[i][4] == 0:
                        blk_rx.append(i)
                    elif self.player_matrix()[i][0] == 0 and self.player_matrix()[i][1] == 0 and self.player_matrix()[i][2] == 0 and self.player_matrix()[i][3] == 0:
                        blk_rx.append(i)
                        return self.player_matrix()[i][4]
                    elif self.player_matrix()[i][0] == 0 and self.player_matrix()[i][1] == 0 and self.player_matrix()[i][2] == 0 and self.player_matrix()[i][4] == 0:
                        blk_rx.append(i)
                        return self.player_matrix()[i][3]
                    elif self.player_matrix()[i][0] == 0 and self.player_matrix()[i][1] == 0 and self.player_matrix()[i][3] == 0 and self.player_matrix()[i][4] == 0:
                        blk_rx.append(i)
                        return self.player_matrix()[i][2]
                    elif self.player_matrix()[i][0] == 0 and self.player_matrix()[i][2] == 0 and self.player_matrix()[i][3] == 0 and self.player_matrix()[i][4] == 0:
                        blk_rx.append(i)
                        return self.player_matrix()[i][1]
                    elif self.player_matrix()[i][1] == 0 and self.player_matrix()[i][2] == 0 and self.player_matrix()[i][3] == 0 and self.player_matrix()[i][4] == 0:
                        blk_rx.append(i)
                        return self.player_matrix()[i][0]
                    elif self.player_matrix()[i][0] == 0 and self.player_matrix()[i][1] == 0 and self.player_matrix()[i][2] == 0:
                        return self.player_matrix()[i][4]
                    elif self.player_matrix()[i][0] == 0 and self.player_matrix()[i][1] == 0 and self.player_matrix()[i][3] == 0:
                        return self.player_matrix()[i][3]
                    elif self.player_matrix()[i][0] == 0 and self.player_matrix()[i][1] == 0 and self.player_matrix()[i][4] == 0:
                        return self.player_matrix()[i][2]
                    elif self.player_matrix()[i][0] == 0 and self.player_matrix()[i][2] == 0 and self.player_matrix()[i][3] == 0:
                        return self.player_matrix()[i][4]
                    elif self.player_matrix()[i][0] == 0 and self.player_matrix()[i][2] == 0 and self.player_matrix()[i][4] == 0:
                        return self.player_matrix()[i][3]
                    elif self.player_matrix()[i][0] == 0 and self.player_matrix()[i][3] == 0 and self.player_matrix()[i][4] == 0:
                        return self.player_matrix()[i][1]
                    elif self.player_matrix()[i][1] == 0 and self.player_matrix()[i][2] == 0 and self.player_matrix()[i][3] == 0:
                        return self.player_matrix()[i][4]
                    elif self.player_matrix()[i][1] == 0 and self.player_matrix()[i][2] == 0 and self.player_matrix()[i][4] == 0:
                        return self.player_matrix()[i][0]
                    elif self.player_matrix()[i][1] == 0 and self.player_matrix()[i][3] == 0 and self.player_matrix()[i][4] == 0:
                        return self.player_matrix()[i][0]
                    elif self.player_matrix()[i][2] == 0 and self.player_matrix()[i][3] == 0 and self.player_matrix()[i][4] == 0:
                        return self.player_matrix()[i][0]
                    elif self.player_matrix()[i][0] == 0 and self.player_matrix()[i][1] == 0:
                        return self.player_matrix()[i][3]
                    elif self.player_matrix()[i][0] == 0 and self.player_matrix()[i][2] == 0:
                        return self.player_matrix()[i][3]
                    elif self.player_matrix()[i][0] == 0 and self.player_matrix()[i][3] == 0:
                        return self.player_matrix()[i][4]
                    elif self.player_matrix()[i][0] == 0 and self.player_matrix()[i][4] == 0:
                        return self.player_matrix()[i][2]
                    elif self.player_matrix()[i][1] == 0 and self.player_matrix()[i][2] == 0:
                        return self.player_matrix()[i][3]
                    elif self.player_matrix()[i][1] == 0 and self.player_matrix()[i][3] == 0:
                        return self.player_matrix()[i][4]
                    elif self.player_matrix()[i][1] == 0 and self.player_matrix()[i][4] == 0:
                        return self.player_matrix()[i][0]
                    elif self.player_matrix()[i][2] == 0 and self.player_matrix()[i][3] == 0:
                        return self.player_matrix()[i][4]
                    elif self.player_matrix()[i][2] == 0 and self.player_matrix()[i][4] == 0:
                        return self.player_matrix()[i][0]
                    elif self.player_matrix()[i][3] == 0 and self.player_matrix()[i][4] == 0:
                        return self.player_matrix()[i][2]
                    elif self.player_matrix()[i][0] == 0:
                        return self.player_matrix()[i][1]
                    elif self.player_matrix()[i][1] == 0:
                        return self.player_matrix()[i][2]
                    elif self.player_matrix()[i][2] == 0:
                        return self.player_matrix()[i][3]
                    elif self.player_matrix()[i][3] == 0:
                        return self.player_matrix()[i][4]
                    elif self.player_matrix()[i][4] == 0:
                        return self.player_matrix()[i][0]
                else:
                    return np.random.choice(self.player_array,1)[0]

                # end row check
        for i in range(5):
            if prior >= 0 and prior not in blk_cx:
                    i  = prior
            if i not in blk_cx and choose_c:
                if self.player_matrix()[0][i] == 0 or self.player_matrix()[1][i] == 0 or self.player_matrix()[2][i] == 0 or self.player_matrix()[3][i] == 0 or self.player_matrix()[4][i] == 0:
                    if self.player_matrix()[0][i] == 0 and self.player_matrix()[1][i] == 0 and self.player_matrix()[2][i] == 0 and self.player_matrix()[3][i] == 0 and self.player_matrix()[4][i] == 0:
                        blk_cx.append(i)
                    elif self.player_matrix()[0][i] == 0 and self.player_matrix()[1][i] == 0 and self.player_matrix()[2][i] == 0 and self.player_matrix()[3][i] == 0:
                        blk_cx.append(i)
                        return self.player_matrix()[4][i]
                    elif self.player_matrix()[0][i] == 0 and self.player_matrix()[1][i] == 0 and self.player_matrix()[2][i] == 0 and self.player_matrix()[4][i] == 0:
                        blk_cx.append(i)
                        return self.player_matrix()[3][i]
                    elif self.player_matrix()[0][i] == 0 and self.player_matrix()[1][i] == 0 and self.player_matrix()[3][i] == 0 and self.player_matrix()[4][i] == 0:
                        blk_cx.append(i)
                        return self.player_matrix()[2][i]
                    elif self.player_matrix()[0][i] == 0 and self.player_matrix()[2][i] == 0 and self.player_matrix()[3][i] == 0 and self.player_matrix()[4][i] == 0:
                        blk_cx.append(i)
                        return self.player_matrix()[1][i]
                    elif self.player_matrix()[1][i] == 0 and self.player_matrix()[2][i] == 0 and self.player_matrix()[3][i] == 0 and self.player_matrix()[4][i] == 0:
                        blk_cx.append(i)
                        return self.player_matrix()[0][i]
                    elif self.player_matrix()[0][i] == 0 and self.player_matrix()[1][i] == 0 and self.player_matrix()[2][i] == 0:
                        return self.player_matrix()[4][i]
                    elif self.player_matrix()[0][i] == 0 and self.player_matrix()[1][i] == 0 and self.player_matrix()[3][i] == 0:
                        return self.player_matrix()[3][i]
                    elif self.player_matrix()[0][i] == 0 and self.player_matrix()[1][i] == 0 and self.player_matrix()[4][i] == 0:
                        return self.player_matrix()[2][i]
                    elif self.player_matrix()[0][i] == 0 and self.player_matrix()[2][i] == 0 and self.player_matrix()[3][i] == 0:
                        return self.player_matrix()[4][i]
                    elif self.player_matrix()[0][i] == 0 and self.player_matrix()[2][i] == 0 and self.player_matrix()[4][i] == 0:
                        return self.player_matrix()[3][i]
                    elif self.player_matrix()[0][i] == 0 and self.player_matrix()[3][i] == 0 and self.player_matrix()[4][i] == 0:
                        return self.player_matrix()[1][i]
                    elif self.player_matrix()[1][i] == 0 and self.player_matrix()[2][i] == 0 and self.player_matrix()[3][i] == 0:
                        return self.player_matrix()[4][i]
                    elif self.player_matrix()[1][i] == 0 and self.player_matrix()[2][i] == 0 and self.player_matrix()[4][i] == 0:
                        return self.player_matrix()[3][i]
                    elif self.player_matrix()[2][i] == 0 and self.player_matrix()[3][i] == 0 and self.player_matrix()[4][i] == 0:
                        return self.player_matrix()[0][i]
                    elif self.player_matrix()[0][i] == 0 and self.player_matrix()[1][i] == 0:
                        return self.player_matrix()[3][i]
                    elif self.player_matrix()[0][i] == 0 and self.player_matrix()[2][i] == 0:
                        return self.player_matrix()[3][i]
                    elif self.player_matrix()[0][i] == 0 and self.player_matrix()[3][i] == 0:
                        return self.player_matrix()[4][i]
                    elif self.player_matrix()[0][i] == 0 and self.player_matrix()[4][i] == 0:
                        return self.player_matrix()[2][i]
                    elif self.player_matrix()[1][i] == 0 and self.player_matrix()[2][i] == 0:
                        return self.player_matrix()[3][i]
                    elif self.player_matrix()[1][i] == 0 and self.player_matrix()[3][i] == 0:
                        return self.player_matrix()[4][i]
                    elif self.player_matrix()[1][i] == 0 and self.player_matrix()[4][i] == 0:
                        return self.player_matrix()[0][i]
                    elif self.player_matrix()[2][i] == 0 and self.player_matrix()[3][i] == 0:
                        return self.player_matrix()[4][i]
                    elif self.player_matrix()[2][i] == 0 and self.player_matrix()[4][i] == 0:
                        return self.player_matrix()[0][i]
                    elif self.player_matrix()[3][i] == 0 and self.player_matrix()[4][i] == 0:
                        return self.player_matrix()[2][i]
                    elif self.player_matrix()[0][i] == 0:
                        return self.player_matrix()[1][i]
                    elif self.player_matrix()[1][i] == 0:
                        return self.player_matrix()[2][i]
                    elif self.player_matrix()[2][i] == 0:
                        return self.player_matrix()[3][i]
                    elif self.player_matrix()[3][i] == 0:
                        return self.player_matrix()[4][i]
                    elif self.player_matrix()[4][i] == 0:
                        return self.player_matrix()[0][i]
                else:
                    return np.random.choice(self.player_array,1)[0]
                # end col check