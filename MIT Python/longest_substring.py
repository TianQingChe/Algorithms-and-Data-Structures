# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
s = 'abcbcd'
ls=''
i=0
while i< len(s):
    temp=''
    start=i
    while i+1<len(s) and s[i]<=s[i+1]:
       i=i+1
    temp=s[start:i+1]
    if(len(temp)>len(ls)):
       ls=temp
    i=i+1
print('Longest substring in alphabetical order is: '+str(ls))

