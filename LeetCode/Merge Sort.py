
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 01:06:19 2018

@author: XPS 13 9350
"""

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.mergeSort(nums,0,len(nums)-1)
        
    def mergeSort(self,arr,l,r):
        if l<r:
            m=(l+r)//2
            self.mergeSort(arr,l,m)
            self.mergeSort(arr,m+1,r)
            self.merge(arr,l,m,r)

    def merge(self,arr,l,m,r):
        left=arr[l:m+1]
        right=arr[m+1:r+1]
        l_len,r_len=len(left),len(right)
        i,j,k=0,0,l
        while i<l_len and j<r_len:
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1

        while i<l_len:
            arr[k]=left[i]
            i+=1
            k+=1

        while j<r_len:
            arr[k]=right[j]
            j+=1
            k+=1
        
    