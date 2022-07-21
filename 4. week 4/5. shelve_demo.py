import shelve
# must use shelve.open()
# it's like a dictionary
# its keys must be immutable and STRING
# it does not have  literals
# *important : it does not take mode of as the second argument file for example 'bw'

myFamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

sampleList = [1, 2, 3]
sampleTuple = 4, 5, 6
with shelve.open('sampleShelve.shelve') as shelveFile:
    shelveFile['myFamily'] = myFamily
    shelveFile['sL'] = sampleTuple
    shelveFile['sT'] = sampleTuple

with shelve.open('sampleShelve.shelve', 'r') as sFile:
    new_myFamily = sFile['myFamily']
    new_sL = sFile['sL']
    new_sT = sFile['sT']

print(new_sT)
print(new_myFamily)
print(new_sT)
print('='*40)

with shelve.open('testShelve.shelve') as sSFile:  # it does not have literals
    sSFile = {'myFamily': myFamily,
              'sL': sampleList,
              'sT': sampleTuple}
    print(type(sSFile))

print('='*40)
# *important : shelves are persisted dictionary:
with shelve.open('sampleShelve.shelve') as tSFile:
    tSFile['myFamilies'] = myFamily

    for item in tSFile:
        print(item)
        print(tSFile[item])





























