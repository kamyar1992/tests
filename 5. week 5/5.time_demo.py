import time

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


