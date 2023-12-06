# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:02:50 2023

@author: matthew.king
"""

# Example of deep copy mehtod
#-----------------------------------------------------
list1 = [1,2,3,4,5]
list2 = list1
list2[1] = 4

import copy 
cp_list1 = [1,2,3,4,5]
cp_list2 = copy.deepcopy(cp_list1)
cp_list2[1] = 4
# deep copy you import copy to copy 
list_1 = [1,2,3,4,5]
list_2 = list_1.copy()
list_2[1] = 4
# formated copy will shallow copy the list

slice_example = [20,21,22,23,24,25,26,27]
slice_example[0:2] 
slice_example[:2]
slice_example[4:]
#slice will let you call lists by index so you can call multiple values
 
slice_example[0:6:2]
# stop index not inclued and last number is the step 
slice_example[::-1]
#negative with reverse the list 
slice_example[6:2:-1]

concat_example = slice_example + list1
# concat is used for adding list together

# map method
#----------------------------------------------------

def square(n):
    return n*n
square_list_1 = map(square, list_1)
list(square_list_1)
#map will change a list in to a map that can't be call 
#list will unpack that map 

#filter method
#------------------------------------------------------
def even_number(n):
    return n%2 == 0
evens = filter(even_number,slice_example)
a = list(evens)

#list comp
#------------------------------------------------------

b = [x*x for x in list1]
# using square bracket you can write what output you want 
#and for what list you want t opull from










