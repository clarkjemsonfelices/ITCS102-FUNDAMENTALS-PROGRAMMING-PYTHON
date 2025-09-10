print("Welcome to the Manga Reader Recommender!")
print("Answer a few questions to find your next read.")

genre = input("What genre do you like? \n(action, romance, horror): ").lower()
length = input("How long should the manga be? \n(short, medium, long): ").lower()
date = input("Which decade? (2000, 2010): ")

#Action
if genre == "action":
	if length == "short":
		if date == "2000":
			print("Recommendation: Black Lagoon")
		elif date == "2010":
			print("Recommendation: One Punch Man")
		else:
			print("Invalid decade, Please choose 2000 or 2010")
	elif length == "medium":
		if date == "2000":
			print("Recommendation: Fullmetal Alchemist")
		elif date == "2010":
			print("Recommendation: Attack on Titan")
		else:
			print("Invalid decade, Please choose 2000 or 2010")
	elif length == "long":
		if date == "2000":
			print("Recommendation: Bleach")
		elif date == "2010":
			print("Recommendation: My Hero Academia")
		else:
			print("Invalid decade, Please choose 2000 or 2010")
	else:
		print("Invalid length , Please choose short, medium, or long")

#Romance
elif genre == "romance":
	if length == "short":
		if date == "2000":
			print("Recommendation: Lovely Complex")
		elif date == "2010":
			print("Recommendation: Your Lie in April")
		else:
			print("Invalid decade, Please choose 2000 or 2010")
	elif length == "medium":
		if date == "2000":
			print("Recommendation: Fruit Basket")
		elif date == "2010":
			print("Recommendation: Your Name")
		else:
			print("Invalid decade, Please choose 2000 or 2010")
	elif length == "long":
		if date == "2000":
			print("Recommendation: Kimi ni Todoke")
		elif date == "2010":
			print("Recommendation: Domestic Girlfriend")
		else:
			print("Invalid decade, Please choose 2000 or 2010")
	else:
		print("Invalid length, Please choose short, medium, or long")

#Horror
elif genre == "horror":
	if length == "short":
		if date == "2000":
			print("Recommendation: Another")
		elif date == "2010":
			print("Recommendation: I Am a Hero")
		else:
			print("Invalid decade, Please choose 2000 or 2010")
	elif length == "medium":
		if date == "2000":
			print("Recommendation: Monster")
		elif date == "2010":
			print("Recommendation: Tokyo Ghoul")
		else:
			print("Invalid decade, Please choose 2000 or 2010")
	elif length == "long":
		if date == "2000":
			print("Recommendation: Parasyte")
		elif date == "2010":
			print("Recommendation: The Promised Neverland")
		else:
			print("Invalid decade, Please choose 2000 or 2010")
	else:
		print("Invalid length, Please choose short, medium, or long")
else:
	print("Invalid genre, Please choose action, romance, or horror")
