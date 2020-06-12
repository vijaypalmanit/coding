# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 14:10:04 2020

@author: Vijay
"""

inpt = 'aabfffeeebaa'
ans = 0

from collections import Counter

for v in Counter(inpt).values():
    ans+=(v//2)*2
    if ans%2==0 and v%2==1:
        ans+=1
        
print(ans)