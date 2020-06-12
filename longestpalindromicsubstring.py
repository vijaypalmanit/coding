# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 13:17:38 2020

@author: Vijay
"""

inpt= 'abaabaeabcba'
result=''
current_max_length=0

size =len(inpt)

def expandFromMiddle(left,right):
    while left>=0 and right<size and inpt[left]==inpt[right]:
        left-=1
        right+=1
    return (inpt[left+1:right],right-left+1)

for i in range(size):
    str1,len1 = expandFromMiddle(i,i)
    str2,len2 = expandFromMiddle(i,i+1)
    if current_max_length < max(len1,len2):
        current_max_length=max(len1,len2)
        if len1>len2:
            result=str1
        else:
            result=str2     
        
print(result)
