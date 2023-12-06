# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 08:54:22 2023

@author: matthew.king
"""

def title():
    print("The Total Calculator Program")
    print()
    
def get_price():
    """
    Returns the price of the object.
    -------
    price : float number.

    """
    while True:
        try:
            price = float(input("Enter price: "))  
            return price
        except ValueError:
            print("invalid decimal number. try again.")
    
def get_quant():
    '''
    Returns the quantity of the object.
    -------
    quant : integer number.

    '''
    while True:
        try:
            quant = int(input("Enter quantity: "))
            return quant
        except ValueError:
            print('invalid integer. try again.')
            

def main():   
    title()
    loop = 'y'
    while loop:
       price = get_price()
       quant = get_quant()
       total = price * quant
       print(f"\nPrice:\t  {price}")
       print(f"Quantity: {quant}")
       print(f"Total:\t  {total}")
       loop = input("\nTry again (y/n): ")
       if loop == 'n':
           return
       else:
           print("invalid selection, try again")
           loop = input("\nTry again (y/n): ")
    print("\nBye!")     


if __name__ == '__main__':
    main()
    