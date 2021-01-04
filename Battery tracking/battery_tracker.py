import tkinter as tk
from tkinter import messagebox
import time
import threading

    
def check_perc():
    with open("/sys/class/power_supply/BAT0/capacity") as batt_per:
        for line in batt_per:
            cap = line.strip()
        return cap

def check_status():
    with open("/sys/class/power_supply/BAT0/status") as batt_stat:
        for line in batt_stat:
            sts = line.strip()
        return sts

batt_percentage = check_perc()
batt_status = check_status()

max_batt_perc = 98
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

    if int(batt_percentage) > max_batt_perc and batt_status == "Charging" :
        root = tk.Tk()
        if flg_first_alert == True:
            alert_label = tk.Label(text="Alert! Battery charged. Please disconnect the charger!")
            flg_first_alert = False
        
        else:
            alert_label = tk.Label(text="Alert! Please disconnect the charger to avoid damaging the battery!")

        btn_ok = tk.Button(text="OK")
        btn_ok.bind("<Button-1>",lambda e: root.destroy())
        alert_label.pack()
        root.title('Warning: Battery Monitor by Chaitanya')
        btn_ok.pack()
       
        root.mainloop() 

    
    else:
        print("Charging insufficient. Alert not required")

    

    time.sleep(sleep_time)

    
    
    