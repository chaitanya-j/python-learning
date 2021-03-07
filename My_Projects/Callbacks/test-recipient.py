import reminder
from datetime import datetime
from datetime import timedelta

curr_time = datetime.today()
print('Current time is ', curr_time)

reminder_time1 = curr_time + timedelta(hours=3)
reminder_time2 = curr_time + timedelta(hours=1)

print('Calling the reminder module to wake up after 3 hours. i.e. at', reminder_time2)

# Notify function to be passed to the reminder registration
def notify(msg):
    print('Received notification:', msg)

try:
    reminder.register_for_reminder(notify, reminder_time1)
    reminder.register_for_reminder(notify, reminder_time2)
    reminder.register_for_reminder(notify, reminder_time2)
    
except Exception as e:
    print('Exception occurred:', e)