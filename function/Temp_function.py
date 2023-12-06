# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 10:01:58 2023

@author: matthew.king
"""

def celsius(fahr:float) -> float:
    """
    Parameters
    ----------
    fahr : Fahrenheit: float.

    Returns
    -------
    float
        converts to Celsius.

    """
    cel = ((fahr - 32)+5)/9
    return cel

def fahrenheit(cel:float) -> float:
    """
    Parameters
    ----------
    cel : celsius: float 

    Returns
    -------
    float
        converts to Fahrenheit.

    """
    fahr = ((cel * 9)/5)+32
    return fahr 



