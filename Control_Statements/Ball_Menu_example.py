# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:44:44 2023

@author: matthew.king
"""

print("=" * 30)
print("\t Baseball Team manager")
print("\nMENU OPTIONS")
print("1 - Calculate batting average")
print('2 - Exit program')
print("=" * 30)

loop = True 
while (loop):
    option = int(input("selcet menu:\t"))
    if (option == 1):
        print("Calculate batting average...")
        bats = int(input("official number of at bats: "))
        hits = int(input("numbers of hit's: \t\t\t"))

        average = hits / bats

        print("batting average is {:.3f} \n".format(average))
        print("=" * 30)
    elif (option == 2):
        print("\nBye!")
        break 
    else:
        print("\nerror")
        print("=" * 30)
