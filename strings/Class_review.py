# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 08:19:42 2023

@author: matthew.king
"""

# csv file review
d2_array = [['Arun Rameshbabu','jsdfghj'],
            ['greg jones', 'qwertyui'],
            ['casey kim', 'zxcvbnm']]

import csv
#writing csv
# with open('passwords.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(d2_array)
    
# with open('passwords2.csv', 'w') as file2:
#     for row in d2_array:
#         string_to_write = row[0] + ',' + row[1] + '\n'
#         file2.write(string_to_write)
        
# reading csv
with open('passwords.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    struture = []
    for row in reader:
        struture.append(row)
        
with open('passwords.csv') as file2:
    lines = file2.readlines()
    stucture2 = []
    for line in lines:
        row = line.replace('\n', '').split(',')
        stucture2.append(row)