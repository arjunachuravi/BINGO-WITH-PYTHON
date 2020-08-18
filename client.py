from socket import error
from network import network
from methods import display_results, modify_grid
from time import sleep
from tabulate import tabulate as tb

client = network()
online = True
curr_player = int(client.get_p_id())
print("you are player", curr_player)

count = 0

while online:
    try:
        game = client.send("get")
    except error as e:
        online = False
        print("[client] cannot connect to game ")
        break
    
    if not (game.connected()):
        print("waiting for game players....")
        sleep(10)
        continue
    
    if len(game.victory_list) == len(game.players) - 1:

        if curr_player in game.victory_list:
            print("winner , please exit the program ")
            break
        else:
            print("you lost , please exit the program ")
            break


    if (game.connected()) and (not(game.went[curr_player])) and (curr_player not in game.victory_list):

        choice = 0
        flag = 1
        while flag:
            if count == 0:
                string = input("## M(1/0))## -->")
                count = 1
                client.send(string)
                flag = 0
                continue
            
            if not game.GAME_PLAYERS[curr_player].machine_player:
                print("########## player-->",curr_player,"'s turn ##########")
                print(tb(game.GAME_PLAYERS[curr_player].player_matrix(), tablefmt="fancy_grid"))
                choice = input("[INPUT] Enter the number (1-25):")
            else:
                choice = str(game.GAME_PLAYERS[curr_player].computerlogic())
            if choice.isnumeric() and 26 > int(choice) > 0:
                choice = int(choice)
                if modify_grid(game.GAME_PLAYERS, choice):
                    if game.GAME_PLAYERS[curr_player].machine_player:
                        print("machine called -->",choice)
                    print("########## player-->",curr_player,"'s after-matrix ##########")
                    print(tb(game.GAME_PLAYERS[curr_player].player_matrix(), tablefmt="fancy_grid"))
                    flag = 0
                    client.send(str(choice))
                    client.send("check")
                else:
                    print("[GAME] already taken")
                    flag = 1
            else:
                print("[ERR] invalid entry")
                sleep(2)
                flag = 1