bloodType = ('o-', 'o+', 'a-', 'a+', 'b-', 'b+', 'ab-', 'ab+')
starterBoolean = True
quitTuple = ('q', 'quit')
wrongString = ''
inputString = 'provider'
error = ''
pType = ''
rType = ''


def blood(provider, receiver):
    indexProvider = bloodType.index(provider)
    indexReceiver = bloodType.index(receiver)
    bloodProviderDic = {0: range(8),
                        1: range(1, 8, 2),
                        2: (2, 3, 6, 7),
                        3: (3, 7),
                        4: (4, 5, 6, 7),
                        5: (5, 7),
                        6: (6, 7),
                        7: (7,)
                        }
    if indexReceiver in list(bloodProviderDic[indexProvider]):
        return True
    else:
        return False


def true_word(words):
    for word in words:
        if word in quitTuple:
            return 'quit'
        if word in bloodType:
            return True, word
        else:
            return False
while starterBoolean:
    providerInput = input(error + 'please type ' + "\33[31m" + inputString + "\33[39m"+' blood type (q or quit): ').lower()
    error = ''
    providerInputList = providerInput.split()
    if true_word(providerInputList) == 'quit':
        print('goodbye')
        break
    elif true_word(providerInputList):
        if inputString == 'provider':
            pType = true_word(providerInputList)[1]
            inputString = 'receiver'
            continue
        elif inputString == 'receiver':
            rType = true_word(providerInputList)[1]
            inputString = ''
    else:
        error = 'please type correct blood type \n'
    if pType and rType:
        if blood(pType, rType):
            print("OK")
        else:
            print('NOT OK')
        pType = ''
        rType = ''
        inputString = 'provider'



