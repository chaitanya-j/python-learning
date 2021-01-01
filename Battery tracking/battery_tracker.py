import tkinter as tk
from tkinter import messagebox
import time
import threading
from PIL import ImageTk,Image  

    
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



cnt = 1
batt_percentage = check_perc()
batt_status = check_status()


while True:
    print('Checking again...')
    if cnt != 1:
        batt_percentage = check_perc()
        batt_status = check_status()

    if int(batt_percentage) > 20 and batt_status != "Charging":
        root = tk.Tk()
        alert_label = tk.Label(text="Alert! Battery charged. Please disconnect the charger!")
        btn_ok = tk.Button(text="OK")
        alert_img = tk.Canvas(root,height=50,width=50)
        btn_ok.bind("<Button-1>",lambda e: root.destroy())
        alert_img.pack()
        img = ImageTk.PhotoImage(Image.open("alert2.png"))  
        alert_img.create_image(20,20,image=img)     
        alert_label.pack()
        btn_ok.pack()
        root.mainloop() 
        
    else:
        print("Charger not connected. Alert not required")

    

    time.sleep(120)
    cnt += 1

    
    
    