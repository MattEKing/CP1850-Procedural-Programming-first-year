# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 08:46:35 2023

@author: matthew.king
"""
#starting lists 
#syntax
"""
    list_name = [ item1, item2, ...]
"""

movies = ["the Dark Knight", 2005, 9.99]
type(movies)
objects_list = [ 'sword','bats','cat']
flt_objects_list = [ 48.0, 88.0, 100.0,40.0]
empty_list_ex = []

scores = [0] * 10
flt_objects_list[0]
type(flt_objects_list[0])
type(movies[0])

flt_objects_list[-1] 
flt_objects_list[-4]
flt_objects_list[4]

# the values can be updated as long as the index is inputed.
flt_objects_list[2] = 'hello?'
flt_objects_list[3] = False
#append will add a value to the list.
movies.append(400)
#insert will add a value at a specific index.
movies.insert(2, "USA")
# value inputed will be removed from the list
movies.remove("USA")
# if value is not in the list this will cause a value error.
# pop will remove the last value in the list and returns it to the console.
flt_objects_list.pop() 
flt_objects_list.pop(1)
# giving pop an index will have it return and remove the value at the index.

i = objects_list.index("bats")
objects_list.pop(i)
# if the index is define with a vary after finding the index yuo can pop it for the list

len(movies)
# gives you the amount of object in the list

year = 2005
year in movies
year in objects_list

if (year in movies):
    movies.append("This is a awesome movie")
for item in movies:
    print(item)
    
scores = [70,80,90,100,60]
total = 0 
for scores in scores:
    total = total + scores
    print(total)
scores = [70,80,90,100,60]
total = 0 
i = 0
while i < len(scores):
    total = total + scores[i]
    i = i + 1 
print(total)
# enumerate will print the index value with the value 
for  j, item in enumerate(scores):
    print("{} - {}".format(j,item))

cars = ["VW", "Ford", "BMW", "Audi"]
prices = [30000,15000,40000,35000]
for car, prices in zip(cars, prices):
    print("{} - {}".format(car, prices))
# zip is used to combine two list 










