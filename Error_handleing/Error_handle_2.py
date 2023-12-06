# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:52:36 2023

@author: matthew.king
"""

# handleing multiple errors in one function
#exceptions have a level such as a blanket can't go above a more 
# specific exception that needs to be specfied.

file_name = input("enter file name: ")
movies = []
try:
    with open(file_name) as file_handle:
        movies = file_handle.readlines()
except FileNotFoundError:
    print(f"Couldn't find the file named {file_name}")
except OSError as os:
    print('file is found. Error reading the file')
# you can find the type of error and display it.
    var = type(os)
    print(f"Type of OS error is {var}")
except Exception:
    print("Unexpected Error Occured")
    