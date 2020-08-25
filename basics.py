name = input("What is your name?:")
age = int(input("What is your age?:"))
gender = input("what is your gender?:")

if gender == "male":
    if age < 6:
        print("Hi!",name,"You should do swimming")

    else:
        print("Hi!",name,"You should play hide n seek")

if gender == "female":
    if age < 6:
        print("Hi!",name,"You should play badminton")

      
    else:
        print("Hi!",name,"You should play hide n seek")  
