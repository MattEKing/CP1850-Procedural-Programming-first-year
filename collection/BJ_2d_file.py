# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 08:54:15 2023

@author: matthew.king
"""

def write_file(FILENAME, balence):
    with open(FILENAME, 'w') as money:
        money.write(str(balence))
        
def read_file(FILENAME):
    with open(FILENAME, 'r') as file:
        money = file.readline()
        return int(money)
