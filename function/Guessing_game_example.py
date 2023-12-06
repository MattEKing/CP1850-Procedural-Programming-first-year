# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 08:51:41 2023

@author: matthew.king
"""
 
def title():
    return("Guess the Number!\nI'm thinking of a number from 1 to 10\n")

def guess_game():
    import random
    loop = 'y'
    trys = 0 
    number = random.randint(1, 10) 
    while loop == 'y':       
        guess = int(input("Your guess: "))
        trys += 1
        if guess == number:
            print("You guess it in {} tries".format(trys))
            trys = 0
            loop = input("Play again? (y/n): ")
            number = random.randint(1, 10) 
        elif guess < number:
            print("too low")
        elif guess > number:
            print("too high")            
        if loop == 'n':
            print("\nBye!")          
def main():
    title()
    guess_game()
    
if __name__ =='__main__':
    main()
  