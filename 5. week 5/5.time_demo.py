import time

print(time.time())
print(time.gmtime(1658575345))
print('='* 40)
print(time.gmtime())
print(time.gmtime(0))
print('='* 40)
print(time.localtime(0))
print(time.localtime(1658575345))
print(time.localtime(1000000000))


