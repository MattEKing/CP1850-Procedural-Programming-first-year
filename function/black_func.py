# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 09:04:42 2023

@author: matthew.king
"""

def title():
    """
    

    Returns
    -------
    None.

    """
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print("Enter 'x' for bet to exit")
    
 
def start_money():
    money = float(input("\nStarting money:\t"))
    if money < 5:
        print("mininum amount of starting money is 5")
        money = start_money()
    elif money > 10000:
        print("Mazimum amount of start money is 10000 ")
        money = start_money()
    return money
       
     
def bet_amount():
     bet_amt = float((input("\nbet amount:\t\t")))
     if bet_amt < 5:
         print("minimum bet amount is 5")
         bet_amt = bet_amount()
     if bet_amount > 1000:
         print("Maximum bet amount is 10000")
         bet_amt = bet_amount()
     
            
def bwpl():
    import random
    num = random.randint(1, 100)
    if num > 95:
        return "b"
    elif num > 58:
        return "w"
    elif num > 49:
        return "p"
    else:
        return "l"

def Blackjack():
    """
    

    Returns
    -------
    None.

    """
    money = start_money()
    bet = bet_amount()
    import random
    loop = 'y'
 
    while loop == 'y':
       
      out = random.randint(1, 101)   
      if  (out >= 96):
          money = money + (bet) *1.5
          print("Blackjack.")
          print("money:\t\t{}".format(money))
          
      elif (out >= 58 and out <= 95):
           money = money + (bet)
           print("you win.")
           print("money:\t\t\t{}".format(money)) 
                         
      elif (out >= 49 and out <= 57 ):
           print("you pushed")
           print("money:\t\t\t{}".format(money))
           
      elif (out >= 0 and out <= 48):
           money = money - (bet)
           print("you lost.")
           print("money:\t\t\t{}".format(money))
      
       
def main ():
    print(title())
    money = start_money()
    while (money > 0):
        bet_amt = bet_amount()
        if bet_amt == "x"
            
      
print(main())
print("Bye!")    
  

   
