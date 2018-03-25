# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 13:41:43 2018

@author: XPS 13 9350
"""

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return -1
        low=0
        high=len(nums)-1
        cut=len(nums)-1
        while low<high:
            mid=(low+high)//2
            if nums[mid]>nums[mid+1]:
                cut=mid
                break
            else:
                if nums[mid]>nums[low]:
                    low=mid+1
                else:
                    high=mid
        if target>nums[0]:
            return self.bSearch(nums,0,cut,target)
        elif target<nums[0]:
            return self.bSearch(nums,cut+1,len(nums)-1,target)
        else:
            return 0
    def bSearch(self,nums,low,high,target):
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return -1