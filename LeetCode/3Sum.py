# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 20:01:18 2018

@author: XPS 13 9350
"""

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        for k in range(0,len(nums)-2):
            if k==0 or (k>0 and nums[k]!=nums[k-1]):
                target=0-nums[k]
                i=k+1
                j=len(nums)-1
                while i<j:
                    temp=nums[i]+nums[j]
                    if temp==target:
                        res.append(nums[k],nums[i],nums[j])
                        while i<j and nums[i+1]==nums[i]:
                            i+=1
                        while i<j and nums[j-1]==nums[j]:
                            j-=1
                        i+=1
                        j-=1
                    elif temp<target:
                        i+=1
                    else:
                        j-=1
        return res
