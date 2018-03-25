# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 18:26:37 2018

@author: XPS 13 9350
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        max_profit=0
        low=prices[0]
        high=prices[0]
        for i in prices:
            if i>high:
                high=i
            if i<low:
                low=i
                high=i
            max_profit=max(max_profit,high-low)
        return max_profit