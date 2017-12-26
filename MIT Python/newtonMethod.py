# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 21:42:16 2017

@author: XPS 13 9350
"""

num=0.01
epsilon=0.001
guess=12.5
while abs(guess*guess-num)>=epsilon:
    guess=guess-(guess**2-num)/(2*guess)
print(guess)
