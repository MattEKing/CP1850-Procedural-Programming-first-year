# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:08:37 2023

@author: matthew.king
"""

def menu():
    return "COMMAND MENU\nList - List all movies\nAdd  - Add a movie\nDel - Delete a movie\nExit - Exit program"
    
def movies_list(movies):
    i = 1 
    for i, item in enumerate(movies):
        print("{}. {} ({})".format(i + 1,item[0], item[1]))  
    print()
    
def add_movie(movies):
    name = input("name: ")
    year = int(input("Year: "))
    if year < 1:
        print("invalid year.\n")
        add_movie(movies)
    else:
        m = [name, year]   
        print("{} was added \n".format(name))
        movies.append(m)
    
def del_movie(movies):
    num = int(input("number: ")) - 1
    if (num < 0) or (num + 1 > len(movies)):       
        print("invalid selection \n")
    else:
        print("{} was deleted. \n".format(movies[num][0]))
        movies.pop(num)
                
def main():
    print(menu())     
    movies = [["Monty Python and the holy grail", 1975],
              ["On the Waterfront", 1954],
              ["Cat on the Hot Tin Roof", 1939]]
    loop = 'y'
    while loop == 'y':
        command = input("\nCommand: ").lower()
        if command == "list":
            movies_list(movies)
        elif command == "add":     
            add_movie(movies)
        elif command == "del":
            del_movie(movies)
        elif command == "exit":
            break
        else:
            print("invalid command.")
  
    print("\nBye!")  
    
if __name__ =="__main__" :          
    main()
   


    