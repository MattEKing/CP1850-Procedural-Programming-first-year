# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 08:46:16 2023

@author: matthew.king
"""

#files
#-text
#-binary

output_example = open("first_file.txt",'w')
# used to open a file 
output_example.write('This is my first file operation') 
output_example.close()
# write func used to add to file
# close func used to closse the file 

with open("first_file.txt",'w') as output_handle:
    output_handle.write("This is the second file operation")
# With will let you overwrite a file
   
with open("first_file.txt",'r') as output_handle:
    print(output_handle.readline())
# readline func will input line of file in console

with open("first_file.txt",'a') as outfile_handle:
    print(outfile_handle.write('We are doing the file module. \n'))
    
#reading files
with open("first_file.txt") as file_handle:
    for line in file_handle:
        print(line, end='')
    print()
   
with open("first_file.txt") as file_handle:
    content = file_handle.read()
    print(content)
# read will give the hole file as one string 

with open("first_file.txt") as file_handle:
    content_lines = file_handle.readlines()
    print(content_lines[1])
#readline will make the contents of the file a list

