# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 23:20:00 2020

@author: Vijay
"""

inpt='civicll'

buffer=set()

for i in inpt:
    if i in buffer:
        buffer.remove(i)
    else:
        buffer.add(i)
        
if len(buffer)<=1:
    print('Yes it is possible palindrome')
else:
    print('No it is not possible palindrome')    