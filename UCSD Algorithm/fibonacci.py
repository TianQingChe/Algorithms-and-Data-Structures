# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 20:52:29 2018

@author: XPS 13 9350
"""

def fibonacci(n):
    if n<=1:
        return n
    num1 = 0
    num2 = 1
    for i in range(2, n):
        temp = num2
        num2 = num1+num2
        num1 = temp
    return num1+num2


print(fibonacci(100))