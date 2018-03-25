# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 20:34:35 2018

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
        last_pair=[]
        while i<j:
            temp=nums[i]+nums[j]
            if temp==target:
                if nums[i] not in last_pair:
                    res.append([nums[i],nums[j]])
                    last_pair=[nums[i],nums[j]]
                    i+=1
                    j-=1
                else:
                    i+=1
            elif temp<target:
                i+=1                
            else:
                j-=1
        return res
    