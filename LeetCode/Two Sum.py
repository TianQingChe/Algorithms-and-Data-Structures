# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:23:55 2018

@author: XPS 13 9350
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            temp=target-nums[i]
            if temp in nums and nums.index(temp)!=i:
                return [i,nums.index(temp)]