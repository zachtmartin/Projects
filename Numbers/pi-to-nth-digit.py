# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 16:47:59 2017
Calculates pi to user defined decimal point.
@author: zach
"""
from decimal import *

n = input("How many decimal places (<100) would you like to see pi? ")
if n > 100:
    n = 100
getcontext().prec = n + 1

def factorial(j):
    if j<1:
        return 1
    else:
        return j * factorial(j-1)

def pi():
    """
    Calculates and returns pi using the Chudnovsky method 
    http://en.wikipedia.org/wiki/Chudnovsky_algorithm
    """    
    p = Decimal(0)
    k = 0
    while k < 163: #Limited iterations to 163 due to maximum recursion depth on factorial function.
        p += (Decimal(-1)**k)*(Decimal(factorial(6*k))/((factorial(k)**3)*(factorial(3*k)))* (13591409+545140134*k)/(640320**(3*k)))
        k += 1
    p = p * Decimal(10005).sqrt()/4270934400
    p = p**(-1)    
    print(p)
    return 
    
pi()
