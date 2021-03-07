from datetime import datetime

lst_reminder_times = []
reminder_recipients = {}

def register_for_reminder(func,dttime):
    now = datetime.today()
    if dttime < now:
        raise Exception('Sorry, reminder time needs to be ahead than the current time')
    else:
        if dttime not in lst_reminder_times:
            lst_reminder_times.append(dttime)
        else:
            print('Entry already exists for this time. Not adding a new one')

        lst_recipients = reminder_recipients.get(dttime)
        if lst_recipients != None:
            if func not in lst_recipients:
                lst_recipients.append(func)
        else:
            reminder_recipients[dttime] = []
            reminder_recipients[dttime].append(func)

    lst_reminder_times.sort()
    print('list of reminder times:',lst_reminder_times)
    print('reminder recipients:',reminder_recipients)


    
