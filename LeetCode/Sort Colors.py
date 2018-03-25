# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 13:37:17 2018

@author: XPS 13 9350
"""

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        slower=0
        faster=0
        while faster<len(nums):
            if nums[faster]==0:
                nums[faster]=nums[slower]
                nums[slower]=0
                slower+=1
            faster+=1
        faster=slower
        while faster<len(nums):
            if nums[faster]==1:
                nums[faster]=nums[slower]
                nums[slower]=1
                slower+=1
            faster+=1
