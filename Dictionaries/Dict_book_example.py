# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:40:51 2023

@author: matthew.king
"""

def command_menu():
    print("COMMAND MENU")
    print("show - Show book info")
    print("add  - Add book")
    print("edit - Edit book")
    print("del  - Delete book")
    print("exit - Exit program")
    
    
def show_book(books):
    title = input("Title: ")
    if title in books:
        print("Author name: {}".format(books[title]['Author']))
        print("Publication year: {}".format(books[title]['Year']))
    else:
        print(f"{title} not in catalog.")
              
def add_book(books):
    new_title = input("Title: ")
    if new_title in books:
        print("This book is already in the catalog.")
    else:
        author = input("Author name: ")
        year = int(input("Publication year: ")) 
        new_book = {'Author': author, 'Year': year}
        books[new_title] = new_book
        print(f"{new_title} was add to the catalog.")
    
def del_book(books):
    del_title = input("Title: ")
    if del_title in books:
        print(f"{del_title} was deleted")
        del books[del_title]
    else:
        print("book not in catalog.")
       
def edit_book(books):
    title = input("Title: ")
    if title in books:
        author = input("Author name: ")
        year = int(input("Publication year: ")) 
        new_book = {'Author': author, 'Year': year}
        books[title] = new_book
        print(f"{title} was edited") 
    else:
        print("Book not in catalog.")
    
    
def main():
    books = {} 
    command_menu()
    while True:
        command = input("\ncommand: ")
        if command == 'show':
            show_book(books)
        elif command == 'add':
            add_book(books)
        elif command == 'edit':
            edit_book(books)
        elif command == 'del':
            del_book(books)
        elif command == 'exit':
            break
        else:
            print("Invalid selection.")
    print("\nBye!")
    
if __name__ == '__main__':
    main()



