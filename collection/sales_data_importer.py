# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 08:21:38 2023

@author: matthew.king
"""

command_options = ('view','add','menu','exit')
sales_list = []
month_30 =(4,6,9,11)
quar_1 = (1,2,3)
quar_2 = (4,5,6)
quar_3 = (7,8,9)
quar_4 = (10,11,12)

def title():
    print("SALES DATA IMPORTER\n")
def commands():
    print('-'*50)
    print("COMMAND MENU")
    print("view - view all sales")
    print("add  - add sales")
    print("menu - show menu")
    print("exit - exit program")
    print("-"*50)
    print()
    
def get_command():
    command = input("Please enter a command: ")
    if command not in command_options:
        print("Invalid selection")
    command = command.lower()
    return command 


def view_sales_list():
    if sales_list == []:
        print("No sales to view.")
        print("-"*50)
    else:
        print("\n\t\tDate\t\tQuarter\t\tAmount")
        print('-'*50)
        for i, sales in enumerate(sales_list,start = 1):
            print("{}.\t\t{}-{}-{}\t{}\t\t\t{}".format(i,sales[1],sales[2],sales[3],sales[4],sales[0]))
            print("\n")
def get_amount() -> float:
    amount = float(input('Amount:\t\t\t'))
    if amount < 0:
        print("invalid amount")
        get_amount()
    return amount

def get_year() -> int:
    year = int(input('Year:\t\t\t'))
    return year

def get_month() -> int:
    month = int(input('Month(1-12):\t'))
    if month < 1 or month > 12:
        print("invalid month")
    return month

def get_day(month) -> int:
    if month == month_30:
        max_day = 30
    elif month == 2 :
        max_day = 28
    else:
        max_day = 31
    day = int(input(f"day(1-{max_day}):\t\t"))
    return day 
        
def get_quarter(month) -> int:
    if month in quar_1:
        quarter = 1
    elif month in quar_2:
        quarter = 2
    elif month in quar_3:
        quarter = 3 
    elif month in quar_4:
        quarter = 4
    else:
        quarter = 0
    return quarter

def add_sale():
    print("-"*50)    
    new_sale = []
    amount = get_amount()
    new_sale.append(amount)
    year = get_year()
    new_sale.append(year)
    month =get_month()
    new_sale.append(month)
    day = get_day(month)
    new_sale.append(day)
    quarter = get_quarter(month)
    new_sale.append(quarter)
    sales_list.append(new_sale)
    print("sale was added")
        
def main():
   
    title()
    commands()
    while True:
        command = get_command()
        if command == 'view':
            view_sales_list()
        elif command == 'add':
            add_sale()
        elif command == 'menu':
            commands()
        elif command == 'exit':
            break
    print("\nBye!")
        
        
        
main()    
        
        
        
        
        