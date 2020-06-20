# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 22:51:05 2020

@author: Vijay
"""

inpt = [[0,1,0,0],
        [1,1,1,0],
        [0,0,1,0],
        [0,1,0,1]]

n_island=0

def explore_island_boundary(i,j):
    while i<len(inpt) and i>=0 and j < 4 and j>=0 and inpt[i][j]==1:
        inpt[i][j]=0
        explore_island_boundary(i,j-1) # go left
        explore_island_boundary(i,j+1) # go right
        explore_island_boundary(i-1,j) # go up  
        explore_island_boundary(i+1,j) # go down

for i in range(len(inpt)):
    for j in range(4):
        if inpt[i][j]==1:
            n_island+=1
            explore_island_boundary(i,j)
print(f'total island are: {n_island}')            