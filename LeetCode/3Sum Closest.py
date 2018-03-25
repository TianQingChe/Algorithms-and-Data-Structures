# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 22:06:42 2018

@author: XPS 13 9350
"""

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res=nums[0]+nums[1]+nums[2]
        diff=abs(res-target)
        for k in range(0,len(nums)-2):
            if k==0 or (k>0 and nums[k]!=nums[k-1]):
                i=k+1
                j=len(nums)-1
                while i<j:
                    temp_sum=nums[i]+nums[j]+nums[k]
                    temp_diff=temp_sum-target 
                    abs_temp_diff=abs(temp_diff)
                    if temp_diff==0:
                        return target
                    if abs_temp_diff<diff:
                        diff=abs_temp_diff
                        res=temp_sum
                        if temp_diff<0:                        
                            while i<j and nums[i]==nums[i+1]:
                                i+=1
                            i+=1
                        else:
                            while i<j and nums[j]==nums[j-1]:
                                j-=1
                            j-=1
                    else:
                        if temp_diff<0:
                            i+=1
                        else:
                            j-=1
        return res
                            