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
    
hanoi(4,'A','B','C')
print(f'---------------------\ntotal move required here are :{total_move}')    
    
    

