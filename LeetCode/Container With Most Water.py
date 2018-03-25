# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 14:47:17 2018

@author: XPS 13 9350
"""
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area=0
        left=0
        right=len(height)-1
        from math import *
        while left<right:
            area=max(area,(right-left)*min(height[left],height[right]))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return area
    


    def maxArea(self, height):
        left=0
        right=len(height)-1
        max_area=0
        from math import *
        while left<right:
            max_area=max(max_area,(right-left)*min(height[left],height[right]))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area
































