# python has several time modules:
# time, datetime and calendar

import datetime
print(datetime.date.today())
print(type(datetime.date.today()))
print('=' * 40)

today = datetime.date.today()
threeWeeksFromNow = datetime.timedelta(weeks=3)
print(today + threeWeeksFromNow)

