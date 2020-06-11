input=[1,2,3,4]
left_product=[1]*len(input)
right_product=[1]*len(input)
result=[]

for i,num in enumerate(input):
  if i==0:
    left_product[i]=1
  else:
    left_product[i]= left_product[i-1]*input[i-1] 
for j in range(len(input)-1,-1,-1):
  if j == len(input)-1:
    right_product[j]=1
  else:
    right_product[j]=right_product[j+1]*input[j+1]
print(left_product)
print(right_product)

for k in range(len(input)):
  result.append(left_product[k]*right_product[k])

print(result)