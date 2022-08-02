def factorial(n: int):
    fac = 1
    # if n <= 1:
    #     return 1
    for _ in range(1, n+1, 1):
        fac *= _
    return fac


if __name__ == "__main__":
    print(factorial(5))

def fibonacci(n):
    previous, current = 0, 1
    for _ in range(n):
        # print(current)
        yield current
        # return current
        previous, current = current, previous + current