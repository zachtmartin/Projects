# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 12:05:34 2017
Count number of steps to 1 using Collatz Conjecture
@author: zachtmartin
"""

n = input("What's the number?")
counts = int(0)
while n > 1:
    if (n % 2 == 0):
        n = n / 2
    else:
        n = n * 3 + 1
    counts += 1

print"It took" , counts , "iterations to get to 1."