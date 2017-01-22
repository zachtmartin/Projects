# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 16:47:59 2017
User determines how many digits to see e.
@author: zachtmartin
"""
from decimal import *
import math

n = input("How many digits (<100) would you like to see euler's number go to?")
if n > 100:
    n = 100

getcontext().prec = n + 1

def factorial(k):
    if k<1:
        return 1
    else:
        return k * factorial(k-1)

def euler():
    j = 1
    e = Decimal(1)
    while j < 100:
        e += Decimal(1) / factorial(j)
        j += Decimal(1)
    return e

print(euler())
