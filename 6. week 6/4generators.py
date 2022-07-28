# Generators : a function that write with yield
import sys
def my_range(n: int):
    starter = 0
    while starter < n:
        print("the value is: {}".format(starter))
        yield starter
        starter += 1


if __name__ == '__main__':
    temp = my_range(10)
    r = range(10)
    print(sys.getsizeof(temp))
    print(sys.getsizeof(r))
    for i in temp:
        print(i)
    print("=" * 40)
    for i in temp:  # *important : as you can see this for does not work the generators that we created must not assign
        print(i)    # to a variable but for example range() it works
    print("the last for does not work\n", "=" * 40)
    for i in r:
        print(i)
    print("both for work because of range()\n", "=" * 40)
    for i in r:
        print(i)















