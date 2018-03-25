# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 20:40:08 2018

@author: XPS 13 9350
"""

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result=[]
        order=len(digits)-1
        number=0
        for i in digits:
            number+=i*(10**order)
            order-=1
        number+=1
        str_number=str(number)
        for j in str_number:
            result.append(int(j))
        return result
def plusOne(digits):
    for i in range(len(digits)-1,-1,-1):
        if digits[i]==9:
            digits[i]=0
        else:
            digits[i]+=1
            return digits
    digits.insert(0,1)
    return digits