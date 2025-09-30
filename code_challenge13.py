#diamond
for i in range(1,6,1):
	for s in range(1,6,1):
		print(" ",end=" ")
	for x in range(5,i,-1):
		print(" ",end=" ")
	for y in range(1,i,1):
		print("*",end=" ")
	for z in range(i,2,-1):
		print("*",end=" ")
	print()
for i in range(1,4,1):
	for s in range(1,6,1):
		print(" ",end=" ")
	for x in range(1,i + 1,1):
		print(" ",end=" ")
	for y in range(4,i,-1):
		print("*",end=" ")
	for z in range(3,i,-1):
		print("*",end=" ")
	print()
#Triangle 1
for i in range(1,6,1):
	for s in range(1,5,1):
		print(" ",end=" ")
	for x in range(5,i,-1):
		print(" ",end=" ")
	for y in range(0,i,1):
		print("*",end=" ")
	for z in range(i,1,-1):
		print("*",end=" ")
	print()
#Triangle 2
for i in range(1,8,1):
	for s in range(1,3,1):
		print(" ",end=" ")
	for x in range(7,i,-1):
		print(" ",end=" ")
	for y in range(0,i,1):
		print("*",end=" ")
	for z in range(i,1,-1):
		print("*",end=" ")
	print()
#Triangle 3
for i in range(1,10,1):
	for x in range(9,i,-1):
		print(" ",end=" ")
	for y in range(0,i,1):
		print("*",end=" ")
	for z in range(i,1,-1):
		print("*",end=" ")
	print()
#Rectangle
for i in range(1,10,1):
	for x in range(1,6,1):
		print(" ",end=" ")
	for y in range(1,8,1):
		print("*",end=" ")
	print()