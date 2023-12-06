# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 08:57:09 2023

@author: matthew.king
"""

print("SALES DATA IMPORTER \n")
print('Enter sales data \n')

total = 0
sales = "y"
a = 0
while sales == "y":
    
        a += 1
        amt = float(input("Amount: \t "))
        year = int(input("Year: \t\t "))
        month = int(input("Month (1-12):"))
        day = int(input("Day (1-31):  "))
        if month in range(1,4):
            quar = "Quarter 1"
        elif month in range(4,7):
            quar = "Quarter 2"
        elif month in range(7,10):
            quar = "Quarter 3"
        elif month in range(10,13):
            quar = "Quarter 4"
            
        print("{}.\t\t\t {}-{}-{}\t{}\t${:.1f} \n".format(a,year,month,day,quar,amt))
        
        sales = input("Enter more sales? (y/n)\t")
        total += amt
    
        if sales == "n":
            break
        elif sales != "y":
            print("Error")
        
print("Total Sales")
print("="*11)
print("${:.1f}".format(total))
print("\nBye!")







     
