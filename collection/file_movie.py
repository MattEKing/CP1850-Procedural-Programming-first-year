# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 09:33:24 2023

@author: matthew.king
"""

def title():
    print("The Movie list Program")
    print()
    
def menu():
    return "COMMAND MENU\nList - List all movies\nAdd  - Add a movie\nDel - Delete a movie\nExit - Exit program"
    
def movies_list():
   
    with open("movie_file.txt",'r') as movies:
        movie = movies.readlines()
        for i, name in enumerate(movie):
            print(f"{i}. {name}", end='')
        
        
def add_movie():
    name = input("name: ")
    with open("movie_file.txt",'a') as movies:
        movies.write(name)      
    print("{} was added \n".format(name))

    
def del_movie(movie_file):
    num = int(input("number: ")) - 1
    if (num < 0) or (num + 1 > len(movies)):       
        print("invalid selection \n")
    else:
        print("{} was deleted. \n".format(movies[num][0]))
        movies.pop(num)
                
def main():
    
    # movie_file = open("movie_file.txt",'w')
    
    
    
    title()
    print(menu())     
    movies = [["Monty Python and the holy grail", 1975],
              ["On the Waterfront", 1954],
              ["Cat on the Hot Tin Roof", 1939]]
    loop = 'y'
    while loop == 'y':
        command = input("\nCommand: ").lower()
        if command == "list":
            movies_list()
        elif command == "add":     
            add_movie()
        # elif command == "del":
        #     del_movie()
        elif command == "exit":
            break
        else:
            print("invalid command.")
            
            
            
main()