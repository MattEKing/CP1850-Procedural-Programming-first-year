# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 08:06:01 2023
~(8^(I))
@author: matthew.king
"""

print("The Test Scores Program \n")
print("Enter 3 test scores")
print("======================")

test1 = int(input("Enter test score: \t"))
test2 = int(input("Enter test score: \t"))
test3 = int(input("Enter test score: \t"))
total = test1 + test2 + test3 
print("======================")
print("total score: \t {}".format(total))
print("Average score: \t {:.0f}".format(total/3))
average = total/3 
if(average >= 90):
    print("Grade: A")
elif(average >= 80):
    print("Grade: B")
elif(average >= 60):
    print("Grade: C")
elif(average >= 40):
    print("Grade: D")
elif(average >= 0 and average <= 39):
    print("Grade: F")
else:
    print("ERROR")
print("\nBye!")

