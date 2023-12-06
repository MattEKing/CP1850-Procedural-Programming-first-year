# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 08:36:24 2023

@author: matthew.king
"""

#The reduce function
import functools

num_lists = [1,2,3,4,5,6]

def squared(tot_val, current):
    return tot_val + (current * current)

#list comprehension advanced
import random

def get_num():
    return random.randint(1, 10)

squares = [(num * num) for n in range(10) if (num := get_num()) <= 6]


