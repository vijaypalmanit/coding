# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 16:37:47 2020

@author: Vijay
"""
#Given a 2D array of 1s and 0s, find the largest square subarray of all 1s.
#explanation https://www.youtube.com/watch?v=aYnEO53H4lw

import numpy as np
matrix=np.array([1,1,1,0,1,1,1,1,1,1,0,0]).reshape(3,4)

table = np.zeros(matrix.shape)

#lets populate this table first

result=1

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if i==0 or j==0:
            table[i,j]=matrix[i,j]
        elif matrix[i,j]==0:
            table[i,j]=0
          
        else:
            table[i,j] = min(matrix[i,j-1],matrix[i-1,j-1],matrix[i-1,j])+1
            if table[i,j]>result:
                result=table[i,j]
                
          
print(matrix)
print('-'*12)
print(table)            
print('largest submatrix size is: {}'.format(result))  