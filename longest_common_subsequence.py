# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 13:34:20 2020

@author: Vijay
"""

import numpy as np
a='ABAB'
b='BABA'
mat =np.zeros((len(a),len(b)))
local_substring=''



for i in range(len(a)):
  for j in range(len(b)):
    if a[i]==b[j]:
      if i==0 or j==0:
          mat[i,j]=1
      else:
          mat[i,j]=mat[i-1,j-1]+1
      if mat[i,j] >= len(local_substring):         
          local_substring = a[int(i - mat[i,j]+1):i+1]
      print(f'longest common subsequence so far : {local_substring}')

          
print(mat)

