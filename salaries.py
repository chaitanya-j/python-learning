# Creating an empty list
sal = []

# Made a continuous While Loop
while True:

    # Asking user to enter the salary
    i = input("Do yo want to add any salary? y/n :")

    # If user enters 'y' or 'Y' it will execute the statement after that 
    if i == "y" or i == "Y":
        i2 = input("Please enter the salary:")

        # Using the "try" method to catch the error thown by the function int(), and thus preventing it from crashing.
        try:
            i2_input_int = int(i2)

            # Adding the perfect int in the list, sal
            sal.append(i2_input_int)

        except ValueError:
            print("Please enter a number! Please Try Again!")
    
    if i == "n" or i == "N":
        sal.sort()
        print(sal)
        print("Second Highest Salary: ",sal[-2])        
        break

print("Thank You for using my program!")
        