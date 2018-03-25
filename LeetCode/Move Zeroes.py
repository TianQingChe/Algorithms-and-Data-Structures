# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 17:21:10 2018

@author: XPS 13 9350
"""

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_count=nums.count(0)
        non_zero_count=len(nums)-zero_count
        nums_copy=nums[:]
        zeroes=[]
        for i in nums_copy:
            if i==0:
                nums.remove(0)
                zeroes.append(0)
        nums.extend(zeroes)
    
    def moveZero_best(self,nums):
        zero=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[zero]=nums[zero],nums[i]
                zero+=1