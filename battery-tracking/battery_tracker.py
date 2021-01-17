## This is a program which will track your battery and alert you if needed.
## I have seen many people's laptop's batterys going bad because of overcharging!
## This program will help, monitor and alert the user if the battery percentange is above 98 or less than 10 percent.
## If you want you can modify the percentages at which an alert shoulg be shown!!
## If you want, you can add this .pyffile to the .bashrc file. So, when you boot your laptop, the program will autostart!!!
## Hope you guys like this wonderfull program!
## Enjoy!!!


                    ####### PLEASE READ THE "README" FILE WHICH IS GIVEN WITH THE BATTERY TRACKER PACKAGE #######


import tkinter as tk
import time
import logging
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

logging_level = config.get('DEFAULT','logging_level')

if logging_level == 'DEBUG':
    logging_level = logging.DEBUG
elif logging_level == 'INFO':
    logging_level = logging.INFO
elif logging_level == 'WARNING':
    logging_level = logging.WARNING
elif logging_level == 'ERROR':
    logging_level = logging.ERROR

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "battery_tracker.log",
                    level = logging_level,
                    format = LOG_FORMAT,
                    )

logger = logging.getLogger()

def check_perc():
    '''
    This is a function which will check the current battery percentage of your device. There is a file with the following 
    path : "/sys/class/power_supply/BAT0/capacity" where the current battery percentage is stored.
    IMPORTANT : IF THIS IS NOT WORKING THEN, THE PATH WILL HAVE A MODIFICATION : IN THE PATH "/sys/class/power_supply/BAT0/capacity"
                IT WILL BE "BAT1" INSTEAD OF "BAT0"
    '''
    try:
        with open("/sys/class/power_supply/BAT0/capacity") as batt_per:
            for line in batt_per:
                cap = line.strip()
            logger.debug(f"<<<<>>>>{cap}")    
            return cap
    except Exception as e:
        logger.debug(f"Exeption occured while reading BAT0 capacity {e}")

def check_status():
    '''
    This is a function which will check the current battery status(it's charging or discharging) of your device. There is a file with the following 
    path : "/sys/class/power_supply/BAT0/status" where the current battery percentage is stored.
    IMPORTANT : IF THIS IS NOT WORKING THEN, THE PATH WILL HAVE A MODIFICATION : IN THE PATH "/sys/class/power_supply/BAT0/capacity"
                IT WILL BE "BAT1" INSTEAD OF "BAT0"
    '''
    try:
        with open("/sys/class/power_supply/BAT0/status") as batt_stat:
            for line in batt_stat:
                sts = line.strip()
            logger.debug(f"<<<<>>>>{sts}")    
            return sts

    except Exception as e:
        logger.debug(f"Exeption occured while reading BAT0 status {e}")    

batt_percentage = check_perc()
batt_status = check_status()

# Defining the max and min battery percentage
max_batt_perc = int(config.get('DEFAULT','max_batt_perc'))
sleep_time = int(config.get('DEFAULT','check_interval'))

logger.info('**************************************************************************************************')
logger.info(f'Config:logging_level = {logging_level}')
logger.info(f'Config:max_batt_perc = {max_batt_perc}')
logger.info(f'Config:check_interval = {sleep_time}')


flg_first_alert = True

root = tk.Tk()
alert_label = tk.Label(text="Battery monitor program started")
btn_ok = tk.Button(text="OK")
btn_ok.bind("<Button-1>",lambda e: root.destroy())
alert_label.pack()
root.title('Battery Monitor by Chaitanya')
btn_ok.pack()

root.mainloop()

logger.info('Starting the battery tracking program')

time.sleep(4)

while True:

    logger.info('Checking again...')
    batt_percentage = check_perc()
    batt_status = check_status()

    logger.debug(f'batt_percentage:{batt_percentage}')
    logger.debug(f'batt_status:{batt_status}')

    # This block of code will show messagebox if charging is above "98" and status is "Charging"
    if int(batt_percentage) > max_batt_perc and (batt_status == "Charging" or batt_status == "Full"):
        logger.info('Batter charged. Issuing alert')
        root = tk.Tk()
        logger.debug('root tkinter window created')
        if flg_first_alert == True:
            logger.debug('showing the first alert')
            
            alert_label = tk.Label(text="Alert! Battery charged. Please disconnect the charger!")
            flg_first_alert = False
        
        # If the user does not disconnect the charger even after alerting him once, there will be a different messagebox.
        else:
            logger.info('Charger still not disconnected. Issuing warning!')
            alert_label = tk.Label(text="Alert! Please disconnect the charger to avoid damaging the battery!")

        btn_ok = tk.Button(text="OK")

        # If the "OK" button in the messagebox is pressed, the root window will be destroyed.
        btn_ok.bind("<Button-1>",lambda e: root.destroy())
        alert_label.pack()
        root.title('Warning: Battery Monitor by Chaitanya')
        btn_ok.pack()
       
       # Starting the mainloop.
        logger.debug('starting main loop for the tkinter window')
        root.mainloop() 

    
    else:

        logger.info("Charging insufficient or charger is disconnected. Alert not required")

    

    time.sleep(sleep_time)

    
    
             ############################################## THANK YOU ##############################################