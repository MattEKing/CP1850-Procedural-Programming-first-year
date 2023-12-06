# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 08:30:54 2023

@author: matthew.king
"""

import random 
help(random)

#random function
#float 0.0 and 1.0
number1 = random.random() * 100
print(number1)

# The randint() function
# int in the range you specilfy
# syntax randint(min,max)
number2 = random.randint(1,100)
print(number2)

number3 = random.randint(281, 300)
print(number3)

# The randrange() function
# int in the range that you specify 
# syntax randrange([start,]stop[,step])
number4 = random.randrange(1,100)
print(number4)
number5 = random.randrange(100,200,2)
print(number5)
number6 = random.randrange(11, 220,2)
print(number6)

