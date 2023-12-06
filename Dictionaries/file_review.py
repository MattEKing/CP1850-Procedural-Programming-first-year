# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 08:57:42 2023

@author: matthew.king
"""

file_read_handle = open('class_review.txt', 'r')
read = file_read_handle.read()
file_read_handle.close()

with open('class_review.txt', 'r') as file:
    print(file)