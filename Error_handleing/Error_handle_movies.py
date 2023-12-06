# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 10:07:13 2023

@author: matthew.king
"""

def command_menu():
    print("list - List all movies")
    print('add  - Add a movie')
    print("del  - Delete a movie")
    print("exit - Exit program")
    print()
    
def get_command():
    command = input("Command: ")