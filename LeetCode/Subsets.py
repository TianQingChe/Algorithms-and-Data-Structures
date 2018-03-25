# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 15:13:05 2018

@author: XPS 13 9350
"""

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        r=[]
        search(nums,r,[],0)
        return r
    def search(self,nums,r,subset,index):
        r.append(subset)
        i=index
        while i<len(nums):
            subset.append(nums[i])
            search(nums,r,subset,i+1)
            subset.pop()
            i++