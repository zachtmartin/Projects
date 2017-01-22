# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 16:47:59 2017
lists 1 to 100 and replaces multiples of 3 with Fizz and 5 with Buzz and both with FizzBuzz
@author: zachtmartin
"""

i = 1

while i <= 100:
	if i % 3 == 0 and i % 5 == 0:
		print("FizzBuzz")
	elif i % 3 == 0:
		print("Fizz")
	elif i % 5 == 0:
		print("Buzz")
	else:
		print(i)
	i += 1