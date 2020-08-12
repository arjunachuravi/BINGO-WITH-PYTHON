# bingo.py

# packages
import numpy as np
from tabulate import tabulate as tb
import os
from time import sleep
import random

class player:
    
    def __init__(self):
        self.r = [] # avoid redundant row check 
        self.c = [] # avoid redundant column check 
        self.d = [] # avoid redundant diagonal check 
        self.machine_player = False # player is machine or not
        self.player_array = np.asarray(random.sample(range(1,26),25)) # bingo matrix 1-D array
        self.player_passbook = 0 # B-I-N-G-O counter
        self.player_name = "" # player name
        self.player_matrix_type = "a"  # matrix fill type (a/m)
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

    # ckeck for iter val of row to avoid redundanct looping and bingo count
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
    
    # chance taker
    def take_chance(self,NUM_PLAYERS,GAME_PLAYERS):
        choice = 0
        if self.machine_player == False:
            choice = input("[INPUT] Enter the number (1-25):")
        else:
            choice = str(self.computerlogic())
            print("[debug] mac-input-->",choice)
        if choice.isnumeric() and int(choice)<26 and int(choice)>0:
            choice = int(choice)
            
            if modify_grid(NUM_PLAYERS,GAME_PLAYERS,choice):
                return
            else:
                if self.machine_player == False:
                    print("[GAME] already taken")
                self.take_chance(NUM_PLAYERS,GAME_PLAYERS)
        else:
            print("[ERR] invalid entry")
            sleep(2)
            self.take_chance(NUM_PLAYERS,GAME_PLAYERS)

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
#function to clear screen
def clear(): 
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 

#function to exit program
def exit_prgm():
    clear()
    print("\n[INFO] Exiting")
    sleep(4)
    os._exit(os.X_OK)

#display the grid 
def grid_show(ARR):
    print(tb(ARR,tablefmt="fancy_grid"))

#if playing h-vs-h then this fn is invoked to init player objects
def get_num_players(GAME_PLAYERS):
    numplayer = input("[INPUT] number of players: ")
    if numplayer.isnumeric() and int(numplayer) < 5 and int(numplayer) >= 2: # max players are set to be 5 [can be changed]
        numplayer = int(numplayer)
        for i in range(numplayer):
            GAME_PLAYERS[i] = player()
            GAME_PLAYERS[i].player_name = input("[INPUT] Enter the name of player:")
        return numplayer
    else:
        print("[ERR] invalid,need to be numeric or below 5")
        get_num_players(GAME_PLAYERS)
    return numplayer # returns a value so that it can be used locally

# Main-Menu
def mainmenu():
    clear()
    print("thattikutt bingo 1.0 ")
    print("(n)ew game \n(e)xit \n choice: ")
    choice = input()
    if choice.isalpha() and len(choice)==1:
        if choice in ['n','N','e','E']:
            if choice in ['n','N']:
                print("(m)with machine \n(o)r not \n choice: ")
                choice2 = input()
                if choice2.isalpha() and len(choice2)==1:
                    if choice2 in ['m','M','o','O']:
                        if choice2 in ['m','M']:
                            new_game(True) # play with machine
                        else:
                            new_game(False) # play with other humans
                    else:
                        print("[ERR] invalid choice")
                        mainmenu()
                else:
                    print("[ERR] invalid choice")
                    mainmenu()
            else:
                exit_prgm() # exit the game
        else:
            print("[ERR] invalid choice")
            mainmenu()
    else:
        print("[ERR] invalid choice")
        mainmenu()

#manual entry of matrix
def bingo_matrix_man(GAME_PLAYERS,player_id):
    GAME_PLAYERS[player_id].player_array = np.zeros(25)
    print("[INFO] NOTE: NUMBERS WILL BE INITIALIZED BY ROWS")
    for i in range(25):
        clear()
        grid_show(GAME_PLAYERS[player_id].player_matrix())
        sleep(2)
        err = 1
        while(err):
            clear()
            num = input("[INPUT] input :")
            if num.isnumeric() and int(num)<26 and int(num)>0 and int(num) not in GAME_PLAYERS[player_id].player_array:
                num = int(num)
                GAME_PLAYERS[player_id].player_array[i] = num
                err = 0
            else:
                print("[ERR] error @_@ type again : it may be already present ")
                sleep(2)
                err = 1
    print("[INFO] all done")

# 2nd menu
def new_game(mach_bool): # if mach_bool is True ie, play with a machine
    GAME_PLAYERS = {} # dictionary to hold player-class objects
    NUM_PLAYERS = 0
    clear()
    if mach_bool == True:
        NUM_PLAYERS = 2
        for i in range(NUM_PLAYERS):
            GAME_PLAYERS[i] = player()
        GAME_PLAYERS[1].player_name = "MACHINE"
        GAME_PLAYERS[1].machine_player = True # machine plays 2nd , human play 1st
        GAME_PLAYERS[0].player_name = input("Enter The player's name-->")
    else:
        NUM_PLAYERS = get_num_players(GAME_PLAYERS)

    if mach_bool == False: # human vs human 
        #loop
        i = 0
        while(i >= 0 and i < NUM_PLAYERS):
            print("options for player id-->",i,"player name-->",GAME_PLAYERS[i].player_name)
            print("(a)utomatic grid generation \n(m)anual mode \n(e)xit")
            choice = input()
            if choice.isalpha() and len(choice)==1:
                if choice in ['a','A','m','M','e','E']:
                    if choice in ['a','A']:
                        GAME_PLAYERS[i].player_matrix_type = 'a'
                    elif choice in ['m','M']:
                        GAME_PLAYERS[i].player_matrix_type = 'm'
                        # call the class fn to describe the matrix
                        bingo_matrix_man(GAME_PLAYERS,i)
                    else:
                        exit_prgm()
                    i = i + 1
                else:
                    print("[ERR] invalid choice")
            else:
                print("[ERR] invalid choice")
        #--> loop ended
    else:
        #loop
        flag = 0
        while flag==0:
            print("options for player id-->",i,"player name-->",GAME_PLAYERS[0].player_name)
            print("(a)utomatic grid generation \n(m)anual mode \n(e)xit")
            choice = input()
            if choice.isalpha() and len(choice)==1:
                if choice in ['a','A','m','M','e','E']:
                    if choice in ['a','A']:
                        GAME_PLAYERS[0].player_matrix_type = 'a'
                    elif choice in ['m','M']:
                        GAME_PLAYERS[0].player_matrix_type = 'm'
                        # call the class fn to describe the matrix
                        bingo_matrix_man(GAME_PLAYERS,0)
                    else:
                        exit_prgm()
                    flag = 1
                else:
                    print("[ERR] invalid choice")
            else:
                print("[ERR] invalid choice")
        #--> loop ended
    play_game(mach_bool,NUM_PLAYERS,GAME_PLAYERS)

#result-display function
def display_results(VICTORY_LIST,GAME_PLAYERS):
    header = ["Winner1","winner2","winner3","winner4","winner5"]
    m_o_h = []
    for i in VICTORY_LIST:
        m_o_h.append(GAME_PLAYERS[i].player_name)
    m_o_h = [m_o_h]
    print(tb(m_o_h, header, tablefmt="grid"))

# modify grid values
def modify_grid(NUM_PLAYERS,GAME_PLAYERS,number):
    flag = True
    for iter in range(NUM_PLAYERS):
        #find the index of number
        result = np.where(GAME_PLAYERS[iter].player_array == number)
        if len(result[0]) == 0:
            flag = False
        else:
            pos = result[0][0]
            GAME_PLAYERS[iter].player_array[pos] = 0
            flag = True
    return flag 

# Logic
def play_game(mach_bool,NUM_PLAYERS,GAME_PLAYERS):
    VICTORY_LIST=[]
    clear()
    print("[INFO] done setting...")
    sleep(2)
    print("[INFO] lets play")
    print("[INFO] !!! the queue will be in the order of player id !!!")
    sleep(2)
    while(len(VICTORY_LIST) <= NUM_PLAYERS - 1):
        i = 0
        while(i < NUM_PLAYERS and len(VICTORY_LIST) <= NUM_PLAYERS - 1):  
            if i not in VICTORY_LIST:
                clear()
                print("[INFO]","Player-->",GAME_PLAYERS[i].player_name," PLAYER ID-->",i," chance-->")
                GAME_PLAYERS[i].take_chance(NUM_PLAYERS,GAME_PLAYERS)
                grid_show(GAME_PLAYERS[i].player_matrix())
                check_bingo(VICTORY_LIST,NUM_PLAYERS,GAME_PLAYERS) #--> checks if player won
                if len(VICTORY_LIST) == NUM_PLAYERS - 1:
                    display_results(VICTORY_LIST,GAME_PLAYERS)
                    sleep(8)
                    mainmenu()
                sleep(5)
            i = i + 1     
    sleep(5)
    mainmenu() # jumps to main-menu fun [recursive]

def check_bingo(VICTORY_LIST,NUM_PLAYERS,GAME_PLAYERS):
    for player_id in range(NUM_PLAYERS):
        for i in range(5):
            if GAME_PLAYERS[player_id].player_array[i+0] == GAME_PLAYERS[player_id].player_array[i+5] == GAME_PLAYERS[player_id].player_array[i+10] == GAME_PLAYERS[player_id].player_array[i+15] == GAME_PLAYERS[player_id].player_array[i+20]:
                if GAME_PLAYERS[player_id].check_col(i) == False:
                    GAME_PLAYERS[player_id].load_col(i)
                    GAME_PLAYERS[player_id].player_passbook = GAME_PLAYERS[player_id].player_passbook + 1
                    if GAME_PLAYERS[player_id].player_passbook == 5:
                        VICTORY_LIST.append(player_id)

        for i in range(0,21,5):
            if GAME_PLAYERS[player_id].player_array[i+0] == GAME_PLAYERS[player_id].player_array[i+1] == GAME_PLAYERS[player_id].player_array[i+2] == GAME_PLAYERS[player_id].player_array[i+3] == GAME_PLAYERS[player_id].player_array[i+4]:
                if GAME_PLAYERS[player_id].check_row(i) == False:
                    GAME_PLAYERS[player_id].load_row(i)
                    GAME_PLAYERS[player_id].player_passbook = GAME_PLAYERS[player_id].player_passbook + 1
                    if GAME_PLAYERS[player_id].player_passbook == 5:
                        VICTORY_LIST.append(player_id)

        if GAME_PLAYERS[player_id].check_dgl(0) == False:
            if GAME_PLAYERS[player_id].player_array[0] == GAME_PLAYERS[player_id].player_array[6] == GAME_PLAYERS[player_id].player_array[12] == GAME_PLAYERS[player_id].player_array[18] == GAME_PLAYERS[player_id].player_array[24]:
                    GAME_PLAYERS[player_id].load_dgl(0)
                    GAME_PLAYERS[player_id].player_passbook = GAME_PLAYERS[player_id].player_passbook + 1
                    if GAME_PLAYERS[player_id].player_passbook == 5:
                        VICTORY_LIST.append(player_id)

        if GAME_PLAYERS[player_id].check_dgl(4) == False:
            if GAME_PLAYERS[player_id].player_array[4] == GAME_PLAYERS[player_id].player_array[8] == GAME_PLAYERS[player_id].player_array[12] == GAME_PLAYERS[player_id].player_array[16] == GAME_PLAYERS[player_id].player_array[20]:
                    GAME_PLAYERS[player_id].load_dgl(4)
                    GAME_PLAYERS[player_id].player_passbook = GAME_PLAYERS[player_id].player_passbook + 1
                    if GAME_PLAYERS[player_id].player_passbook == 5:
                        VICTORY_LIST.append(player_id)
        
if __name__ == "__main__":
    mainmenu()
