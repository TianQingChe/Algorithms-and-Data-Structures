# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 12:37:14 2017

@author: XPS 13 9350
"""

def count7(N):
    '''
    input: N: a non-negative integer
    return: the number if 7 in that integer
    '''
    if N==7:
      return 1
    if N==0:
      return 0
    if N%10==7:
      return 1+count7(N//10)
    else:
      return count7(N//10)