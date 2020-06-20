# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 23:15:13 2020

@author: Vijay
"""

inpt=[2,1,3,2,5,3,2]
seen=set()

for i in inpt:
    if i in seen:
        print("first duplicate value in list is: %d"%i)
        break
    seen.add(i)    
    
