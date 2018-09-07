from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

today = date.today();
print("Today date is: " + today.strftime("%A %d of %B, %Y"))

time = datetime.time(datetime.now())
print("The time is: " + time.strftime("%I:%M:%S %p"))

now = datetime.now();
print("All together this exact moment is:\n" 
        + now.strftime("%A %d of %B, %Y at %I:%M:%S %p"))

delta = timedelta(days = 10)
inTenDays = today + delta
print("In " + str(delta.days) +  " days it is going to be: " + inTenDays.strftime("%A %d of %B, %Y"))

birthday = date(today.year, 12, 4);
daysTillBday = birthday - today
if (daysTillBday.days < 0):
    print("This year my birthday has already passed, but next year is going to be in:")
    birthday = birthday.replace(year = (today.year + 1))
    print("%d days!"  % (birthday - today).days)
elif (daysTillBday.days == 0):
    print("Congratulations today is your birthday!")
else:
    print("My next birthday is going to be in")
    print("%d days!"  % (birthday - today).days)
