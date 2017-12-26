# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 17:55:41 2017

@author: XPS 13 9350
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr)==1:
       return char==aStr
    if len(char)==0 or len(aStr)==0:
       return False
    index=len(aStr)//2
    com=aStr[index]
    if char==com:
       return True
    else:
       if char<com:
          return isIn(char,aStr[0:index])
       else:
          return isIn(char,aStr[index+1:len(aStr)])
