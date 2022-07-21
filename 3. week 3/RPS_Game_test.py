import random
quitTuple = ('q', 'quit')
starterBoolean = True
continueBoolean = False
aValueForWinningScore = 0
computerChoices = ("rock", "paper", "scissors")
# selectTuple = ('r', "rock", "p", "paper", "s", "scissors", "scissor", 'kaghaz', 'gheychi', 'sang')
selectDic = dict.fromkeys(["r", "rock", "sang"], 'rock')
selectDic.update(dict.fromkeys(["p", "paper", "kaghaz"], 'paper'))
selectDic.update(dict.fromkeys(["s", "scissors", "gheychi", "scissor"], 'scissors'))

scoreTuple = (('rock', 'scissors'),
              ('scissors', 'paper'),
              ('paper', 'rock'))
userChoice = ''

while starterBoolean:
    computerScore = 0
    userScore = 0
    inputValueForWinningScore = input("please type an integer number for winning score (q or Quit to exit): ").strip()
    if inputValueForWinningScore.lower() in quitTuple:
        print("GOODBYE")
        # starterBoolean = False
        break
    elif inputValueForWinningScore.isdigit():
        aValueForWinningScore = int(inputValueForWinningScore)
        while aValueForWinningScore and starterBoolean:
            noWord = True
            inputValueForSelect = input("please select either rock(r), paper(p) or scissors(s) (or Quit to exit) ")
            inputValueForSelectList = inputValueForSelect.split()
            for word in inputValueForSelectList:
                if word.lower() in quitTuple:
                    print("GOODBYE")
                    noWord = False
                    starterBoolean = False
                    break
                elif word.lower() in selectDic:
                    computerChoice = random.choice(computerChoices)
                    userChoice = selectDic[word.lower()]
                    print("you choose", userChoice)
                    print("computer chooses", computerChoice)
                    if userChoice == computerChoice:
                        print("no one win")
                        print("computer Score: ", computerScore)
                        print("your score:", userScore)
                        noWord = False
                        break
                    elif (userChoice, computerChoice) in scoreTuple:
                        print("you win")
                        userScore += 1
                        print("computer Score: ", computerScore)
                        print("your score:", userScore)
                        noWord = False
                        break
                    else:
                        print("computer win")
                        computerScore += 1
                        print("computer Score: ", computerScore)
                        print("your score:", userScore)
                        noWord = False
                        break

            if computerScore == aValueForWinningScore:
                print("**" * 10, "computer win all rounds", "**" * 10)
                continueBoolean = True
            elif userScore == aValueForWinningScore:
                print("**" * 10, "you win all rounds", "**" * 10)
                continueBoolean = True
            while continueBoolean:
                userYesNO = input("do you want to continue? [yes/no]").strip()
                if userYesNO.lower() in ['y', 'yes']:
                    continueBoolean = False
                    aValueForWinningScore = 0
                    break
                elif userYesNO.lower() in ['n', 'no']:
                    starterBoolean = False
                    print("GOODBYE")
                    break
                else:
                    print("please type yes or no (n/y)")
                    continue
            if noWord:
                print("you do not choose either rock, paper or scissors (or Quit to exit)")
                continue
    else:
        print("please type an integer number!!! (q or Quit to exit)")
        continue
