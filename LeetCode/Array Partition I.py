# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 21:53:38 2018

@author: XPS 13 9350
"""

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        nums.sort()
        for i in range(0,len(nums),2):
            result+=nums[i]
        return result