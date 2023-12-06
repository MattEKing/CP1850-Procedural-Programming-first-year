# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 09:11:28 2023

@author: matthew.king
"""

print("=" * 50)
print("Shipping calculator")
print("=" * 50)
loop = "y"
while loop == "y":
    
    cost = float(input("Cost of items ordered:  "))
    # Made a different if for negative so it will promt for a cost input before resetting the loop.
    if  cost < 0:
        print("you must enter a postive number.please try again")
        cost = float(input("Cost of items ordered:  "))
    if cost > 0:    
        if cost < 30.00 :
            ship = 5.95
        elif cost > 30.00 and cost <= 49.99:
            ship = 7.95
        elif cost >= 50.00 and cost <= 74.99:
            ship = 9.95
        elif cost >= 75.00:
            ship = 0.00
        else:
            print("Error")
        print("Shipping cost:\t\t\t{}".format(ship))
        total = cost + ship 
        print("total cost:\t\t\t\t{:.2f}".format(total))
    loop = input("\nContinue? (y/n): ")
    print("=" *50)
print("\nBye!")
    
    