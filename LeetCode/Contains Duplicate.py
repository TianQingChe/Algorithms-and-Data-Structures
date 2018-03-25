# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 00:18:00 2018

@author: XPS 13 9350
"""

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic={}
        for num in nums:
            if num not in dic:
                dic[num]=1
            else:
                return True
        return False