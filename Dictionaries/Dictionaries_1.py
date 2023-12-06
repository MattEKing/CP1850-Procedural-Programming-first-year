# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 08:34:26 2023

@author: matthew.king
"""

#creating dictionaries
#==========================================================
# dictionaries can intake all types of literals 
# you have to create a key to connect the name to it

countries = {'CA':'Canada',
             'US':'United states',
             'MX':'Mexico'}

movie = {'name': 'Robocop',
         'year': 1987,
         'price': 9.99}

country = countries['CA']
countries['CA'] = 'camaroon'

# dictionaries are mutable objects so they can be changed 
#=========================================================
# retrieving values for a particular key

country_code = 'MX'
if country_code in countries:
    country = countries[country_code]
    print(country)
else:
    print(f"No country for this code {country_code}")

country = countries.get('MX')
country = countries.get('IN', 'Unkown')

# the get func pull the string from its key code

#=======================================================

#delete a key value pair

del countries['CA']
del country, country_code
 
#del can delete any value

country = countries.pop('MX')
# when you use pop you have to give it a key were there is not indexs

movie.clear()
# clear will remove everything from the dictionaries selected

#=======================================================
# Accessing keys

countries.keys()
for code in countries.keys():
    print(f"{code}\t\t{countries[code]}")

# you can use keys() to find the keys for the dictionaries

for code2 in countries:
    print(f"{code2}\t\t{countries[code2]}")
# this will do the same thing as keys()

# Accessing values

countries.values()

for country in countries.values():
    print(country)

# Accessing both keys and values

countries.items()

for country_code, country in countries.items():
    print(f"{country_code}\t\t{country}")
# you can unpack the dictionary with this

# converting keys to a list
list(countries.keys())
list(countries.values())
list(countries.items())

# using the func keys or values you can create list for both

# Converting for a list

countries_list = [['GB','Britain'],
                  ['NL','netherlands'],
                  ['DE','Germany']]

dict(countries_list)
# using the dict func you can change a list into a dict










