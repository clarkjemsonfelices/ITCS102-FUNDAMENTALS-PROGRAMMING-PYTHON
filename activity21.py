
isClean = True

while isClean == True:
	ask = input("are the clothes clean already (y/n) --> ")
	
	if ask.lower() == 'y':
		print("loop continue")
		continue
	else:
		print("loop stops")
		break