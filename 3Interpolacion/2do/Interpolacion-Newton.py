# -*- coding: utf-8 -*-
"""
Created on Sun May  8 10:37:41 2022

@author: ercru
"""

p0=(2,1.43)
p1=(3.2,2.79)
p2=(4,3.56)

def fn1(p0,p1):
    a=(p1[1]-p0[1])/(p1[0]-p0[0])
        
    return a

print(fn1(p0,p1))

def fn2(p0,p1):
    b=(((p2[1]-p1[1])/(p2[0]-p1[0]))-((p1[1]-p0[1])/(p1[0]-p0[0])))/(p2[0]-p0[0])
    return b


print(fn2(p0,p1))

def fn3(x,p0,p1,):
    c=p0[1]+(fn1(p0, p1)*(x-p0[0]))-(fn2(p0, p1)*((x-p0[0])*(x-p1[0])))
    return c
print(fn3(3.6,p0,p1))


