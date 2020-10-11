# Python - Fun with Dates

from datetime import timedelta
from datetime import datetime
import time

starttime = time.perf_counter()
endtime = time.perf_counter()
print(f"Runtime: {endtime - starttime:0.4f} seconds")

day=5
month=12
year=1933
test_date = str(month) + "/"+ str(day) + "/" + str(year)
test_date = datetime.strptime(test_date,'%m/%d/%Y')
current_date = datetime.now()

# current_date = current_date.replace(minute=0, hour=0, second=0, microsecond=0)
formats = "a A w d b B m y Y H I p M S f z Z j U W c x X G u V"
formats = formats.split(' ')
date_entered = current_date
print("Python Date Formats")
print("https://docs.python.org/3/library/datetime.html")
print("Date Entered = " + date_entered.strftime("%x"))
for each_format in formats:
    print(date_entered.strftime("date_entered.strftime(\'%%"+ each_format + "\') = %"+each_format))




from datetime import datetime

ts = int("1284101485")
print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))

ts = 1591026207404
ts = int(str(ts)[:10])
str(datetime.utcnow().timestamp())[:10]

ts = int(str(datetime.utcnow().timestamp())[:10])
print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))

timestamp = datetime.utcfromtimestamp(ts).strftime('%Y%m%d-%H%M%S')

def ts():
   ts = int(str(datetime.utcnow().timestamp())[:10])
   ts = datetime.utcfromtimestamp(ts).strftime('%Y%m%d-%H%M%S')
   return ts


