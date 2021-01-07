## This is a program which will track your battery and alert you if needed.
## I have seen many people's laptop's batterys going bad because of overcharging!
## This program will help, monitor and alert the user if the battery percentange is above 98 or less than 10 percent.
## If you want you can modify the percentages at which an alert shoulg be shown!!
## If you want, you can add this .pyffile to the .bashrc file. So, when you boot your laptop, the program will autostart!!!
## Hope you guys like this wonderfull program!
## Enjoy!!!

import tkinter as tk
import time

    
def check_perc():
    '''
    This is a function which will check the current battery percentage of your device. There is a file with the following 
    path : "/sys/class/power_supply/BAT0/capacity" where the current battery percentage is stored.
    IMPORTANT : IF THIS IS NOT WORKING THEN, THE PATH WILL HAVE A MODIFICATION : IN THE PATH "/sys/class/power_supply/BAT0/capacity"
                IT WILL BE "BAT1" INSTEAD OF "BAT0"
    '''
    with open("/sys/class/power_supply/BAT0/capacity") as batt_per:
        for line in batt_per:
            cap = line.strip()
        return cap

def check_status():
    '''
    This is a function which will check the current battery status(it's charging or discharging) of your device. There is a file with the following 
    path : "/sys/class/power_supply/BAT0/status" where the current battery percentage is stored.
    IMPORTANT : IF THIS IS NOT WORKING THEN, THE PATH WILL HAVE A MODIFICATION : IN THE PATH "/sys/class/power_supply/BAT0/capacity"
                IT WILL BE "BAT1" INSTEAD OF "BAT0"
    '''
    with open("/sys/class/power_supply/BAT0/status") as batt_stat:
        for line in batt_stat:
            sts = line.strip()
        return sts

batt_percentage = check_perc()
batt_status = check_status()

# Defining the max and min battery percentage
max_batt_perc = 98
min_batt_perc = 10
sleep_time = 120

flg_first_alert = True

root = tk.Tk()
alert_label = tk.Label(text="Battery monitor program started")
btn_ok = tk.Button(text="OK")
btn_ok.bind("<Button-1>",lambda e: root.destroy())
alert_label.pack()
root.title('Battery Monitor by Chaitanya')
btn_ok.pack()

root.mainloop()

while True:

    print('Checking again...')
    if flg_first_alert == False:
        batt_percentage = check_perc()
        batt_status = check_status()

# This block of code will show messagebox if charging is above "98" and status is "Charging"
    if int(batt_percentage) > max_batt_perc and batt_status == "Charging" :
        root = tk.Tk()
        if flg_first_alert == True:
            alert_label = tk.Label(text="Alert! Battery charged. Please disconnect the charger!")
            flg_first_alert = False
        
        # If the user does not disconnect the charger even after alerting him once, there will be a different messagebox.
        else:
            alert_label = tk.Label(text="Alert! Please disconnect the charger to avoid damaging the battery!")

        btn_ok = tk.Button(text="OK")

        # If the "OK" button in the messagebox is pressed, the root window will be destroyed.
        btn_ok.bind("<Button-1>",lambda e: root.destroy())
        alert_label.pack()
        root.title('Warning: Battery Monitor by Chaitanya')
        btn_ok.pack()
       
       # Starting the mainloop.
        root.mainloop() 

    if batt_status == "Discharging":
        flg_first_alert = True

# This block of code will show messagebox if charging is below "10" and status is "Discharging"
    if int(batt_percentage) < min_batt_perc and batt_status != "Charging" :
        root2 = tk.Tk()    
        alert_label = tk.Label(text="Alert! Charging very low, please connect the charger!!!")
        button_ok = tk.Button(text="OK")

        # If the "OK" button in the messagebox is pressed, the root window will be destroyed.
        button_ok.bind("<Button-1>",lambda e: root2.destroy())
        alert_label.pack()
        root2.title('Warning: Battery Monitor by Chaitanya')
        button_ok.pack()
        root2.mainloop()


        

    
    else:
        print("Charging insufficient. Alert not required")

    

    time.sleep(sleep_time)

    
    
             ############################################## THANK YOU ##############################################