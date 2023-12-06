# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 08:19:04 2023

@author: matthew.king
"""

def print_title():
    return "BLACKJACK!  \nBlackjack payout is 3:2\nEnter 'x' for bet to exit"

def start_money():
    start_money = int(input("\nStarting amount:\t"))
    return start_money 

def bet_amount():
    bet_amt = input("\nBet amount: ")
    return bet_amt

def bwpl():
    import random
    num = random.randint(1, 100)
    if num > 95:
        return 'b'
    elif num > 58:
        return 'w'
    elif num > 49:
        return 'p'
    else:
        return 'l'

def main():
    print(print_title())
    start_mon = start_money()
    while (start_mon > 5 and start_mon < 10000):
        bet_amt = bwpl()
        if bet_amt == 'x':
            break
    
        
   