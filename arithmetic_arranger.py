# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 16:16:10 2020

@author: Vijay
"""

inpt=["32 + 698","3801 - 2"]

inpt_cleaned=[]
num1=[]
num2=[]
operator=[]
for expr in inpt:
    inpt_cleaned.append(expr.split(" "))

for i in range(len(inpt_cleaned)):
    for j in range(len(inpt_cleaned[i])):
        if inpt_cleaned[i][j] not in ['+','-']:
            inpt_cleaned[i][j]=int(inpt_cleaned[i][j])
            if j==0:
                num1.append(inpt_cleaned[i][j])
            else:
                num2.append(inpt_cleaned[i][j])
        else:
            operator.append(inpt_cleaned[i][j])
            
#print(inpt_cleaned)
#print(num1)
#print(num2)
#print(operator)
to_print=[]
result=[]

for i,j,k in zip(num1,operator,num2):
    just=max(len(str(i)),len(str(k)))
    output='  '+str(i).rjust(just)+"\n"+j+' '+str(k).rjust(just)+'\n-----'
    to_print.append(output)
    print(output)
    if j=='+':
        result.append(i+k)
    else:
        result.append(i-k)
        