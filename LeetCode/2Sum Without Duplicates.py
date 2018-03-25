# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 19:51:15 2018

@author: XPS 13 9350
"""
class Solution:
    def twoSum_no_duplicates(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        i=0
        j=len(nums)-1
        while i<j:
            temp=nums[i]+nums[j]
            if temp==target:
                    res.append([nums[i],nums[j]])
                    while i<j and nums[i]==nums[i+1]:
                        i+=1
                    while i<j and nums[j]==nums[j-1]:
                        j-=1
                    i+=1
                    j-=1
            elif temp<target:
                i+=1                
            else:
                j-=1
        return res
        
            
                
                
                