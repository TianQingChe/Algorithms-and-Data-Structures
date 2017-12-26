# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 21:55:58 2017

@author: XPS 13 9350
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    result=()
    for n in aTup[::2]:
       result+=(n,)
    return result
def f():
    oddTuples((1,2,3))
def s1(a):
    return a-1
    