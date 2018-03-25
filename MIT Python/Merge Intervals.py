# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 13:15:36 2018

@author: XPS 13 9350
"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List
        """
        if len(intervals)==0:
            return []
        intervals.sort(key=lambda inter:inter.start)
        rlist=[intervals[0]]
        i=0
        for inter in intervals:
            if inter.start<=rlist[i].end:
                new_inter=Interval(rlist[i].start,max(inter.end,rlist[i].end))
                rlist[i]=new_inter
            else:
                rlist.append(inter)
                i+=1
        return rlist