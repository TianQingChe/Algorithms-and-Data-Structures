# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:51:51 2018

@author: XPS 13 9350
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1=len(nums1)
        len2=len(nums2)
        if (len1+len2)%2==1:
            k=(len1+len2+1)//2
            return self.findKSortedArrays(nums1,nums2,k)
        else:
            k1=(len1+len2)//2
            k2=k1+1
            return (self.findKSortedArrays(nums1,nums2,k1)+self.findKSortedArrays(nums1,nums2,k2))/2
        
    def findKSortedArrays(self,nums1,nums2,k):
        len1=len(nums1)
        len2=len(nums2)
        if len1==0:
            return nums2[k-1]
        elif len2==0:
            return nums1[k-1]
        mid1=len1//2
        mid2=len2//2
        if mid1+mid2>k-2: 
            if nums1[mid1]>nums2[mid2]:
                return self.findKSortedArrays(nums1[:mid1],nums2,k)
            else:
                return self.findKSortedArrays(nums1,nums2[:mid2],k)
        else:
            if nums1[mid1]<nums2[mid2]:
                return self.findKSortedArrays(nums1[mid1+1:],nums2,k-mid1-1)
            else:
                return self.findKSortedArrays(nums1,nums2[mid2+1:],k-mid2-1)


#findKSortedArrays([1,2,3,4],[1,2,3,4],5)
#findKSortedArrays([2,4,6,8,9],[1,3,6,11,20,25],5)
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    def findMedianSortedArrays(self, nums1, nums2):      
        len1=len(nums1)
        len2=len(nums2)
        total=len1+len2
        if total%2==1:
            k=(total+1)//2
            return self.findKSortedArrays(nums1,nums2,k)
        else:
            k1=total//2
            k2=k1+1
            return (self.findKSortedArrays(nums1,nums2,k1)+self.findKSortedArrays(nums1,nums2,k2))/2
            
    def findKSortedArrays(self,nums1,nums2,k):
        len1=len(nums1)
        len2=len(nums2)
        if len1==0:
            return nums2[k-1]
        elif len2==0:
            return nums1[k-2]
        mid1=len1//2
        mid2=len2//2
        if mid1+mid2>k-2:
            if nums1[mid1]>nums2[mid2]:
                return self.findKSortedArrays(nums1[:mid1],nums2,k)
            else:
                return self.findKSortedArrays(nums1,nums2[:mid2],k)
        else:
            if nums1[mid1]<nums2[mid2]:
                return self.findKSortedArrays(nums1[mid1+1:],nums2,k-mid1-1)
            else:
                return self.findKSortedArrays(nums1,nums2[mid2+1:],k-mid2-1)
                

        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        