# functions that have self arguments are called methods
# magic methods or dunder methods

a = 5
b = 10

print(a + b)
print(a.__add__(b))

print(help(type))


class Foo(object):  # foo the name that use for examples

    def __new__(cls):
        print('new is called')
        return object.__new__(cls)

    def __init__(self):
        self.a = 1
        print('init is called')

    def set_a(self, val):
        self.a = val

    def __str__(self):
        return 'this is foo class and a attribute is {}'.format(self.a)

    def __call__(self, *args, **kwargs):
        return 'call method is initiated'


if __name__ == "__main__":
    f = Foo()
    print(f)  # this is used __str__() method
    f.set_a(3)
    print(f)
    print('=' * 50)
    print(f())


