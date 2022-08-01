def factorial(n: int):
    fac = 1
    # if n <= 1:
    #     return 1
    for _ in range(1, n+1, 1):
        fac *= _
    return fac


if __name__ == "__main__":
    print(factorial(5))

