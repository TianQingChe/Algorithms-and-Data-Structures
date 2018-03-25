# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 23:45:48 2018

@author: XPS 13 9350
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit=0
        length=len(prices)
        if length==0:
            return profit
        valley=prices[0]
        peak=prices[0]
        i=0
        while i<length-1:
            while i<length-1 and prices[i+1]<=prices[i]:
                i+=1
            valley=prices[i]
            while i<length-1 and prices[i+1]>=prices[i]:
                i+=1
            peak=prices[i]
            max_profit+=(peak-valley)
        return max_profit
    
    def maxProfit(prices):
        length=len(prices)
        if length==0:
            return 0
        
        max_profit=0
        valley=prices[0]
        peak=prices[0]
        i=0
        while i<length:
            while i<length-1 and prices[i+1]<=prices[i]:
                i+=1
            valley=prices[i]
            while i<length-1 and prices[i+1]>=prices[i]:
                i+=1
            peak=prices[i]
            max_profit+=peak-valley
        return max_profit
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    