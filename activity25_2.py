def factorial(num):
	result = 1
	for x in range(int(num), 0, -1):
		result *= x
	return result
	
def triangle(num):
	for i in range(1,int(num) + 1,1):
	for x in range(1,i,1):
		print("*",end=" ")
	print()
