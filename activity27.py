print("Adding new title to the Dictionary")

anime = {}     # dictionary to store titles
loop = True

def search_title(key):      
    print("Searching....")
    if key in anime:
        print(f"Result: {anime[key]}")
    else:
        print("Key not found!")

def print_titles():
    for key, value in anime.items():
        print(f"Key: {key} Title: {value}")

while loop == True:
    key = input("Enter key to call the anime: ")
    title = input("Enter the new anime: ")

    anime[key] = title   # store in dictionary

    choice = input("Would you like to continue?\n""y - Yes\n" "n - No\n" "p - Print\n" "s - Search\n" "Typing..... ").lower()

    if choice == "y":
        print("Continuing...")
        continue

    elif choice == "n":
        print("Program Stops")
        break

    elif choice == "p":
        print("=========================")
        print_titles()
        print("=========================")
        continue

    elif choice == "s":
        search = input("Enter the key to search: ")
        search_title(search)
        continue

    else:
        print("Invalid Choice")