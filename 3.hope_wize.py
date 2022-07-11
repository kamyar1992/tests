# for number in range(1,101):
#     if not number%15:
#         print(number, "   hop-wize")
#     elif not number%3:
#         print(number, '   hop')
#     elif not number%5:
#         print(number, "   wize")
#     else:
#         print(number)
# for number in range(1, 101): print("hop-wize" if not number % 15 else "hop" if not number % 3 else "wiz" if not number % 5 else number)
# https://peps.python.org/pep-0308/

for number in range(1, 101):
    print("hop-wize" if number in range(0,101, 15) else "hop" if number in range(0,101,3) else "wiz" if number in range(0,101,5) else number)

import os
import sys