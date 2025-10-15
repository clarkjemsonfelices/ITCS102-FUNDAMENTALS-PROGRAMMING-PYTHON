name = input("Hi ! what is your name --> ")

print("+++++++++++++++++++++++++++++++++++++++++++")
print("ODD number compiler, Type '0' to terminate the loop")

loop = True
odd = 0
all =""

while loop == True:
	num = eval(input("Please input a number --> "))
	
	if num == 0:
		print("Loop Terminated")
		break
	elif num % 2 == 1:
		print("ODD Number detected")
		odd += num
		all += str(num) + ","
		continue 
	else:
		print("EVEN Number")
		continue
print(f"Hi {name}, The sum of all ODD number is {odd}")
print(f"All the ODD numbers you input is {all}")