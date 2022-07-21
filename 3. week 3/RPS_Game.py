import random
import os
quitTuple = ('q', 'quit')
starterBoolean = True
aValueForWinningScore = 0
choices = {1: "rock", 2: "paper", 3: "scissors"}
selectTuple = ("r", "rock", "p", "paper", "s", "scissors", "scissor")
userWord = ''
answer = ''
while starterBoolean:
    computerScore = 0
    userScore = 0
    inputValueForWinningScore = input("please type an integer number for winning score (q or Quit to exit): ")
    if inputValueForWinningScore.lower() in quitTuple:
        print("goodbye")
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
                    print("goodbye")
                    noWord = False
                    starterBoolean = False
                    break
                elif word.lower() in selectTuple:
                    computerChoice = choices[random.randint(1, 3)]
                    if word.lower() == "s":
                        userWord = "scissors"
                    elif word.lower() == "scissor":
                        userWord = "scissors"
                    elif word.lower() == 'r':
                        userWord = "rock"
                    elif word.lower() == 'p':
                        userWord = 'paper'

                    print("you choose", userWord)
                    print("computer chooses", computerChoice)
                    if userWord == computerChoice:
                        print("no one win")
                        print("computer Score: ", computerScore)
                        print("your score:", userScore)
                        clean = os.system("cls")
                        noWord = False
                        break
                    elif userWord == 'rock' and computerChoice == 'scissors':
                        print("you win")
                        userScore += 1
                        print("computer Score: ", computerScore)
                        print("your score:", userScore)
                        clean = os.system("cls")
                        noWord = False
                        break
                    elif userWord == 'rock' and computerChoice == 'paper':
                        print("computer win")
                        computerScore += 1
                        print("computer Score: ", computerScore)
                        print("your score:", userScore)
                        clean = os.system("cls")
                        noWord = False
                        break
                    elif userWord == 'paper' and computerChoice == 'scissors':
                        print("computer win")
                        computerScore += 1
                        print("computer Score: ", computerScore)
                        print("your score:", userScore)
                        clean = os.system("cls")
                        noWord = False
                        break
                    elif userWord == 'paper' and computerChoice == 'rock':
                        print("user win")
                        userScore += 1
                        print("computer Score: ", computerScore)
                        print("your score:", userScore)
                        clean = os.system("cls")
                        noWord = False
                        break
                    elif userWord == 'scissors' and computerChoice == 'rock':
                        print("computer win")
                        computerScore += 1
                        print("computer Score: ", computerScore)
                        print("your score:", userScore)
                        clean = os.system("cls")
                        noWord = False
                        break
                    elif userWord == 'scissors' and computerChoice == 'paper':
                        print("you win")
                        userScore += 1
                        print("computer Score: ", computerScore)
                        print("your score:", userScore)
                        clean = os.system("cls")
                        noWord = False
                        break
            if computerScore == aValueForWinningScore or userScore == aValueForWinningScore:
                if computerScore > userScore:
                    print("**" * 10, "computer win all rounds", "**" * 10)
                    while starterBoolean:
                        userYesNO = input("do you want to continue? [yes/no]").strip()
                        if userYesNO.lower().strip() in ['y', 'yes']:
                            starterBoolean = True
                            aValueForWinningScore = 0
                            break
                        elif userYesNO.lower().strip() in ['n', 'no']:
                            starterBoolean = False
                            print('goodbye')
                            break
                        else:
                            print("please type yes or no (n/y)")
                            continue
                else:
                    print("**" * 10, "you win all rounds", "**" * 10)
                    while starterBoolean:
                        userYesNO = input("do you want to continue? [yes/no]").strip()
                        if userYesNO.lower() in ['y', 'yes']:
                            starterBoolean = True
                            aValueForWinningScore = 0
                            break
                        elif userYesNO.lower() in ['n', 'no']:
                            starterBoolean = False
                            print("goodbye")
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
