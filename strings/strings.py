# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 08:38:04 2023

@author: matthew.king
"""

# ord will return the acii value of a character.
ord('A')
ord('a')

# string properties
len('Arun')
# len will return the number of characters in that string

# string Access mthods

string1 = 'This is the CP1850 class'
len(string1)
string1[0]
string1[5]
string1[12]
# giving the index for a string will return the chaeacter in that
# postion as strings are a list if characters.
# you can not change characters in the string not mutable.

# slicing strings
string1[:3]
string1[12:18]
string1[12:]

# slicing will return multiple characters.
#syntax: string1[start:stop]
# the start and stop do not be input to work.

#multiline strings
query = '''SELECT name, value as CategoryValue
            FROM CategoryTable where name = ?'''
            
#checking for substrings in strings

'CP1850' in string1

if ('CP1850' in string1):
    print('Yes, substring exists.\n')
else:
    print('substring does not exist.\n')
    
# you can check within the string using an 'in' statement if something
#is in a string and you can make it a condisional.

#looping a string
for char in string1:
    print(char)
    
# strings can also be made in to a collection.

#some basic string functions
#check if is integer
user_entry = '2345'
user_entry.isdigit()

if (user_entry.isdigit()):
    print('This is a numeric value.\n')
else:
    print('This is not numeric.\n')
    
#checking if it begins with a specific substring
string1.startswith('This')
string1.endswith('class')    

# above will let you check that beginning and the end of the string

#tranformations

string1.lower()
string1.upper()
string1.capitalize()
string1.title()
# title will capitalize the start of every word in a string
string2 = '                 this is string 2'
string2.strip()
# strip will remove any random white space in the string

string1.replace('CP1850', 'CP4477')
user_entry.replace('.', '').isdigit()
user_entry.isnumeric()
# you can rerplace a substring with the 
#replace func by input old and new

email = 'matt.king@cnl.nl.ca'
email.removeprefix('matt.king')
email.removesuffix('@cnl.nl.ca')

# above functions will remove the beginning and end as given

#find elements

at_index = email.find('@')
email.removeprefix(email[:9])

# find will find where a character is in the string

#Splitting strings
string1.split()

# will break up the string into a list

string1.split('is')
date = '12/3/95'
date.split('/')

name = 'BMW 330i Turbo'
name.split(' ', 1)
splitted_string = string1.split()
'/'.join(splitted_string)
' '.join(splitted_string)




    
    







