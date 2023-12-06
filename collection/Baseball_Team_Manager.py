# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 09:48:22 2023

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
                avg = hit / bat
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
        elif option == 5:
            mov_pos()
        elif option == 6:
            edit_play()
        elif option == 7:
            break
            
if __name__ == "__main__":

    main()
    
    print("\nBye!")



