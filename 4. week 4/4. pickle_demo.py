# data serialization
import pickle

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
# pickle.dump(object, file handler, protocol= pickle.DEFAULT_PROTOCOL)  protocol = 0 to 5
with open('myFamily.pickle', 'bw') as binaryFile:
    pickle.dump(myFamily, binaryFile, protocol=pickle.DEFAULT_PROTOCOL)

# pickle.load()
with open('myFamily.pickle', 'br') as binaryFile:
    pickleString = pickle.load(binaryFile)
print(pickleString)
print(type(pickleString))

# pickle problems
# 1- insecure
# 2- accessibility

# 1- insecure:

pickle.loads(b"cos\nsystem\n(S'del pickle_test_delet.txt'\ntR.")  # this deletes the file in this root

# accessibility:
sampleList = [1, 2, 3]
sampleTuple = 4, 5, 6
with open('myFamily.pickle', 'bw') as pf:
    pickle.dump(myFamily, pf, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(sampleList, pf, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(sampleTuple, pf, protocol=pickle.DEFAULT_PROTOCOL)

with open('myFamily.pickle', 'br') as bf:
    new_myFamily = pickle.load(bf)
    new_sampleList = pickle.load(bf)
    new_sampleTuple = pickle.load(bf)

print(new_myFamily)
print(new_sampleList)
print(new_sampleTuple)

