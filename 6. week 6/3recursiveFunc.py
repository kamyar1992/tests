# recursive functions:
# must call function inside the recursive function
# must have a condition for witch at some point recursion could finish

# limitation:
# recursion depth: RecursionError
# Memory OverFlow :
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    print(factorial(3))

    # print(factorial(1000))
    print(factorial(998))
    print('=' * 40)

    print(fibonacci(10))
    print('------------------------')
    for i in range(20):  # if rang is more than 30 is make our system very slow or memory overflow error
        print(i, ':  ', fibonacci(i))









