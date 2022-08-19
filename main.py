# This is a sample Python script.
import numpy as np
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# rc = 0
# counter = 0
# lst1 = []
# while rc - 81:
#     row = rc // 9
#     col = rc % 9
#
#     si = col // 3 if row < 3 else 3 + col // 3 if row < 6 else 6 + col // 3 if row < 9 else None
#     lst1.append(si)
#     rc += 1
# new_list = []
# print(len(lst1))
# for i in lst1:
#     print(i, end='')

grid = np.zeros((3, 3), dtype=int)
print(grid.tolist()[0][0])


