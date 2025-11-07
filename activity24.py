def greet(name):
	print(f"Hi {name}, How are you?")

def factorial(num):
	result = 1
	for x in range(num, 0, -1):
		result *= x
	print(f"The factorial of {num} is {result}")

greet("Tom")
greet("Jerry")
factorial(5)