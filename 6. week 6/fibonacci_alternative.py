def fibonacci(n):
    previous, current = 0, 1
    for _ in range(n):
        # print(current)
        previous, current = current, current + previous
    return current


if __name__ == '__main__':
    print(len(str(fibonacci(100000))))
    print(fibonacci(10))

