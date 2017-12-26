# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 17:24:52 2017

@author: XPS 13 9350
"""

def fibnacci(x):
    if x==0 or x==1:
        return 1
    else:
        return fibnacci(x-1)+fibnacci(x-2)