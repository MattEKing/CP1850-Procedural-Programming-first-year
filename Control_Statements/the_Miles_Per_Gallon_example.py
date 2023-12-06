# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 09:24:12 2023

@author: matthew.king
"""

print("The Miles Per Gallon Program \n") 

miles = float(input("Enter miles driven: \t \t"))
gallon = float(input("Enter Gallons of gas used: \t"))

if (gallon <= 0):
    print("gallons used must be greater then zero. Try again. ")
else:
    print("Miles Per Gallon: \t \t \t{:.1f} \n".format(miles / gallon))

print("Bye!")

