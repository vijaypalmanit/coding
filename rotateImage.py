# Given an two dimensinal array of size N*N, rotate it colcokwise 90 degree, so that first row becomes the last column

arr = [[4,7,2],
       [5,9,1],
       [6,9,3]]
# To achieve the goal we will first transpose it along the primary diagonal

for i in range(len(arr)):
    for j in range(len(arr)):
        temp = arr[i][j]  
        arr[i][j] = arr[j][i] 
        arr[j][i] = temp
        print(arr)