# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 08:32:41 2023

@author: matthew.king
"""

print("================================================")
print("\tBaseball Team Manager \n")
print("This program calculates the batting average for the player's based")
print("on the player's offcial number of at bats and hits.")
print("================================================\n")

name = input("Player's name: \t \t \t \t")
bats = int(input("official number of at bats: "))
hits = int(input("numbers of hit's: \t\t\t"))

average = hits / bats

print("\n",name,"'s batting average is {:.3f}".format(average))


    
