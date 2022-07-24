# def <functionName>(parameters):
    # 1-
    # 2-
    # 3-

def temp():
    print('inside temp function')

def temp2():
    print('inside temp2 function')
    return 'this is temp2 function'
print(temp())
print('=' * 40)
temp()
print('=' * 40)
print(temp2())
print(temp2)  # repr(): return identity address
print(type(temp2))

# print():
# 1- str()
# 2- repr()

def adder(a, b, c=1 , d=2):  # parameters
    return a + b + c + d


# non-default arguments ==> positional arguments
# default arguments ==> keyword arguments
addedNumbers = adder(1, 2, 3, 5)  # arguments
print(addedNumbers)
print(adder(1, 2))
print(adder(1, 2, 4))
print(adder(1, 2, d=4))
print(adder(3, 3, c=1, d=1))
print(adder(a=1, d=1, b=1, c=1))

print('=' * 40)
print(1, 2, 3, sep='@@', end='%%%')
