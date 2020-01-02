# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:43:19 2019

@author: Vijay
"""

n=5
i=1
def table(k,i):
    print(k*i)
    if i!=10:
        table(k,i+1)
table(n,i)  