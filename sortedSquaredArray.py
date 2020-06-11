inpt = [-6, -4, 1, 2, 3, 5]
rslt = [0 for i in inpt]
left = 0
right = len(inpt) - 1

for k in range(right, -1, -1):
    if abs(inpt[left]) > inpt[right]:
        rslt[k] = inpt[left]**2
        left += 1
    else:
        rslt[k] = inpt[right]**2
        right -= 1
print(rslt)
