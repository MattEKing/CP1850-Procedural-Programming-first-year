# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 08:24:58 2023

@author: matthew.king
"""

postion = ["C","1B","2B","3B","SS","LF","CF","RF","P"]
player = [["Joe","p",10,2,0.2 ],["Tom","SS",11,4,0.364],
          ["Ben","3B",4,1,0.25],["Mike","C",4,1,0.25]]

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
    print("5 - Edit player stats")
    print("7 - Exit program \n")  
    print("POSTIONS")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")
    print("="*50)

      
def player_list():
    for i, item in enumerate(player, start = 1): 
        print("{}.\t\t{} \t\t{}\t {}\t {}\t{}".format(i,item[0],item[1],item[2],item[3],item[4]))
    print()  
        

def add_play():
    name = input("Name: ")
    post = str(input("postion: ")).upper()
    bat = int(input("At bats: "))
    if bat < 1:
        print("invalid selection")
        add_play()
    hit = int(input("Hits: "))
    if hit < 1 or hit > bat:
        print("invalid selection")
        add_play()
    avg = hit / bat
    if postion.count() in range(len(player)):
        play = [name, post, bat, hit, avg]       
        player.append(play)
        print("{} was add".format(name))
    else:
        print("Invalid selection")
        print("POSTIONS")
        print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")
        add_play()
        
def del_play():
    num = int(input("Enter number: ")) 
    if num < 1 or num > len(player):
        print("Invalid selection")
    else:
        print("{} was deleted".format(num))
        player.pop(num)
 
def mov_play():
    num = int(input("select line up number: "))  
    if num < 1 or num < len(player):
        print("Invalid selection")
        mov_play()
    if player.count() in range(len(player)):
        print("{} was selected".format(player[num][0]))
        move = int(input("New line up number: "))
        player.insert(move, player)
    
def main():
    title()
    menu()
    while True:
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
            
            
main()    