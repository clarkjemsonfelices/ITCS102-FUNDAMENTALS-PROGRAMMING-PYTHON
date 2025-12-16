import random

num = random.randint(1,10)

tries = 0
loop = True

while loop == True:
    g = int(input("What number u guess(1-10): "))
    tries += 1

    if g == num:
        print("Congratulation")
        print(f"the number is {num}")
        print(f"You took {tries} tries")
        break

    else:
        print("Wrong! Try again.")
        continue