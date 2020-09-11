import time

t_orignal = int(input("For how hany minutes do you want to set your pomodoro timer?:"))
t = t_orignal

# Function to start and execute the pomodoro cycle
def start_pomodoro():
    # Re-assign the variable t to the original user input value
    # Warning: Else, the value will stay 0 and it will enter an infinite loop
    t = t_orignal

    # Gave condition as true to the loop.
    while True:
        time.sleep(60)

        # After each passing minute the  no of minutes will be reduced by 1.
        t -= 1

        # When t will become 0 break or else the loop will go on forever.
        if t == 0:
            # Very important to break here. Or else the pomodoro cycle will continue for ever!
            break
        
        # Printing the no of minutes after every 60 seconds.
        print(f"{t} minutes to go")
    print("Pomodoro over!!")


# Function to get the user choice for pomodoro repeat
def read_usr_choice():
    while True:
        # Asking do you want one more round of pomodoro?
        v = input("Do you want more? y/n:")

        # If user says no we break he loop.
        if v == "n" or v == "N":
            print("Thanks for using my program!! Bye!")

            # We need to exit the whole program. So break will not help
            exit()

        elif v == "y" or v == "Y":
            break

        else:
            print("Invalid Input! Please try again")

# Check if the user has entered a positive value (in minutes) for the pomodoro cycles
if t > 0:
    # Gave condition as true to the loop, so it will go on forever unless we break it.
    while True:

        start_pomodoro()
        read_usr_choice()

# User has not provided a positive value. This will lead to an infinite loop.
# Ask the user to enter the value again
else:
    print("Invalid input! Please enter a value greater than zero")

        

