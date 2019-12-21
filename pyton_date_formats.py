# Python - Fun with Dates

from datetime import timedelta
from datetime import datetime

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
print("Date Entered = " + date_entered.strftime("%x"))
for each_format in formats:
    print(date_entered.strftime("date_entered.strftime(\'%%"+ each_format + "\') = %"+each_format))