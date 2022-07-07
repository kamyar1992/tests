# sequence:
# string:
# slicing:
# index [start : stop : step]
# step : show the direction of movement - right to left + left to right (default is +1)

my_string = 'ABCDEFGHYZ'
print(my_string[-1:-10]) # this does not work because the default step is 1  *important
print(my_string[-1:5])
# *important : does not make a circle
print(my_string[-1:-10:-1])
print(my_string[3: -5])  # *important
print(my_string[-1: 3: -1])  # *important

