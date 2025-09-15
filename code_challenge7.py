#ODD number summation

result = 0
for x in range(1,11):
	num = eval(input("Enter a Number " + str(x)+ " : "))

	if num % 2:
		result += num
print("The sum of all odd numbers is",result)