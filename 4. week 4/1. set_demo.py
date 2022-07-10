# unordered data type
# sets are mutable
# you CANNOT define an empty set using literals

emptySet = set()

sampleSet = {1, 2, 'A', 'kamyar', 100}
print(sampleSet)
for x in range(10):  # if it writes on memory its order does not change
    print(sampleSet)


print("+"*40)
odd = set(range(1, 50, 2))  # 25 members
power = {1, 4, 9, 16, 25, 36, 49}  # 7 members

print(odd.intersection(power))
print(len(odd.intersection(power)))

# *important: a set does not take repetitive members
print(len(odd.union(power)))  # sum of two sets is 32 but it gives 28






print('change list')


# sets update methods
print(odd.intersection_update(power))  # it returns none because sets are mutable
print(odd)

# frozenset(): make an iterable object to a immutable set

alphabetList = ['a', 'b', 'c', 'd']
frozenSet = frozenset(alphabetList)
print(frozenSet)























