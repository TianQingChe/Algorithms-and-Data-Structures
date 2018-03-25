# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 18:10:37 2018

@author: XPS 13 9350
"""

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        left=1
        temp=nums[0]
        for i in range(len(nums)):
            res.append(left)
            left*=nums[i]
        right=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=right
            right*=nums[i]
        return res