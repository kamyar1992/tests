# mapping

# dictionary

emptyDic = {}
anotherEmptydic = dict()

sampleDic = {'name': 'kamyar',
             'family': 'mazaheri',
             'age': 30}

# accessing values can ONLY be through keys

print(sampleDic['name'])
print(hex(id(sampleDic)))
sampleDic['education'] = 'diploma'
print(hex(id(sampleDic)))
print(sampleDic)
# dictionaries are mutable
# .values():
print(sampleDic.values())
dictValuesList = list(sampleDic.values())
print(dictValuesList)

# .keys():
print(sampleDic.keys())
dictKeysList = list(sampleDic.keys())
print(dictKeysList)

# .items():
print(sampleDic.items())
dictItemsList = tuple(sampleDic.items())
print(dictItemsList)

# cast to a dictionary

newDic = dict(dictItemsList)
print(newDic)


# insertion order v14
# memory order    v14

for key in sampleDic:  # very fast o(n)
    print(sampleDic[key])

for value in sampleDic.values():  # very low o(n^2)
    print(value)

my_dict = dict.fromkeys(['a', 'c', 'd'], 10)
my_dict.update(dict.fromkeys(['b', 'e'], 20))
print(my_dict)








