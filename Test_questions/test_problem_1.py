# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 09:07:50 2023

@author: matthew.king
"""

print("Year program")

year = int(input("Enter the value of year: "))

if year in range(2000,3001, 4):
    print("True")
else:
    print("False")