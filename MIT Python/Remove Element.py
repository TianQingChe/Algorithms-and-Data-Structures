# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 15:48:28 2018

@author: XPS 13 9350
"""
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        """
        j marks first diff, faster pointer
        i marks first same, slower pointer
        """
        i=0
        j=0
        while j<len(nums):
            if nums[j]!=val:
               nums[i]=nums[j]
               i+=1
            j+=1
        return i
        