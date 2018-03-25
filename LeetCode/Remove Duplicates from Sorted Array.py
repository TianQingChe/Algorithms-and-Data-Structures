# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 17:34:23 2018

@author: XPS 13 9350
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=0
        while j<len(nums):
            while j<len(nums)-1 and nums[j+1]==nums[j]:
                j+=1
            