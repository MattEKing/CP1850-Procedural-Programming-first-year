# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 09:57:32 2023

@author: matthew.king
"""
import csv

FILENAME = 'movies_2d.csv'
# movies_2d = [["Monty Python", 1975],
#              ["cat burning", 1958],
#              ['waterfront', 1954]]

def title():
    print("The Movie list Program")
    print()
    
def menu():
    return "COMMAND MENU\nList - List all movies\nAdd  - Add a movie\nDel - Delete a movie\nExit - Exit program"

def list_movies(movies_list):
    with open(FILENAME, 'r', newline = '') as movies:
        
   
def add_movies():
    movies_list = [["Monty Python", 1975],
                  ["cat burning", 1958],
                  ['waterfront', 1954]]
    with open(FILENAME, 'w') as file:
        for name in file:
            name = name.replace('\n', "")
            movies_list.append(name)
    return movies_list