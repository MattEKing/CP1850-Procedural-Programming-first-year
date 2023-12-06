# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 08:14:50 2023

@author: matthew.king
"""
from random import randint
 
def generate_deck() -> list:
    suits = ['Hearts','Dimonds','Spades','Clubs']
    ranks = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']  
    deck = []
     
    for s in suits:
        for r in ranks:
            if r == "ace":
                v = 11
            elif r.isnumeric():
                v = int(r)
            else:
                v = 10
            deck.append([r,s,v])      
    return deck           
    
def title():
    print("BLAKCJACK!")
    print("Blackjack payout is 3:2")
    print("Enter 'x' for bet to exit \n")
    print()
    
def start_money() -> float:
    while True:
        money = float(input("\nStarting money:\t"))
        if money < 5:
            print("mininum amount of starting money is 5")
            money = start_money()
        elif money > 10000:
            print("Mazimum amount of start money is 10000 ")
            money = start_money()
        else:
            return money
            
def bet_amount(start_money) -> float:
    while True:
         bet_amt = float((input("\nbet amount:\t\t")))
         if bet_amt > start_money:
             print("not enough money")
         if bet_amt < 5:
             print("minimum bet amount is 5")
             bet_amt = bet_amount()
         if bet_amount > 1000:
             print("Maximum bet amount is 10000")
             bet_amt = bet_amount()
         if bet.lower == 'x':
             return 'x'
    
def draw_card(deck:list):
    return deck.pop((randint(0,len(deck))))
    
def dealer_hand(deck,d_hand):
    card = draw_card(deck)  
    d_hand.append(card)

def player_hand(deck):
    p_hand = [draw_card(deck) for c in range(2)]
    return p_hand

def point_total(hand):
    points = 0
    aces = 0
    for card in hand:
        points += card[3]
        if card[0] == 'Ace':
            aces += 1
    if aces > 0 and points > 21:
        points = points - (aces * 10)
    if aces > 1 and points <= 11:
        points += 10
    return points
        
def shuffle(deck):
    random.shuffle(deck)
    
def main():
    title()
    deck = generate_deck()  
    d_hand = []       
    dealer_hand(deck, d_hand)
    start_money()
    bet_amount()
    while True:
        command = input("Hit or stand? (h/s): ").lower()
        if command == 'h':
            player_hand(deck)
        elif command == 's':
            
            
    
   
    
    # print(d_hand)
    # print(p_hand)
main()
    
