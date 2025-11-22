import os
import json

os.system('cls')
print("STUDENT INFORMATION SYSTEM")
print("---------------------------")

student_records = {}

while True:
	print("SELECT FROM THE OPTIONS BELOW")
	print("A - Add Information")
	print("B - Print All Records")
	print("C - Search a Student Record")
	print("D - Delete a Student Record")
	print("E - Edit a Student Record")
	print("F - Export Record")
	print("G - Import Record")
	print("\nX - Exit")
	choice = input("Choice: ")
	#ADD INFORMATION
	if choice == 'a':
		os.system('cls')
		print("ADDING STUDENT INFORMATION")
		
		student_id = input("Key search for this student use this pattern (course-IDNO): ")
		
		first_name = input("Input Student First Name: ").upper()
		last_name = input("Input Student Last Name: ").upper()
		course = input("Input Student Course: ").upper()
		email = input("Input Student Email Address: ")
		
		student_records[student_id] = [first_name, last_name, course, email]
		print("DATA SAVED")
		
		os.system('cls')
		continue
		#PRINT ALL
	elif choice == 'b':
		os.system('cls')
		print("PRINTING STUDENT RECORD")
		
		for id, record in student_records.items():
			print(f"STUDENT ID {id} in STUDENT RECORD {record}")
		continue
		#SEARCH
	elif choice == 'c':
		os.system('cls')
		print("SEARCH STUDENT RECORD")
		
		search_id = input("Input ID to search: ").lower()
		
		for id in student_records.keys():
			if search_id in student_records.keys():
				print("--------------------------")
				print("\nSTUDENT RECORD FOUND\n")
				print("--------------------------")
				for i in student_records[search_id]:
					print(f"-- {i}")
			
			else:
				print("--------------------------")
				print("\nNO RECORD FOUND\n")
				print("--------------------------")
			break
		continue
		#DELETE A RECORD
	elif choice == 'd':
		os.system('cls')
			
		del_id = input("Input ID of Student to Delete: ").lower()
		
		if del_id in student_records.keys():
			print("--------------------------")
			print("\nSTUDENT RECORD FOUND\n")
			print("--------------------------")
			for i in student_records[del_id]:
				print(f"-- {i}")
			student_records.pop(del_id)
			print("RECORD DELETED")
			
		else:
			print("--------------------------")
			print("\nNO RECORD FOUND\n")
			print("--------------------------")
		continue
		#EDIT
	elif choice == 'e':
		os.system('cls')
			
		edit = input("Input ID of Student to Edit: ")
		if edit in student_records.keys():
			print("--------------------------")
			print("\nSTUDENT RECORD FOUND\n")
			print("--------------------------")
			for x, i in enumerate(student_records[edit]):
				print(f"{x} - {i}")
			
			choice = input("Choose what to change: ")
			#FIRST NAME
			if choice == '0':
				first_name = input("Input New Student First Name: ").upper()
				student_records[edit][0] = first_name
			#LAST NAME
			elif choice == '1':
				last_name = input("Input New Student Last Name: ").upper()
				student_records[edit][1] = last_name
			#COURSE
			elif choice == '2':
				course = input("Input New Student Course: ").upper()
				student_records[edit][2] = course
			#EMAIL
			elif choice == '3':
				email = input("Input New Student Email Address: ")
				student_records[edit][3] = email
			else:
				print("Invalid Choice")
			
			os.system('cls')
			print("DATA SAVED")
		else:
			print("--------------------------")
			print("\nNO RECORD FOUND\n")
			print("--------------------------")
		continue
		
	elif choice == 'f':
		os.system('cls')
		print("Export Student Record")
		
		with open('student_record.json', 'w') as new_file:
			json.dump(student_records, new_file, indent = 4)
		
		print("DATA EXPORTED TO JSON")
		continue
		
	elif choice == 'g':
		os.system('cls')
		print("Export Student Record")
		
		with open('student_record.json', 'r') as new_file:
			student_json = json.load(new_file)
		
		student_records = student_json
		print("DATA IMPORTED")
		continue
			
	elif choice == 'x':
		print("System Exits")
		break
		
	else:
		print("Invalid Choice")
		continue