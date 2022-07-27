# def <functionName>(parameters):
    # 1-
    # 2-
    # 3-

def temp():
    print('inside temp function')


def temp2():
    print('inside temp2 function')
    return 'this is temp2 function'


def number_adder(*args, spt=":", ind = 1):
    sum_value = 0
    for num, index in enumerate(args, ind):
        print('{} {} {}'.format(index, spt, num))
        sum_value += num
    return sum_value


def adder(a, b, c=1 , d=2):  # parameters
    return a + b + c + d


if __name__ == "__main__":  # *important : this is executable part of our code
    print(temp())           # *important : without executable part of our code when you import a module to another
    print('=' * 40)         # module and run the destination module it runs imported module
    temp()
    print('=' * 40)
    print(temp2())
    print(temp2)  # repr(): return identity address
    print(type(temp2))

    # print():
    # 1- str()
    # 2- repr()

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
    print(1, 2, 3, sep='@@', end='%%%\n')  # *important end= is very important you can omit \n to understand
    print('=' * 40)

    # * ==> unpack a tupel

    print(number_adder(1, 2, 3, 4, 5, 6, 7))
    print("this is function_demo2:", __name__)




