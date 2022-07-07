# set:
# unordered data type

# you CANNOT define a set with literals
emptySet = set()


sampleSet = {1, 2, 3, 'kamyar', 'Mazaheri', 3, 'A', 'A'}
print(sampleSet)  # sets do not take repetitive elements : like set in set theory

for i in range(5):
    print(sampleSet)  # when it writes into memory its order does not change
print("="* 40)
even = set(range(1, 50, 2))  # members : 25
power = {1, 4, 9, 16, 25, 36, 49}  # members : 7

print(even.intersection(power))
print(len(even.union(power)))  # sets act like mathematics sets and not get repetitive elements






















