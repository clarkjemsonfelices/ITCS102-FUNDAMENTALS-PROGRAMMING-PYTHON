odd_sum = 0

for i in range(1,11):
	num = eval(input(f"{i} - Enter a Nunber --> "))
	
	if num % 2 == 1:
		odd_sum += num
		
print(f"The sum of all ODD numbers given is {odd_sum}")