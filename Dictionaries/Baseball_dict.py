# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 09:18:54 2023

@author: matthew.king
"""
import csv

def title():
    print("="*50)
    print("\t\t\t Baseball Team Manager")
    print("\nCURRENT DATE:\t2021-03-19")
    print("\nGAME DATE: ")
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
    
def player_list(player):
    for p in enumerate(player, start = 1):
        print(f"{p}. {player['name']}")
        




def main():
    player = [{'name':'Tommy La Stella','POS':'3B', 'AB':1316, 'H':360, 'AVG':0.274},
               {'name':'Mike Yastrzemski','POS':'RF', 'AB':563, 'H':168, 'AVG':0.281},
               {'name':'Donovan Solano','POS':'2B', 'AB':1473, 'H':407, 'AVG':0.276},
               {'name':'Buster Posey','POS':'C', 'AB':4575, 'H':1380, 'AVG':0.302},
               {'name':'Brandon Belt','POS':'1B', 'AB':3811, 'H':1003, 'AVG':0.263},
               {'name':'Brandon Crawford','POS':'SS', 'AB':4402, 'H':1099, 'AVG':0.250},
               {'name':'Alex Dickerson','POS':'LF', 'AB':586, 'H':160, 'AVG':0.273},
               {'name':'Austin Slater','POS':'CF', 'AB':569, 'H':147, 'AVG':0.274},
               {'name':'Kevin Gausman','POS':'P', 'AB':56, 'H':2, 'AVG':0.036}]

    title()
    menu()
    while True:
        option = int(input("Menu Options: "))
        if option < 1 or option > 7:
            print("invalid selection")
        elif option == 1:
            print("\t\tPlayer\t\tPOS\t AB\t H\tAVG")
            print("-"*50)
            player_list(player)
        elif option == 2:
            add_play(player)
        elif option == 3:
            del_play(player)
        elif option == 4:
            mov_play()
        elif option == 5:
            mov_pos(player)
        elif option == 6:
            edit_play(player)
        elif option == 7:
            break
