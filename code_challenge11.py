#Diamond
for i in range(1,11,1):
	for x in range(10, i, -1):
		print("",end=" ")
	for y in range(1, i, 1):
		print("*", end= " ")
	print()
for n in range(1,11,1):
	for a in range(1,n,1):
		print("",end=" ")
	for b in range(10,n,-1):
		print("*",end=" ")
	print()