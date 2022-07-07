# tuple
# immutable

emptyTuple = ()
anotherEmptyTuple = tuple()

sampleTuple = 1, 2, 3
print(type(sampleTuple))
print(sampleTuple)

print(1, 2, 3)  # a tuple is not printed here
print((1, 2, 3))  # a tuple is printed here

print(hex(id(sampleTuple)))
sampleTuple = sampleTuple[0] , 10, sampleTuple[2]
print(sampleTuple)
print(hex(id(sampleTuple)))

print('=' * 40)
# tuple unpacking
album = "shajarian", 2003, ("nasim-e-vesal", "sokoot", "havay-e-geryeh")
artist, year, track = album
print(artist)
print(year)
print(track)

#================================================================
print('='*40)
# size of tuple and list
import sys
oddTuple = tuple(range(1, 20, 2))
oddList = list(range(1, 20, 2))
print('size of tuple {} BYTES: '.format(sys.getsizeof(oddTuple)))
print('size of list {} BYTES: '.format(sys.getsizeof(oddList)))









