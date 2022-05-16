# -*- coding: utf-8 -*-
"""
Created on Sun May  8 08:43:58 2022

@author: ercru
"""

p1=(-4,-2)
p2=(1,5)

#print(p1[0]);print(p1[1])

def fn(y,p2,p1):
    a=(p2[1]-p1[1])/(p2[0]-p1[0])
    b=y-p1[0]
    return a*b+p1[1]

print(fn(3.7,p2,p1))
