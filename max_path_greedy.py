import numpy as np
A=[[12,4,19,32],
   [43,62,21,22],
   [53,47,88,23],
   [43,65,11,24]]
A=np.array(A)

t=['' for _ in range(16)]
route=np.array(t).reshape(4,4)
fm = np.array(['  ' for _ in range(16)]).reshape(4,4)

path=[12]
route[0][0]='+'
fm[0,0]=12
route[3][3]='+'
fm[3,3]=24
i,j=0,0

print('original matrix:\n\n',A)

while i <3 or j<3:
  if i==3:
    j+=1
    path.append(A[i][j])
    route[i][j]='+'
    fm[i,j]=A[i,j]

  if j==3:
    route[i][j]='+'
    fm[i,j]=A[i,j]
    i+=1
    path.append(A[i][j])
    

  if i !=3 or j!=3:
    right=A[i][j+1]
    bottom=A[i+1][j]

    if right > bottom:
      path.append(right)
      route[i][j]='+'
      fm[i,j]=A[i,j]
      j+=1
    else:
      path.append(bottom)
      route[i][j]='+'
      fm[i,j]=A[i,j]
      i+=1
  #print(path)
print('\nThe route is:\n')
print(route)
print('\route with values picked:\n')
print(fm)