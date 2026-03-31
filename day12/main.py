import datetime
print(dir(datetime))



from datetime import datetime
now = datetime.now()
print(now)
day = now.day
print(day)
month = now.month
print(month)

year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day,month,year,hour,minute)
print("timestamp", timestamp)
print(f"[{day}/{month}/{year}, {hour}:{minute}:{second}]")

from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%y, %H:%M:%S")
print("time one:", time_one) 
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
print("time two:", time_two)

from datetime import time

a= time ()
print("a=",a)
b = time ( 10, 30, 50)
print("b = ", b)
c = time(hour=10, minute=30, second=50)
print("c= ", c)


from datetime import date , datetime
today = date(year=2026, month = 3, day = 31)
new_year = date(year=2027, month = 1, day= 1)
time_left_for_newyear = new_year - today
print("time left for new year : ", time_left_for_newyear)

#Get the current day, month, year, hour, minute and timestamp from datetime module
#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
from datetime import datetime 
now = datetime.now().strftime("%m/%d/%y, %H:%M:%S")
print("current date and time : ", now)
