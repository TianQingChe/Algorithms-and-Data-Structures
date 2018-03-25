# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 01:07:25 2018

@author: XPS 13 9350
"""

class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        i=1
        length=1
        max_length=1
        while i<len(nums):
            if nums[i]>nums[i-1]:
                length+=1
            else:
                max_length=max(max_length,length)
                length=1
            i+=1
        return max(max_length,length)
            