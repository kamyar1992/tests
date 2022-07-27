def number_adder(*args, spt=":", ind = 1):
    sum_value = 0
    for num, index in enumerate(args, ind):
        print('{} {} {}'.format(index, spt, num))
        sum_value += num
    print(dir())
    print(locals())
    return sum_value


# dir()
# locals()
# globals()

kamyar = 1
kamyar2 = "Mazaheri"
print(dir())
print(locals())
print(globals())
print(locals() == globals())  # locals() in the executable part of a module is globals

print('=' * 40)

print(number_adder(1, 2, 3))

