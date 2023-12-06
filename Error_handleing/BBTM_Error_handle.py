# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 09:04:36 2023

@author: matthew.king
"""

import csv
postion = ["C","1B","2B","3B","SS","LF","CF","RF","P"]

player = [["Tommy","3B",1316, 360, 0.274],
           ["Mike","RF", 563, 168, 0.298],
           ["Don","2B", 1473, 407, 0.276],
           ["Buster","C", 4575, 1380, 0.302],
           ["Bran","1B", 3811, 1003, 0.263],
           ["Bran","SS", 4402, 1099, 0.25],
           ["Alex","LF", 586, 160, 0.273],
           ["Austin","CF", 569, 147, 0.258],
           ["Kevin","P", 56, 2, 0.036]]
FILENAME = 'BB_Players.csv'

def title():
    print("="*50)
    print("\t\t\t Baseball Team Manager")
def menu():
    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player postion")
    print("6 - Edit player stats")
    print("7 - Exit program \n")   
    print("POSITIONS")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")   
def player_list():
    for i, item in enumerate(player, start = 1): 
        print("{}.\t\t{} \t\t{}\t {}\t {}\t{}".format(i,item[0],item[1],item[2],item[3],item[4]))
    print()    
def add_play():
    
    name = input("Name: ")
    while True :
        pos = str(input("Postion: ")).upper()
        while True :
            if pos not in postion:
                print("Invalid selection")
            else:    
                bat = int(input("At bats: "))
                if bat < 1:
                    print("invalid selection")
                hit = int(input("Hits: "))
                if hit < 1 or hit > bat:
                    print()
                try:
                    avg = hit / bat
                except ZeroDivisionError:
                    avg = 0.0
                play = [name,pos,bat,hit,avg]
                player.append(play)
                print("{} was add".format(name))
                break
            break
        break    
def del_play():
    num = int(input("Enter number: ")) - 1
    if num < 1 or num > len(player):
        print("Invalid selection")
        del_play()
    else:
        print("{} was deleted".format(player[num][0]))
        player.pop(num - 1)          
            
def mov_play():
    while True:
        current = int(input("Current line up number: "))
        print("{} was selected".format(player[current - 1][0]))
        if current < 1 or current > len(player):
            print("invalid selection")
        else:
            move = int(input("New line up number: "))
            pop = player.pop(current - 1)
            player.insert(move - 1, pop)      
            break
    print("{} was moved".format(player[move - 1][0]))             
    
def mov_pos():
    num = int(input("Enter number: ")) -1 
    print("{} was selected".format(player[num][0]))
    if num < 0 or num > len(player):
        print("invalid selection")
    n_pos = str(input("New postion: ")).upper()
    while True:
        if n_pos not in postion:
            print("invalid selection")
            mov_pos()
        else:
            player[num][1] =n_pos 
            print("{} has changed postions".format(player[num][0]))
            break
                   
def edit_play():
    num = int(input("Enter number: ")) -1
    print("{} was selected".format(player[num][0]))
    if num < 0 or num > len(player):
        print("invalid selection")
        edit_play()
    n_bat = int(input("Enter new bats: "))
    n_hit = int(input("Enter new hits: "))
    n_avg = n_hit / n_bat
    while True:
        if n_hit > n_bat:
            print("invalid selection")
            edit_play()
        else:
            player[num][2] = n_bat
            player[num][3] = n_hit
            player[num][4] = n_avg
            print("{} stats have been updated".format(player[num][0]))
            break
     
def write_player_file(players):
    with open('BB_Players.csv', 'w', newline = '') as player_list:
        write_file = csv.writer(player_list)
        write_file.writerows(player)
    
def read_file():
    with open(FILENAME, 'w') as player_file:
        reader = csv.reader(player_file)
        for row in reader:
            player.append([row[0], row[1], row[2],row[3],row[4]])
        
        
    
    
def main():
    title()
    menu()
    while True:
        try:
            option = int(input("Menu Options: "))
            if option < 1 or option > 7:
                print("invalid selection")
            elif option == 1:
                print("\t\tPlayer\t\tPOS\t AB\t H\tAVG")
                print("-"*50)
                player_list()
            elif option == 2:
                add_play()
            elif option == 3:
                del_play()
            elif option == 4:
                mov_play()
            elif option == 5:
                mov_pos()
            elif option == 6:
                edit_play()
            elif option == 7:
                break
        except ValueError:
            print("Not a valid opition")
if __name__ == "__main__":

    main()
    
    print("\nBye!")
