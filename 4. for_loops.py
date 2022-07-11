# for <iterator> in <iterabel objec>:
#     1-
#     2-
#     3-
#
# in : means subset
alphabetString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(sorted(alphabetString, reverse=True))

for char in alphabetString:
    if char in "qKaz":
        break
    if char in "CFHG":
        continue
    print(char)
print('=' * 40)
# else: for for
for char in alphabetString:
    if char in "qaz":
        break
    if char in "CFHG":
        continue
    print(char)
else:
    print("if 'for' loop does not 'break' else will excute")
print('=' * 40)
#prime numbers
def prime(numberFrom, numberTo):
    primeNumber = []
    for number in range(numberFrom, numberTo):
            for x in range(2 , number-1):
                if number % x == 0:
                    break
            else:
                if number !=1:
                    primeNumber.append(number)
    return primeNumber

print(prime(1,1000))
print('=' * 40)
alphaString = 'abcdef'
for number, char in enumerate(alphaString, start=1):
    print(number, char)

print('=' * 40)
for num in filter(lambda x: x in 'aBCdEF', alphabetString):
    print(num)


print('=' * 40)
numberList = [1,2,3,4,5,6,7,8,9,10]
def s(x):
    return x**x
for num in sorted(numberList,key=s):
    print(num)
print('=' * 40)
for num1 in  reversed(list(map(s, numberList))):
    print(num1)


print('=' * 40)
for i in range(6,-1,-2):
    print(i)
print('=' * 40)
for odd, even in zip(range(1,10,2),range(0,10,2)):
    print(f'{even}, {odd}')
print('=' * 40)
for x in reversed(range(1,10)):
    print(x)

# even odd alphabe
for even, odd in zip(alphabetString[::2],alphabetString[1::2]):
    print(even, odd)

print(alphabetString[-1:-26:-1])

numberString = "1, -0.5, 3.5,0.23"
sum = 0
number = ''
for char in numberString:
    if char == ',':
       sum += float(number)
       number = ''
    else:
        number += char
else:
    sum += float(number)
print(sum)










