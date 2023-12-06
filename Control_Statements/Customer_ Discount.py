# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 09:45:17 2023

@author: matthew.king
"""
print("Customer Discount \n")

print("======================")

customer_type = input("Enter customer Type (R or W): ")

invoice_total = float(input("Invoice Total \t \t \t \t  "))

if(customer_type.lower() == "r"):
    if(invoice_total < 250):
        discount_percent = 0
        
    elif(invoice_total >= 250):
        discount_percent = .2
        
elif(customer_type.lower() == "w"):
    discount_percent = .4
    
else:
    print("customer type must be R or W.")


discount = (invoice_total * discount_percent)
total = (invoice_total - discount) 

print("======================")

print("Invoice total: \t \t{}".format(invoice_total))
print("Total price: \t \t{}".format(total))
print("Discount percent: \t{}".format(discount_percent))
print("Discount amount: \t{}".format(discount))

print("\nbye!")
    

    