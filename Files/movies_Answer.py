# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 08:42:18 2023

@author: matthew.king
"""

FILENAME = 'movie.txt'

def write_movies(movies_list):
    with open(FILENAME,'w') as file:
        for movies in movies_list:
            file.write(f"{movies}\n")
            
def read_movies():
    movies_list = []
    with open(FILENAME, 'w') as file:
        for name in file:
            name = name.replace('\n', "")
            movies_list.append(name)
    return movies_list

with open(FILENAME) as file:
    text = file.read()
    movies_list2 = text.split('\n')
    
movies_2d = [["Monty Python", 1975],
             ["cat burning", 1958],
             ['waterfront', 1954]]
 
import csv 

with open("movies.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(movies_2d)
    
with open('movies.csv', newline='') as file_handler:
    reader = csv.reader(file_handler)
    for row in reader:
        print(f"{row[0]} {row[1]}")
        
with open('movies_delim.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerows(movies_2d)