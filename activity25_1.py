def activity1():
	print("Hello World")
	
def activity2():
	name = input("What is Your Name .? ")
	print("Hi",name,"Welcome to the Matrix.")
	
def odd_sum():
	for i in range(1,11):
		num = eval(input(f"{i} - Enter a Nunber --> "))
		if num % 2 == 1:
		odd_sum += num
	print(f"The sum of all ODD numbers given is {odd_sum}")
