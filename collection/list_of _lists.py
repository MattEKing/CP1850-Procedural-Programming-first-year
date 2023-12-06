# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 08:41:07 2023

@author: matthew.king
"""

instructors = [["Arun", "cool", "top class", "VW", 2020],
               ["unhappy guy", "tardy", "cancel class", 2021],
               ["homer", "guy", "good", 2022]]

instructors[0][3]
instuctor = ["brad", "cool",2024]
instructors.append(instuctor)
print(instructors)

for instuctor in instructors:
    for element in instuctor:
        print(element, end = ' | ')
    print()