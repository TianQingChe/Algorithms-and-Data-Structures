# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 00:07:32 2017

@author: XPS 13 9350
"""

def genFib():
    fib_1=1
    fib_2=0
    while True:
        next=fib_1+fib_2
        yield next
        fib_2=fib_1
        fib_1=next