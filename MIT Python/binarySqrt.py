# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:20:58 2017

@author: XPS 13 9350
"""
target=float(input('Enter a number: '))
accuracy=0.01
guess=target/2
if target==1 or target==0:
    guess=target
else:
    if target>1:
        left=0
        right=target
    else:
        left=target
        right=1
    while abs(guess**2-target)>=0.01:
        diff=guess**2-target
        if diff>0:
            right=guess
            guess=(left+right)/2
        elif diff<0:
            left=guess
            guess=(left+right)/2
print(guess)
