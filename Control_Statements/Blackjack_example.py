# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:14:04 2023

@author: matthew.king
"""

print("BLACKJACK!")
print("Blackjack payout is 3:2")
print("Enter 'x' for bet to exit")

start_money = float(input("\nStarting money:\t"))

loop = True

while loop:
    
   bet_amount = (input("\nbet amount:\t\t"))
   
   if bet_amount == "x":
       print("Bye!")
       break   
   option = input("Blackjack, win, push, or lose? (b/w/p/l):")
   if option == "b":
       print("money:\t\t{}".format(start_money + float(bet_amount) * 1.5))      
       money = start_money + float(bet_amount) *1.5
   elif option == "w":
        money = money + float(bet_amount)
        print("money:\t\t\t{}".format(money))                       
   elif option == "p":
        print("money:\t\t\t{}".format(money))        
   elif option == "l":
        money = money - float(bet_amount)
        print("money:\t\t\t{}".format(money))      
   else:
        print("Error")


    

