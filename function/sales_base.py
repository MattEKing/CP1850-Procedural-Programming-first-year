# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 08:46:45 2023

@author: matthew.king
This module contains functions for getting sales data from a user
"""


def get_amount() -> float: 
    """
    
    Get sales amount form the user, converts it to
    a float value, and returns the float value.
    
    -------
    amt : float 

    """
    amt = float(input("Sales amount: "))
    if amt < 0:
        print("Amount has to be greater then 0")
        amt = get_amount()
    return amt 

def get_day(month) -> int:
    """
    
    Gets a day from the user, converts its to an
    int value, and returns the int value.
    -------
    day : int. 

    """ 
    if month == 4 or month == 6 or month == 9 or month == 11:
        max_d = 30
    elif month == 2:
        max_d = 29
    else:
        max_d = 31
    day = int(input("Day 1-{}:".format(max_d)))
    if day < 1 :
        print("days have to be 1-{}".format(max_d))
        day = get_day(month)
    elif day > max_d:
        print("days have to be 1-{}".format(max_d))
        day = get_day(month)        
    return day 

def get_month() -> int:
    """
    
    Get a month from the user,converts to an
    int value, and returns the int value.
    -------
    mon : int.

    """
    mon = int(input('Month: '))
    if mon < 1 or mon > 12:
        print("Month has to be 1-12")
        mon = get_month()
    return mon

def get_year() -> int:
    """
    
    Get a year from the user, convert to an
    int value, and returns the int value.
    -------
    year : int.

    """
    year = int(input("Year: "))
    if year < 2000 or  year > 9999:
        print("year has to be within 2000-9999")
        year = get_year()
    return year
    
def main():
    print("SALES DATA IMPORTER \n")
    print('Enter sales data \n')
    loop = 'y'
    a = 0
    total = 0
    while loop == 'y':
        a += 1
        
        amt = get_amount()
        month = get_month()
        day = get_day(month)      
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

if __name__ == "__main__":
    main()
