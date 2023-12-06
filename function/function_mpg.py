# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 08:59:59 2023
~(8^(I))
@author: matthew.king
"""



loop = "y"

def calc_mpg(miles_driven, gallons_fuel):
    """
    This function calculates and returns miles per galllon

    Parameters
    ----------
    miles_driven : float or int
        number of miles driven.
    gallons_fuel : float or int
        gallons of fuel used.

    Returns
    -------
    mpg : float
        miles per gallon.

    """
    mpg = miles_driven/gallons_fuel
    return mpg
if __name__ == "__main__":
    
    while loop.lower() == "y":
        print("The Miles Per Gallon Program \n") 
    
        miles = float(input("Enter miles driven: \t \t"))
        gallon = float(input("Enter Gallons of gas used: \t"))
        c_mpg = calc_mpg(miles, gallon)
        if (gallon <= 0):
            print("gallons used must be greater then zero. Try again. ")
        else:
            print(c_mpg)
    
        contin = input("Calculate again? (y/n):")
    
        if contin.lower() == "n":
            break
    print("\nBye!")

