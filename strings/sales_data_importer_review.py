# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 09:30:28 2023

@author: matthew.king
"""
import csv
FILENAME = 'sales_data.csv'

sales_dict = [{'Date':'2020-12-22','Quarter': '4','Region':'West','Amount': '12493.00'},
              {'Date':'2021-09-15','Quarter': '3','Region':'East','Amount': '13761.00'},
              {'Date':'2021-05-15','Quarter': '2','Region':'East','Amount': '9710.00'},
              {'Date':'2021-08-08','Quarter': '3','Region':'Cent','Amount':'8934.00'}]

def title():
    print('SALES DATA IMPORTER\n')
    
def command_menu():
    print('COMMAND MENU\n'
          'view   - View all sales\n'
          'add    - Add sales\n'
          'import - Import sales from file\n'
          'exit   - Exit program\n')
    
def write_file():
    with open(FILENAME, 'w') as file:
        for row in sales_dict:
            writer_data = row['Date'] + ',' + row['Quarter'] + ',' + row['Region'] + ',' + row['Amount']     
            file.write(writer_data)
        
def get_year():
    while True:
        try:
            year = int(input("Year:  "))
            if year < 1900 or year > 3000:
                print("invalid selection.")
            else:
                break
        except ValueError:
            print("invalid selection.")
    return year

def get_month():
    while True:
        try:
            month = int(input("month: "))
            if month < 1 or month > 12:
                print('invalid selection.')
            else:
                break
        except ValueError:
            print('invalid selection.')
    return month


def get_day(get_month):
    month = get_month() 
    while True:
        try:
            if month == 4 or month == 6 or month == 9 or month == 11:
                d = 30
            elif month == 2:
                d = 28
            else:
                d = 31
            day = int(input("day (1-{d})"))
            if day < 1 or day > d:
                print("invalid selection")
            else:
                break
        except ValueError:
            print("invalid selection.")
    return day
    
def add_sale():
    get_year()
    get_month()
    get_day(get_month())
    
    
    
    
    
    
    