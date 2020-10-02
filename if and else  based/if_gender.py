name = input("enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")

if gender.lower() == "male":
	if age > 10:
		print("Hi! ",name," You should do swimming")
	else:
		print("Hi! ",name," You should play hide and seek")

elif gender.lower() == "female":
	if age > 10:
		print("Hi! ",name," You should play badminton")
	else:
		print("Hi! ",name," You should play hide and seek ")


