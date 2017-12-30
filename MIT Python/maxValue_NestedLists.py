# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 12:55:49 2017

@author: XPS 13 9350
"""

def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    return max(all_values(t))
    
def all_values(t):
    lst=[]
    for ele in t:
        if type(ele)==int:
            lst.append(ele)
        else:
            lst.extend(all_values(ele))
    return lst
max_val([1,2,3,[1,7]])

            
                    