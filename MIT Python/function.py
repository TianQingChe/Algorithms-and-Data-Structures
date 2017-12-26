# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 21:52:08 2017

@author: XPS 13 9350
"""

def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)
a(3>2, a, b)

def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)
print(foo(1))
print(foo(1,2))