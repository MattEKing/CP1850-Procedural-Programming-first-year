# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 09:58:29 2023

@author: matthew.king
"""

subtotal = float(input("enter the subtotal "))

tax_percent = float(input("enter the tax percent "))

tax_amount = subtotal * tax_percent

total = tax_amount + subtotal
print(total)