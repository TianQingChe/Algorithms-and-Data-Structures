# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 19:16:42 2017

@author: XPS 13 9350
"""

print('Please think of a number between 0 and 100!')
print('Is your secret number 50?')
left=0
right=100
guess=50
s=input('Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.')
while s!='c':
    if s=='h':
      right=guess
      guess=(left+right)//2
      print('Is your secret number '+str(guess)+'?')
    elif s=='l':
      left=guess
      guess=(left+right)//2
      print('Is your secret number '+str(guess)+'?')
    s=input('Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.')
print('Game over. Your secret number was: '+guess)