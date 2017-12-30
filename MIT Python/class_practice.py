# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 13:23:02 2017

@author: XPS 13 9350
"""
class Coordinate(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return '<'+str(self.x)+','+str(self.y)+'>'
    def distance(self,another):
        x_diff_sqr=(self.x-another.x)**2
        y_diff_sqr=(self.y-another.y)**2
        return (x_diff_sqr+y_diff_sqr)**0.5

c=Coordinate(3,4)
origin=Coordinate(0,0)
