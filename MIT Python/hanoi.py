# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 16:31:22 2017

@author: XPS 13 9350
"""
def printMove(frm,to):
    print('Move from '+str(frm)+' to '+str(to))

def Towers(n,frm,to,spare):
    if (n==1):
        printMove(frm,to)
    else:
        Towers(n-1,frm,spare,to)
        Towers(1,frm,to,spare)
        Towers(n-1,spare,to,frm)
Towers(6,'1','3','2')
        