# two arrays and on target is given, return true if sum of two numbers (one from each array) from given array is equal to target.

def sumOfTwo(a,b,target):
	for i in a:
		if target-i in b:
			return True
	return False
	
a=[5,8,9,2,3]
b=[99,-10,3]
target= -7

print(sumOfTwo(a,b,target))
	
	
	
	status=active from subscription
	
	store_id/gateway_config