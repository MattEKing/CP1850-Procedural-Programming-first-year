# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 08:05:15 2023

@author: matthew.king
"""
# value error handleing. covers invalid inputs for the value type.
try:
    number = int(input("Enter an integer: "))
    print(f"you entered {number}")
except ValueError as ve:
    print("You entered an invalid integer, try again.")
    print(f"{ve}")
print("Bye!")

# Blanket expcept example. cover all the possable errors.

try:
    number = int(input("Enter an integer: "))
    print(f"you entered {number}")
except:
    print("You entered an invalid integer, try again.")
print("Bye!")

