print("MULTIPLICATION TABLE MAKER")

num = eval(input("Enter a Number: "))
for x in range(1,11):
	result = num * x
	print(num, "*", x, "=", result)
