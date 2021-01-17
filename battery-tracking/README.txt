
Battery Tracker for Linux V1.0
Author: Chaitanya Jaipurkar
Rel Date: 17 Jan 2021
--------------------------------------------------

INSTALLATION INSTRUCTIONS:

1. Copy the battery-tracking utility to a suitable location on your machine
2. Install pyenv and then python v3.8+. If you are not sure how to do it, you may refer to this page https://realpython.com/intro-to-pyenv/
3. After successful installation, you should see the following output on your terminal:

demouser@computer:~$ pyenv versions
* system (set by /home/demouser/.pyenv/version)
  3.8.6

4. Provide executable permissions to the battery_tracker.sh
   chmod u+x batter_tracker.sh

5. Add an entry to your crontab by using the command crontab -e

@reboot /home/path/to/your-battery-tracker/battery-tracking/battery_tracker.sh>>~/battery_tracker.cron.log 2>&1

6. Reboot your machine. You should see a pop-up with message 'Batter tracker program started'. Click on the OK button and the program will continue in the background.
   The program will check your battery percentage and charging status at regular intervals and will issue you an alert to disconnect the charger if the battery is 
   charged more than 98%. It will issue you alerts every 2 mins if you do not disconnect. This is to protect your battery from getting damaged due to over-charging. 
   Once the charger is disconnected, the program will stop showing the alerts.

I hope that your will find this program helpful in increasing your battery life. In case you have any suggestions or you face any issues in using my program, please feel
free to raise an issue on my github repository.  

Note: The program configuration is in config.ini file. In my opinion, the configuration should be good for all systems. I advise not to change the configuration unless
there is a strong reason to do so. 

Supported config options:
- max_batt_perc: By default, the value is 98. This means, the program will issue an alert if the charging percentage goes beyond 98%. You may change the value to anything 
between 0 to 100
- check_interval: By default, the value is 120 i.e. 2 mins. The program checks the battery status and percentage after every 2 mins. If you want, you may change this to any 
positive integer value
- logging_level: By default, the program has INFO as the logging level. Other options are DEBUG, WARNING and ERROR
   