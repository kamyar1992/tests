# iterators
sampleList = [1, 2, 3]
sampleString = "ABCDE"

for char in sampleString:
    print(char)

# char = iterator
# sampleList = iterable Object

char = iter(sampleString)
elem = iter(sampleList)
print(char)
print(elem)
print(type(char))
print(type(elem))
print('='*40)

print(next(char))
print(next(char))
print(next(char))
print(next(char))
print(next(char))
try:
    print(next(char))
except Exception as error1:
    print(error1)