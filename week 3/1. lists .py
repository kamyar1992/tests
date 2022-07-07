# sequence
# 1- ordered
# 2- Index_able

emptyList = []  # literal
sampleList2 = list()  # constructor

#sampleList = [1, 2, 'A', 3]
sampleList = [1, 2, -0.5, 3]

sampleList.append(-10)

# pep : a list should have same data type item because some methods just work on a list that have the same data type
# item

print(sampleList.sort())  # sort return null
print(sampleList)

# why sort return none? because:
# 1- all variable in python is a pointer
# 2- list is a mutable object


a = 5
print(hex(id(a)))
b = 5
print(hex(id(b)))
print('+'*40)
# in video 2 and 3 explain pointer and mutable
print(hex(id(sampleList)))
sampleList.append(20)
sampleList.sort()
print(hex(id(sampleList)))
print(sampleList)
print('+'*40)
# list copy:
# shallow copy and deep copy

# shallow copy:
odd = [1, 3, 5, 7, [101]]

backUp1 = odd
backUp2 = list(odd)
backUp3 = odd.copy()

print("od_id:     ", id(odd))
print("backUp1_id:", id(backUp1))
print("backUp2_id:", id(backUp2))
print("backUp3_id:", id(backUp3))



odd.append('1')

print("odd_id:    ", id(odd), "backUp1:", odd)
print("backUp1_id:", id(backUp1), "backUp1:", backUp1)
print("backUp2_id:", id(backUp2), "backUp1:", backUp2)
print("backUp3_id:", id(backUp3), "backUp1:", backUp3)

print('+'*40)
print('innner Lists:')
odd[4].append(20)

print("odd_id:    ", id(odd), "backUp1:", odd)
print("backUp1_id:", id(backUp1), "backUp1:", backUp1)
print("backUp2_id:", id(backUp2), "backUp1:", backUp2)
print("backUp3_id:", id(backUp3), "backUp1:", backUp3)


print('+'*40)
print('copy.copy')
import copy
backUp4 = copy.copy(odd)
odd[4].append(40)
print("backUp4_id:   ", id(backUp4), "backUp1:", backUp4)

print('+'*40)
# deep copy
fullBackUp = copy.deepcopy(odd)
odd.append(20)
odd[4].append(50)
print("odd_id:       ", id(odd), "odd:", odd)
print("fullBackUP_id:", id(fullBackUp), "fullBackUp:", fullBackUp)


# assignment:
print('+'*40)
print("assignment")
odd = odd + [1000]
print("backUp1_id: ", id(backUp1), "backUp1:", fullBackUp)
print("odd_id:     ", id(odd), "odd:", odd)

# assignment:
print('+'*40)
print("augment assignment")
odd += [1000]
print("backUp1_id: ", id(backUp1), "backUp1:", fullBackUp)
print("odd_id:     ", id(odd), "odd:", odd)














