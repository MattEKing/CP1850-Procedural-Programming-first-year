# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 09:53:56 2023

@author: matthew.king
"""

def get_name():
    name = str(input("Enter full name:\t"))
    name_list = name.split()
    if len(name_list) > 1:
        return name_list
    else:
        print("you must enter your full name")
        get_name()
    
def get_password():
    uppercase = False
    digit = False
    while True:
        password = str(input('Enter password:\t'))
        if (len(password) < 8):
            print('Password Must be 8 characters or more')
        else:
            for i in password:
                if ord(i) >= 65:
                    uppercase = True
                elif ord(i) > 47 and ord(i) < 58:
                    digit = True 
            if uppercase == True and digit == True:
                return password      
            else:
                print('with at least one digit and one uppercase letter.')
                    

def main():
    name_list = get_name()
    get_password()
    print(f"Hi {name_list[0]}, thanks for creating an account.")
    
    
if __name__ == '__main__':
    main()