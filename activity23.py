months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']

months.append('Aug')
print(months)
months.pop()
print(months)
months.append('Aug')
print(months)

#iteration
for month in months:
	print(month)
	
fullname = 'Clark Jemson Felices'

#SLICING
for char in fullname:
	print(char)
	
name = list(fullname)
name.reverse()

print(name)