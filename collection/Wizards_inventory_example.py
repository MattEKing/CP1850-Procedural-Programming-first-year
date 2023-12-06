# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 08:10:57 2023

@author: matthew.king
"""

def title():
    print("The Wizard inventory Program")
    print()
    
def command_menu():
    print("COMMAND MENU")
    print("Show - Show all items")
    print("Grab - Grab an item")
    print("Edit - edit an item")
    print("Drop - Drop an item")
    print("Exit - Exit program")
    print()
    
def get_command(command_options:tuple):
    command = input("\nPlease enter a command: ")
    if command not in command_options:
        print("Invalid selection")
    command = command.lower()
    return command 
    
def show_inventory(inventory:list):
    for i, item in enumerate(inventory, start = 1):
        print("{}.{}".format(i,inventory[i - 1]))

def grab_item(inventory:list):
    if len(inventory) < 4:
        grab_item = input("Name: ")
        print(f"{grab_item} was added to inventory.")
        inventory.append(grab_item)
    else:
        print("You can't carry anymore items")
        
def edit_inventory(inventory:list):
    get_num = int(input("Number: ")) - 1
    if (get_num < 0) or (get_num + 1) > len(inventory):
        print("Invaild selection")
    else:
        new_name  = str(input("Updated name: "))
        inventory[get_num] = new_name
        print(f"Item {get_num + 1} was updated.")
    
def drop_item(inventory:list):
    get_num = int(input("Number: ")) - 1
    if (get_num < 0) or (get_num + 1) > len(inventory):
        print("Invalid selection")
    else:
        print(f"{inventory[get_num]} was dropped")
        inventory.pop(get_num)
    
def main():
    command_options = ("show","grab","edit","drop","exit")
    inventory = ["Wooden Staff","Wizard Hat","Cloth Shoes"]   
    title()
    command_menu()
    while True:       
        command = get_command(command_options)
        if command == "show":
            show_inventory(inventory)
        elif command == "grab":
            grab_item(inventory)
        elif command == "edit":
            edit_inventory(inventory)
        elif command == "drop":
            drop_item(inventory)
        elif command == "exit":
            break
    print("\nBye!")
        

if __name__ == "__main__":
    main()


    
    