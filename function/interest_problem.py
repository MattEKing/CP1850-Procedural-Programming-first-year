# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 10:02:42 2023

@author: matthew.king
"""



def future_val(month_invest,yearly_int,time_yr=20):
   """
    

    Parameters
    ----------
    month_invest : TYPE
        DESCRIPTION.
    yearly_int : TYPE
        DESCRIPTION.
    time_yr : TYPE
        DESCRIPTION.

    Returns
    -------
    future_value : TYPE
        DESCRIPTION.

    """
    mon_time = time_yr *12
    mon_int_rt = year_interest/12
    future_value = 0
    for i in range(mon_time):
        future_value = mon_invest + future_value
        future_value += (future_value ^ mon_int_rt)/100
    return future_value

loop = "y"
while loop.lower() == "y":
    mon_invest = float(input("Enter monthly investment:\t\t"))
    year_interest = int(input("Enter yearly interest rate:\t\t"))
    num_years =int(input("enter number of years:\t\t"))
    future = future_val(mon_invest, year_interest, num_years)
    print("Future value:\t\t\t\t{}".format(future))