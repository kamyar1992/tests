# We want to play an Old game called rock, scisor , paper
import random

#  Bazi be chand bashe?
gameIteration = input("How many a winner should win to win the game?")
# while not gameIteration.isdigit():
#     print("Your input should be a number between 1 and 999")
#     gameIteration = input("How many a winner should win to win the game?")


# PC random Choice
choices_list = ["R", "Rock", "S", "Scisor", "P", "Paper"]
random_choice = random.choice(choices_list)


# User choice
print("""if you want to exit you can type "Quit" or "Q""")


userChoice = input("Rock (r), Scisor (s) or Paper (p) ? ")

computer_score = 0
user_score = 0
if x == '':
    for x in range(int(gameIteration)):
        print(x)
        print(userChoice.lower())
    if userChoice.lower() == "q" or userChoice.lower() == "quit":
        print(userChoice)
        break

    elif userChoice.lower() == "r" or userChoice.lower() == "rock":
        if random_choice.lower() == "s" or random_choice.lower() == "scisor":
            print("you won!")
            user_score += 1
        elif random_choice.lower() == "p" or random_choice.lower() == "paper":
            print("you lost!")
            computer_score += 1
        elif random_choice.lower() == "r" or random_choice.lower() == "rock":
            print("Computer chose Rock too, so no one won the game and it should be repeated!")

    elif userChoice.lower() == "s" or userChoice.lower() == "scisor":
        if random_choice.lower() == "p" or random_choice.lower() == "paper":
            print("you won!")
            user_score = user_score + 1
        elif random_choice.lower() == "p" or random_choice.lower() == "paper":
            print("you lost!")
            computer_score = computer_score + 1
        elif random_choice.lower() == "s" or random_choice.lower() == "scisor":
            print("Computer chose Scisor too, so no one won the game and it should be repeated!")

    elif userChoice.lower() == "p" or userChoice.lower() == "paper":
        if random_choice.lower() == "r" or random_choice.lower() == "rock":
            print("you won!")
            user_score += 1
        elif random_choice.lower() == "s" or random_choice.lower() == "scisor":
            print("you lost!")
            computer_score += 1
        elif random_choice.lower() == "p" or random_choice.lower() == "paper":
            print("Computer chose Paper too, so no one won the game and it should be repeated!")

    else:
        print("You should choose Paper, Rock or Scisor! If you want to Quit press Q!")

print(random_choice)
print("Your score is {}".format(user_score))
print("Computer score is {}".format(computer_score))
