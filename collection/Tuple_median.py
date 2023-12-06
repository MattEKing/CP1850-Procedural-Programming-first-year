# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 09:17:56 2023

@author: matthew.king
"""
import random
 
 
def get_num():
    return random.randrange(1,50)

def get_tuple(length):
    return tuple([get_num() for i in range(length)])

def get_list(length):
    return [get_num() for i in range(length)]

def get_average(collection):
    average = sum(collection)/len(collection)
    return average

def get_max(collection):
    maxi = max(collection)
    return maxi

def get_min(collection):
    mini = min(collection)
    return mini

def get_median(collection):
    length = len(collection)
    if length % 2 == 0:
        indexes = [len(collection//2)]
    else:
        indexes = [len/2, (len//2) + 1]
    sorted_collection = sorted(collection)
    median = None
    for i in indexes:
        median += sorted_collection[i]
    median = median / len(indexes)
    return median

def get_dups(collection):
    dup = []    
    for i in collection:
        count = collection.count(i)
        if (count > 1) and (count not in dup):
            dup.append(i)
    return dup
 

tuple_1 = get_tuple(11)            
print("Tuple Data: ".format(tuple_1))
print(f"Average = {get_average(tuple_1)} Median = {get_median(tuple_1)} Min = {get_min(tuple_1)} Max = {get_max(tuple_1)} Dups = {get_dups(tuple_1)}")
    
    
# def main():
    
    
    
    
    
    