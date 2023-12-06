# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 08:19:07 2023

@author: Matthew.king
"""

import csv

FILENAME = 'all_sales.csv'

def write_file(sales_list):
    with open('all_sales.csv', 'w') as all_sales:
        write = csv.writer(all_sales)
        write.writerows(sales_list)
        
def read_file():
    sales_list = []
    with open('all_sales.csv', 'r' , newline = '') as read_sales:
        reader = csv.reader(read_sales)
        for row in reader:
            sales_list.append([ float(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4])])
    return sales_list

def sales_log(file_name, object_name):
    with open(file_name, 'a') as file:
        file.write(f'{object_name}\n')
        
def read_sales_log(file_name):
    sales_log = []
    with open(file_name) as file:
        for name in file:
            name = name.replace('\n', "")
    return sales_log
    
