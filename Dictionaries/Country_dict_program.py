# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 09:47:40 2023

@author: matthew.king
"""

countries = {'CA':'Canada',
             'US':'United states',
             'MX':'Mexico'}

def command_menu():
    print('COMMAND MENU')
    print('view - View country name')
    print('add  - Add a country')
    print('del  - Delete a country')
    print('exit - Exit program')
    
def view_country(countries):
    keys = list(countries.keys())
    keys.sort()
    codes_string = "Counrty codes: "
    for k in keys:
        codes_string += k + " "
    print(codes_string)
    code = input('Enter country code: ').upper()
    if code in countries:
        print(f'Country name: {countries[code]}')
    else:
        print("No country with this code.")
        
def add_country(countries):
    code = input('Enter country code: ').upper()
    if code in countries:
        name = countries[code]
        print(f"{name} is already using this code.")
    else:  
        name = input('Enter country name: ').capitalize()
        countries[code] = name
        print(f'{name} was added')
    
def delete_country(countries):
    code = input('Enter country code: ').upper()
    if code in countries:
        print(f"{countries[code]} was deleted")
        del countries[code]
    else:
        print("There is no country with this code.")
        
def main():
    command_menu()
    while True:
        command = input('\nCommand: ').lower()
        if command == 'view':
            view_country(countries)
        elif command == 'add':
            add_country(countries)
        elif command == 'del':
            delete_country(countries)
        elif command == 'exit':
            break
        else:
            print("invalid selection.")
    print("\nBye!")
if __name__ == '__main__':
    main()