import time
#  https://www.timeanddate.com/time/international-atomic-time.html
print(time.time())
print(time.gmtime(1658575345))
print('=' * 40)

print(time.gmtime())
print(time.gmtime(0))
print('=' * 40)

print(time.localtime(0))
print(time.localtime(1658575345))
print(time.localtime(1000000000))

print('=' * 40)
print(time.gmtime(2147483648))  # when 32 bits system will stop working
# print(time.gmtime(2305843009213693952))  # when 64 bits system will stop working
print('=' * 40)

timeList = ['monotonic', 'perf_counter', 'process_time', 'thread_time', 'time']
for clock in timeList:
    print('clock info for {}: {}'.format(clock, time.get_clock_info(clock)))
    print('---------------------')

print('=' * 40)

tehranTime = time.localtime()
print(tehranTime)
print('{}, {}, {} \t {}, {}, {}'.format(tehranTime.tm_mday,
                                        tehranTime.tm_mon,
                                        tehranTime.tm_year,
                                        tehranTime.tm_hour,
                                        tehranTime.tm_min,
                                        tehranTime.tm_sec))




