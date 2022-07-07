import math
# .format: is a pythonic way
for number in range(16):
    print("{0:<3} to the power of two is {1:>6.3f}".format(number, number ** 2/3))
print("="*40)

# casting : converting one data type to another
# casting : 1- explicit 2- implicit : explicit is better than implicit pep 20
import this
print(math.pi)
print(float("{:.3f}".format(math.pi)))
name = 'Kamyar'
age: str = '30'
print("My name is %s, I am %s"%(name, '30'))  # it is nooooooot pythonic

print(f'My name is{name}, I am {age}')  # it is pythonic formatted string literals

print(f'{name}, {age}')  # search done https://docs.python.org/3/reference/lexical_analysis.html#f-strings
print("hello \n my name is Kamyar")  # \ scape character search done https://docs.python.org/3/reference/lexical_analysis.html
print("hello \\name is Kamyar")
print("hello \t kamyar")
print("hello \ hello")
print("C:\\Users\\ASUSCenter\\Desktop\\Dayche")

print("="*40)
print(r'name:{name}, {age}')
print(u'{name}, {age}')
print(fr'{name}, {age}')
print(br'{name}, {age}')
print(rb'{name}, {age}')
print(u'{name}, {age}')
print(f'{name}, {age}')



