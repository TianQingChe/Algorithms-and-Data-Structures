# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 23:30:08 2017

@author: XPS 13 9350
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp==0:
      return 1
    return base*recurPower(base,exp-1)