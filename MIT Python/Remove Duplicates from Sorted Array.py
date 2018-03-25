# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 11:57:44 2018

@author: XPS 13 9350
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        for j in range(len(nums)):
            if nums[j]!=nums[i]:
                i+=1
                nums[i]=nums[j]
        return i