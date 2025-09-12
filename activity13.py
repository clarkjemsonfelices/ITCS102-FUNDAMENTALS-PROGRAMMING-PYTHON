result = 0
for n in range(1,11):
	num = eval(input(f"Enter a Number({n}): " ))
	result += num
print("The Sum of all numbers is", result)