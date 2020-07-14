# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 23:59:30 2020

@author: Vijay
"""

total_move=0
def hanoi(n,frm,via,to):
    if n==0:
        pass
    else:
        hanoi(n-1,frm,to,via)
        
        global total_move
        print(f'{total_move+1}.move from {frm} --> {to}|')
        
        total_move+=1
        hanoi(n-1,via,frm,to)
    
hanoi(3,'A','B','C')
print(f'---------------------\ntotal move required here are :{total_move}')    
    
    

# 1   1
# 2   2+1
# 3   3+4
# 4   4+11

# n n+

# def move_hanoi_needed(n):
#     if n==0:
#         return n
#     return n + move_hanoi_needed(n-1)

# print(move_hanoi_needed(3))