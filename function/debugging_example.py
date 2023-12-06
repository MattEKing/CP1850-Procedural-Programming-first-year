# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 08:20:46 2023

@author: matthew.king
"""
def calculate_funture_value(monthly_investment,yearly_interest,years):
    #convert yearly values to monthly values
    monthly_interest_rate = (yearly_interest) /12 /100
    months = years * 12 
    #calculate future value
    future_value = 0.0
    for i in range(1,months + 1):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest  
    return future_value

print(calculate_funture_value(5, 5, 7))
    
#debugged from the example from the note.