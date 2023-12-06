# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 09:00:27 2023

@author: matthew.king
"""

import sales_base
# help(sales_base)

loop = 'y'
a = 0
total = 0
from sales_base import get_amount
from sales_base import get_day
from sales_base import get_month 
from sales_base import get_year

while loop == 'y':

    a += 1
    amt = get_amount()
    day = get_day()
    month = get_month()
    year = get_year()
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

