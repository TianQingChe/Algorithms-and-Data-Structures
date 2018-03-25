# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 12:28:28 2018

@author: XPS 13 9350
"""

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length=len(height)
        if length<=2:
            return 0
        top=height.index(max(height))
        if top>=length-2:
            return self.left_trap(height[:top+1])
        elif top<=1:
            return self.right_trap(height[top:])
        else:
            return self.left_trap(height[:top+1])+self.right_trap(height[top:])
    def left_trap(self,height):
        low=0
        high=0
        temp=0
        water=0
        for i in range(len(height)):
            if height[i]>0:
                low=i
                high=i
                break;
        start=high
        for i in range(start,len(height)):
            if height[i]>=height[high]:
                if i!=high:
                    high=i
                    water+=(high-low-1)*height[low]-temp
                    temp=0
                    low=high
            else:
                temp+=height[i]
        return water
                         
    def right_trap(self,height):
        low=len(height)-1
        high=len(height)-1
        temp=0
        water=0
        for i in range(len(height)-1,-1,-1):
            if height[i]>0:
                low=i
                high=i
                break;
        start=high
        for i in range(start,-1,-1):
            if height[i]>=height[high]:
                if i!=high:
                    high=i
                    water+=(low-high-1)*height[low]-temp
                    temp=0
                    low=high
            else:
                temp+=height[i]
        return water