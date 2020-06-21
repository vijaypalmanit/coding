# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 23:58:47 2020

@author: Vijay
"""

inpt=[1,2,4,6,7,9]



find=4

def binSearch(arr):
    mid=len(arr)//2
    if find==arr[mid]:
        return mid
    elif find< arr[mid]:
        return binSearch(arr[:mid])
    else:
        return binSearch(arr[mid+1:])
        
print(binSearch(inpt))        