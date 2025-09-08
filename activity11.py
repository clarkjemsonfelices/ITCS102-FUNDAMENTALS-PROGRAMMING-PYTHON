temp = eval(input("Enter Temperature --> "))

if temp < 1:
	print("Temperature Outside is Freezing Cold")
elif temp >= 1 and temp <= 20:
	print("Temperature Outside is Cold")
elif temp >= 21 and temp <= 30:
	print("Temperature Outside is Lukewarm")
elif temp >= 31 and temp <= 40:
	print("Temperature Outside is Warm")
elif temp >= 41 and temp <= 50:
	print("Temperature Outside is Hot")
elif temp >= 51:
	print("Temperature Outside is Boiling Hot")
else:
	print("Invalid Temperature ")