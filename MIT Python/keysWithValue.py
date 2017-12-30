# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 12:45:18 2017

@author: XPS 13 9350
"""

def keysWithValue(aDict, target):
    '''
    input: aDict: a dictionary
           target: an integer
    return: returns a list of keys in aDict with the value target
            If aDict does not contain the value target, return an empty list    
    '''
    
    keys=[]
    for i in aDict.keys():
        if aDict[i]==target:
            keys.append(i)
    return sorted(keys)
    