# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 12:44:55 2018

@author: XPS 13 9350
"""
from math import *
class Solution:
#    dynamic programming
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum=nums[0]
        lst=[nums[0]]
        for i in range(1,len(nums)):
            lst.append(max(lst[i-1]+nums[i],nums[i]))
            max_sum=max(max_sum,lst[i])
        return max_sum
#    divide and conquer
    
            
            