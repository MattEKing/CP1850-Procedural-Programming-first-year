# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 09:11:33 2023

@author: matthew.king
"""

num_list = [1,1,2,3,4,5,6,7,8,9,10,11,12]

num_list.count(1)
# count the number of element that are the same.

fruits = ['apple','apple','apple','apple','apple','apple','Orange']

fruits.count('orange')

num_list.reverse()
print(num_list)
# used to reverse the original list.

fruits.reverse()
fruits

num_list.sort()
# sorts all list element in A-Z or numercial and also sorts caps 
#before lowers.

fruits.sort(key = str.lower)
fruits
# can and .lower to opmite caps in the list.

sorted(fruits)
#will sort the list but doesn't change the original.

max(num_list)
# shows  the largest value in the list
min(num_list)
#show the smallest value in the list
sum(num_list)
#adds up all the numbers in the list
sum(num_list, start = 200)
#also can add a starting value to add to.