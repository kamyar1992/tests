with open("dummyText2.txt", 'r') as tF:
    fileString = tF.read()

sList = fileString.split()
uniqueWord = set(sList)
print(len(uniqueWord))
wordCounts = {}
uniqueWords = 0
totNumberOfToBeVerb = 0
plainWord = ''
toBeDic = {'am': 0,
           'is': 0,
           'are': 0,
           'was': 0,
           'were': 0}
for word in sList:
    plainWord = word.removesuffix('"').lower()
    plainWord = plainWord.removeprefix('"')
    plainWord = plainWord.removesuffix(".")
    plainWord = plainWord.removesuffix(',')
    plainWord = plainWord.removesuffix("s'")
    plainWord = plainWord.removesuffix("'s")

    if plainWord not in wordCounts:
        wordCounts[plainWord] = 1
    else:
        wordCounts[plainWord] += 1
for word in wordCounts:
    print(word, ': ', wordCounts[word])

for word in wordCounts:
    if wordCounts[word] == 1:
        uniqueWords += 1
    if word in toBeDic.keys():
        toBeDic[word] += 1
print('='*40)
print('uniquewords: ', uniqueWords)
print('='*40)
for verb in toBeDic:
    print(verb, toBeDic[verb])
    totNumberOfToBeVerb += toBeDic[verb]
print('total number of to be verbs: ', totNumberOfToBeVerb)
print('='*40)




