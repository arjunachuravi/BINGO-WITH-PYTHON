# bingo.py

# packages
import numpy as np
from tabulate import tabulate as tb
import os
from time import sleep
import random

class player:
    def __init__(self,r,c,d):
        self.r = []
        self.c = []
        self.d = []
    def load_row(self,rx):
        self.r.append(rx)
    def load_col(self,cx):
        self.c.append(cx)
    def load_dgl(self,dx):
        self.d.append(dx)
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

# main function 
def mainmenu():
    clear()
    print("thattikutt bingo 1.0 ")
    print("(n)ew game \n(e)xit \n choice: ")
    choice = input()
    if choice.isalpha() and len(choice)==1:
        if choice in ['n','N','e','E']:
            if choice in ['n','N']:
                new_game() 
            else:
                exit_prgm()
        else:
            print("[ERR] invalid choice")
            mainmenu()
    else:
        print("[ERR] invalid choice")
        mainmenu()

#num players
def get_num_players(PLAYER_NAME_DICT):
    numplayer = input("[INPUT] number of players: ")
    if numplayer.isnumeric() and int(numplayer) < 5 and int(numplayer) >= 2:
        numplayer = int(numplayer)
        for i in range(numplayer):
            PLAYER_NAME_DICT[i] = input("[INPUT] Enter the name of player:")
        return numplayer
    else:
        print("[ERR] invalid,need to be numeric or below 5")
        get_num_players(PLAYER_NAME_DICT)
    return numplayer

#create bingo matrix manual mode
def bingo_matrix_man(STORE_DICT,player_id):
    temp = np.zeros(25)
    print("[INFO] NOTE: NUMBERS WILL BE INITIALIZED BY ROWS")
    for i in range(25):
        clear()
        grid_show(temp.reshape(5,5))
        sleep(2)
        err = 1
        while(err):
            clear()
            num = input("[INPUT] input :")
            if num.isnumeric() and int(num)<26 and int(num)>0 and int(num) not in temp:
                num = int(num)
                temp[i] = num
                err = 0
            else:
                print("[ERR] error @_@ type again : it may be already present ")
                sleep(2)
                err = 1
    #--> store the data
    STORE_DICT[player_id] = temp.reshape(5,5)
    print("[INFO] all done")

#display the grid
def grid_show(ARR):
    print(tb(ARR,tablefmt="fancy_grid"))


def new_game():

    clear()

    #init
    STORE_DICT = {}
    PLAYER_PASSBOOK = {}
    PLAYER_NAME_DICT = {}
    PLAYER_DICT = {}
    NUM_PLAYERS = get_num_players(PLAYER_NAME_DICT)
    for i in range(NUM_PLAYERS):
        PLAYER_PASSBOOK[i] = 0
        PLAYER_DICT[i] = player(0,0,0)
    VICTORY_LIST = []

    #loop
    i = 0
    while(i >= 0 and i < NUM_PLAYERS):
        print("options for player id:",i,"player name : ",PLAYER_NAME_DICT[i])
        print("(a)utomatic grid generation \n(m)anual mode \n(e)xit")
        choice = input()
        if choice.isalpha() and len(choice)==1:
            if choice in ['a','A','m','M','e','E']:
                if choice in ['a','A']:
                    ARR_MAIN = random.sample(range(1,26),25) #--> random matx
                    ARR_MAIN = np.asarray(ARR_MAIN)
                    STORE_DICT[i] = ARR_MAIN.reshape(5,5) 
                elif choice in ['m','M']:
                    bingo_matrix_man(STORE_DICT,i)
                else:
                    exit_prgm()
                i = i + 1
            else:
                print("[ERR] invalid choice")
        else:
            print("[ERR] invalid choice")
    #--> loop ended

    print("[INFO] done setting...")
    sleep(2)
    print("[INFO] lets play")
    print("[INFO] !!! the queue will be in the order of player id !!!")
    sleep(2)

    while(1):
        flag = 1
        i = 0
        while(i<NUM_PLAYERS):
            if len(VICTORY_LIST) == NUM_PLAYERS - 1:
                display_results(VICTORY_LIST,PLAYER_NAME_DICT) #--> result display 
                flag = 2
                break
            if i not in VICTORY_LIST:
                clear()
                print("[INFO]","Player ",PLAYER_NAME_DICT[i]," PLAYER ID ",i," chance :")
                take_chance(NUM_PLAYERS,STORE_DICT,i) #--> get the number , call modify_grid , then show the grid
                check_bingo(VICTORY_LIST,PLAYER_PASSBOOK,STORE_DICT,NUM_PLAYERS,PLAYER_DICT) #--> checks if player won at the instance returns t/f
                grid_show(STORE_DICT[i])
                sleep(2)
                i = i + 1
        if flag == 2:
            break
    sleep(5)

    mainmenu()

#modify the grid --> when player calls a number it is turned to zero
def modify_grid(NUM_PLAYERS,STORE_DICT,number):
    flag = True
    for iter in range(NUM_PLAYERS):
        #find the index of number
        result = np.where(STORE_DICT[iter] == number)
        if len(result[0]) == 0:
            flag = False
        else:
            i,j = result[0][0],result[1][0]
            #traditional init
            temp = STORE_DICT[iter]
            temp[i][j] = 0
            STORE_DICT[iter] = temp
            flag = True
    return flag 

#--> player chance alternator
def take_chance(NUM_PLAYERS,STORE_DICT,player_id):
    choice = input("[INPUT] Enter the number (1-25):")
    if choice.isnumeric() and int(choice)<26 and int(choice)>0:
        choice = int(choice)
        if modify_grid(NUM_PLAYERS,STORE_DICT,choice):
            return
        else:
            print("[GAME] already taken")
            take_chance(NUM_PLAYERS,STORE_DICT,player_id)
    else:
        print("[ERR] invalid entry")
        sleep(2)
        take_chance(NUM_PLAYERS,STORE_DICT,player_id)

def display_results(VICTORY_LIST,PLAYER_NAME_DICT):
    header = ["Winner1","winner2","winner3","winner4","winner5"]
    m_o_h = []
    for i in VICTORY_LIST:
        m_o_h.append(PLAYER_NAME_DICT[i])
    m_o_h = [m_o_h]
    print(tb(m_o_h, header, tablefmt="grid"))

def check_bingo(VICTORY_LIST,PLAYER_PASSBOOK,STORE_DICT,NUM_PLAYERS,PLAYER_DICT):
    for player_id in range(NUM_PLAYERS):
        temp = STORE_DICT[player_id].flatten()

        for i in range(5):
            if temp[i+0] == temp[i+5] == temp[i+10] == temp[i+15] == temp[i+20]:
                if PLAYER_DICT[player_id].check_col(i) == False:
                    PLAYER_DICT[player_id].load_col(i)
                    PLAYER_PASSBOOK[player_id] = PLAYER_PASSBOOK[player_id] + 1
                    if PLAYER_PASSBOOK[player_id] == 5:
                        VICTORY_LIST.append(player_id)

        for i in range(0,21,5):
            if temp[i+0] == temp[i+1] == temp[i+2] == temp[i+3] == temp[i+4]:
                if PLAYER_DICT[player_id].check_row(i) == False:
                    PLAYER_DICT[player_id].load_row(i)
                    PLAYER_PASSBOOK[player_id] = PLAYER_PASSBOOK[player_id] + 1
                    if PLAYER_PASSBOOK[player_id] == 5:
                        VICTORY_LIST.append(player_id)

        if PLAYER_DICT[player_id].check_dgl(0) == False:
            if temp[0] == temp[6] == temp[12] == temp[18] == temp[24]:
                    PLAYER_DICT[player_id].load_dgl(0)
                    PLAYER_PASSBOOK[player_id] = PLAYER_PASSBOOK[player_id] + 1
                    if PLAYER_PASSBOOK[player_id] == 5:
                        VICTORY_LIST.append(player_id)

        if PLAYER_DICT[player_id].check_dgl(4) == False:
            if temp[4] == temp[8] == temp[12] == temp[16] == temp[20]:
                    PLAYER_DICT[player_id].load_dgl(4)
                    PLAYER_PASSBOOK[player_id] = PLAYER_PASSBOOK[player_id] + 1
                    if PLAYER_PASSBOOK[player_id] == 5:
                        VICTORY_LIST.append(player_id)

if __name__ == "__main__":
    mainmenu()
