# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 23:01:00 2018

@author: XPS 13 9350
"""

class Solution:
    def majorityElement(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for number in nums:
            if number not in dic:
                dic[number]=1
            else:
                dic[number]+=1
        t=len(nums)//2
        for k in dic.keys():
            if dic[k]>t:
                return k