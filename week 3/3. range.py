# sequence

import sys
from cgitb import small

smallRange = range(10)
smallList = list(range(10))

bigRange = range(100)
bigList = list(range(100))

print("size of samllRange:{}".format(sys.getsizeof(smallRange)))
print("size of smallList:{}".format(sys.getsizeof(smallList)))
print("size of bigRange:{}".format(sys.getsizeof(bigRange)))
print("size of bigList:{}".format(sys.getsizeof(bigList)))

