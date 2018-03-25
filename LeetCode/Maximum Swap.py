# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 15:08:52 2018

@author: XPS 13 9350
"""

class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str=str(num)
        num_lst=[]
        for s in num_str:
            num_lst.append(s)
        sort_lst=sorted(num_lst,reverse=True)
        flag=False
        
        for i in range(len(num_lst)):
            if num_lst[i]!=sort_lst[i]:
                j=num_str.rindex(sort_lst[i])
                num_lst[i],num_lst[j]=num_lst[j],num_lst[i]
                flag=True
                break
            
        if not flag:
            return num
        
        new_num_str=''.join(num_lst)
        return (int(new_num_str))
        
a=Solution()
print(a.maximumSwap(91238888))