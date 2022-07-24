# python has several time modules:
# time, datetime and calendar

import datetime
print(datetime.date.today())
print(type(datetime.date.today()))
print('=' * 40)

today = datetime.date.today()
threeWeeksFromNow = datetime.timedelta(weeks=3)
print(today + threeWeeksFromNow)

# .strftime(): https://docs.python.org/3/library/datetime.html?highlight=datetime#strftime-and-strptime-behavior

nowDate = datetime.datetime.now()
print(nowDate.strftime("%Y"))
print(nowDate.strftime("%M"))
print(nowDate.strftime("%h"))

print('=' * 40)
import pytz  # pytz is a package that enable us to make datatime module time aware
print(type(pytz.country_names))  # as you can see this is a dictionary
# for tz in pytz.country_names:
#     print(tz, pytz.country_names[tz])
print(type(pytz.country_timezones))  # as you can see this is a dictionary
# for tz in pytz.country_timezones:
#     print(tz, pytz.country_timezones[tz])

print(type(pytz.all_timezones))  # it is some kind of lists
for tz in pytz.all_timezones:
    print(tz)







