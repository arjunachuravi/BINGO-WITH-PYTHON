import numpy as np
from tabulate import tabulate as tb
import os
from time import sleep


# function to clear screen
def clear():
    # for windows 
    if os.name == 'nt':
        _ = os.system('cls')


# function to exit program
def exit_prgm():
    clear()
    print("\n[INFO] Exiting")
    sleep(4)
    os._exit(os.X_OK)


# result-display function
def display_results(VICTORY_LIST):
    header = ["Winner1", "winner2", "winner3", "winner4", "winner5"]
    m_o_h = []
    for i in VICTORY_LIST:
        m_o_h.append("player " + str(VICTORY_LIST[i]))
    m_o_h = [m_o_h]
    print(tb(m_o_h, header, tablefmt="grid"))


# modify grid values
def modify_grid(GAME_PLAYERS, number):
    flag = True
    for ITER in GAME_PLAYERS:
        # find the index of number
        result = np.where(GAME_PLAYERS[ITER].player_array == number)
        if len(result[0]) == 0:
            flag = False
        else:
            pos = result[0][0]
            GAME_PLAYERS[ITER].player_array[pos] = 0
            flag = True
    return flag


# manual entry of matrix
def bingo_matrix_man(GAME_PLAYERS, player_id):
    GAME_PLAYERS[player_id].player_array = np.zeros(25)
    print("[INFO] NOTE: NUMBERS WILL BE INITIALIZED BY ROWS")
    for i in range(25):
        clear()
        print(tb(GAME_PLAYERS[player_id].player_matrix(), tablefmt="fancy_grid"))
        sleep(2)
        err = 1
        while (err):
            clear()
            num = input("[INPUT] input :")
            if num.isnumeric() and 26 > int(num) > 0 and int(num) not in GAME_PLAYERS[player_id].player_array:
                num = int(num)
                GAME_PLAYERS[player_id].player_array[i] = num
                err = 0
            else:
                print("[ERR] error @_@ type again : it may be already present ")
                sleep(2)
                err = 1
    print("[INFO] all done")


# bingo checker
def check_bingo(VICTORY_LIST, GAME_PLAYERS):
    for player_id in GAME_PLAYERS:
        for i in range(5):
            if GAME_PLAYERS[player_id].player_array[i+0] == GAME_PLAYERS[player_id].player_array[i+5] == GAME_PLAYERS[player_id].player_array[i+10] == GAME_PLAYERS[player_id].player_array[i+15] == GAME_PLAYERS[player_id].player_array[i+20]:
                if not GAME_PLAYERS[player_id].check_col(i):
                    GAME_PLAYERS[player_id].load_col(i)
                    GAME_PLAYERS[player_id].player_passbook = GAME_PLAYERS[player_id].player_passbook + 1
                    if GAME_PLAYERS[player_id].player_passbook == 5:
                        VICTORY_LIST.append(player_id)

        for i in range(0,21,5):
            if GAME_PLAYERS[player_id].player_array[i+0] == GAME_PLAYERS[player_id].player_array[i+1] == GAME_PLAYERS[player_id].player_array[i+2] == GAME_PLAYERS[player_id].player_array[i+3] == GAME_PLAYERS[player_id].player_array[i+4]:
                if not GAME_PLAYERS[player_id].check_row(i):
                    GAME_PLAYERS[player_id].load_row(i)
                    GAME_PLAYERS[player_id].player_passbook = GAME_PLAYERS[player_id].player_passbook + 1
                    if GAME_PLAYERS[player_id].player_passbook == 5:
                        VICTORY_LIST.append(player_id)

        if not GAME_PLAYERS[player_id].check_dgl(0):
            if GAME_PLAYERS[player_id].player_array[0] == GAME_PLAYERS[player_id].player_array[6] == GAME_PLAYERS[player_id].player_array[12] == GAME_PLAYERS[player_id].player_array[18] == GAME_PLAYERS[player_id].player_array[24]:
                    GAME_PLAYERS[player_id].load_dgl(0)
                    GAME_PLAYERS[player_id].player_passbook = GAME_PLAYERS[player_id].player_passbook + 1
                    if GAME_PLAYERS[player_id].player_passbook == 5:
                        VICTORY_LIST.append(player_id)

        if not GAME_PLAYERS[player_id].check_dgl(4):
            if GAME_PLAYERS[player_id].player_array[4] == GAME_PLAYERS[player_id].player_array[8] == GAME_PLAYERS[player_id].player_array[12] == GAME_PLAYERS[player_id].player_array[16] == GAME_PLAYERS[player_id].player_array[20]:
                    GAME_PLAYERS[player_id].load_dgl(4)
                    GAME_PLAYERS[player_id].player_passbook = GAME_PLAYERS[player_id].player_passbook + 1
                    if GAME_PLAYERS[player_id].player_passbook == 5:
                        VICTORY_LIST.append(player_id)