import time

t_orignal = int(input("For how hany minutes do you want to set your pomodoro timer?:"))
t = t_orignal

if t > 0:
    # Gave condition as true to the loop, so it will go on forever unless we break it.
    while True:
        t = t_orignal
        # Gave condition as true to the loop.
        while True:
            time.sleep(1)

            # After each passing minute the  no of minutes will be reduced by 1.
            t -= 1

            # When t will become 0 break or else the loop will go on forever.
            if t == 0:
                break
            
            # Printing the no of minutes after every 60 seconds.
            print(f"{t} minutes to go")
        print("Pomodoro over!!")

        while True:
            # Asking do you want one more round of pomodoro?
            v = input("Do you want more? y/n:")

            # If user says no we break he loop.
            if v == "n" or v == "N":
                print("Thanks for using my program!! Bye!")
                exit()
    
            elif v == "y" or v == "Y":
                break

            else:
                print("Invalid Input! Please try again")

else:
    print("Invalid input! Please enter a value greater than zero")

        

