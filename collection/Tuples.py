# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 08:59:15 2023

@author: matthew.king
"""

#creating tuples
#syntax: tuples_name = (item1,item2,item3,....)

hits = (48.0,30.0,20.2,100.0)
fruits = ('apple','orange','banana','kiwi','grapes')
car = ('VW','jetta','2019','45.65')
#tuples are used for info that will not 
#change becasue you can't change tuple element

#Accesing element
fruits[3]
car[1]

#unpacking tuple to different variables 
mike, joe, ray,kla = hits

def tuple_example_fn():
    return 'mat', ['stud','program'], 2023

name, pos, year = tuple_example_fn()
test1 = tuple_example_fn()
test1[1][0] = "pro"
#you can not change elements in the tuple however you can change 
#parts of a list that are in a tuple.

#looping tuples
for fruits in fruits:
    print(fruits)
    
#most funtion work  the same as they do with list 