# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 01:25:46 2018

@author: XPS 13 9350
"""

class Interval:
     def __init__(self, s=-1, e=-1):
         self.start = s
         self.end = e

class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        interval_list=[]
        for lst in matrix:
            interval=self.maximalInterval(lst)
                interval_list.append(interval)
        for lst in interval_list:
            
    def maximalInterval(self,lst):
        i=0
        n=0
        inter=Interval()
        for j in range(len(lst)):
            if lst[j]=='1':
                if j-i+1>n:
                    n=j-i+1
                    inter.start=i
                    inter.end=j
            else:
                i=j+1
        return inter