# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:41:30 2019

@author: Vijay
"""

l = [6,2,9,11,9,3,7,12]
n=len(l)
def bubblesort(l,n):
    
    for i in range(len(l)-2):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
    if n>1:        
        bubblesort(l,n-1)   
    
bubblesort(l,n)
print(l)