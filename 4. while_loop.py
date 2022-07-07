# while loop
import statistics

# while <condition>: --> condition is a bool method
#   1-
#   2-
inputNumber = 0
# inputNumber = input()
# print(type(int(inputNumber)))
# while True:
#     try:
#         inputNumber = int(input("please enter an integer: "))
#         print("thank u")
#         break
#     except:
#         continue
#

# inputList = []
# whileCondition = True
# while whileCondition:
#     inputNumber = input("please inter an integer or q for quit:  ")
#     if inputNumber == 'q':
#         print("thank u")
#         break
#     try:
#         intNumber = int(inputNumber)
#         inputList.append(intNumber)
#         print("your mean is", statistics.mean(inputList))
#
#     except:
#         print("please enter an integer!!!")
#         continue


str1 = "1,2,3,"
sum = 0
position = 0
positionFirst = 0
positionSecond = 0
number = ''
# for char in str1:
#     if char in '0123456789.-' and char != ',':
#         number += char
#     else:
#         sum += float(number)
#         print(sum)
#         number = ''

# while True:
#     if char in '0123456789.-':


# print(sum)

# s = 0
# for num in str1.split(','):
#     s += float(num)
# print(s)

inp = input('heloo')
print(inp.isdecimal())