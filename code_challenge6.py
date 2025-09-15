#Factorial Program
num = eval(input("Enter a Number --> "))
result = 1
for fac in range(num,0,-1):
	result *= fac
print("The Factorial of",num,"is",result)