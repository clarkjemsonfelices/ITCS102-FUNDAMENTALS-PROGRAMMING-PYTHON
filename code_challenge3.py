from getpass import getpass

name = input("Enter username --> ")
password = getpass("Enter password --> ")

setname = "clark"
setpass = "secret123"

if (name.lower() == setname) and (password.lower() == setpass):
	print("'Access granted'")
else:
	print("'Access denied'")