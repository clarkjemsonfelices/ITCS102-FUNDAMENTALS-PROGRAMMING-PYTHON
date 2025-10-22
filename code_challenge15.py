anime = []
while True:
	title = input("Enter the title of an anime (or type 'exit to finish): ")
	
	if title.lower() == 'exit':
		print("You have exited the the anime entry program.")
		break
	else:
		anime.append(title)
		continue
print("Your anime list includes:")
for a in anime:
	print(f"- {a}") 