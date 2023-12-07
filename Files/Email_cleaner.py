# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 09:08:26 2023

@author: matthew.king
"""

import csv

def title():
    print('Welcome to the Email List Cleaner\n')
    
def read_file(FILENAME):
    prospect_list = []
    with open(FILENAME) as rpf:
        reader = csv.reader(rpf)
        for line in reader:
            prospect_list.append(line)
    return prospect_list

def write_file(CLEANFILE, prospect_list):
    with open(CLEANFILE, 'w', newline= '') as wpf:
        writer = csv.writer(wpf)
        writer.writerows(prospect_list)

def clean_file(prospect_list):
    for i, line in enumerate(prospect_list):
        prospect_list[i][0] = prospect_list[i][0].title()
        prospect_list[i][1] = prospect_list[i][1].title()
        prospect_list[i][2] = prospect_list[i][2].lower()
        
def main():
    title()
    FILENAME = str(input('Source list: '))
    CLEANFILE= str(input('Clean list: ')) 
    prospect_list = read_file(FILENAME)
    clean_file(prospect_list)
    write_file(CLEANFILE, prospect_list)
    print(f'\n{FILENAME} as cleaned') 
    
if __name__ == '__main__':
    main()