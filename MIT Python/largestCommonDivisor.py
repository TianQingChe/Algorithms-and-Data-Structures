# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 17:01:11 2017

@author: XPS 13 9350
"""

def lcd_divide(a,b): 
    """
    辗转相除法iteratively
    """
    while a%b!=0:
        temp=b
        b=a%b
        a=temp
    return b
def lcd_recurse(a,b): 
    """
    辗转相除法recursively
    """
    if b==0:
        return a
    else:
        return lcd_recurse(b,a%b)
print(lcd_recurse(11,22))