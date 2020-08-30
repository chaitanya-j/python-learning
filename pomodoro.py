import time

t_orignal = int(input("For how hany minutes do you want to set your pomodoro timer?:"))
t = t_orignal

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
        print(f"{t}")
    print("Pomodoro over!!")
    v = input("Do you want more? yes/no:")
    if v == "no" or v == "NO" or v == "No":
        break
    



    

