# سنگ کاغذ قیچی
import random

Score_Ali, Score_Christopher = 0, 0

while (True):
    Ali = input("Sang, Kakhaz, Gheychi")
    Christopher = random.randint(1, 3)

    if Christopher == 1:
        Christopher = "Sang"
    elif Christopher == 2:
        Christopher = "Kakhaz"
    elif Christopher == 3:
        Christopher = "Gheychi"

    if Ali == Christopher:
        print('no one win')

    elif Ali == "Sang" and Christopher == "Kakhaz":
        Score_Christopher += 1

    elif Ali == "Sang" and Christopher == "Gheychi":
        Score_Ali += 1

    elif Ali == "Kakhaz" and Christopher == "Sang":
        Score_Ali += 1

    elif Ali == "Kakhaz" and Christopher == "Gheychi":
        Score_Christopher += 1

    elif Ali == "Gheychi" and Christopher == "Sang":
        Score_Christopher += 1

    elif Ali == "Gheychi" and Christopher == "Kakhaz":
        Score_Ali += 1

    print(f"Ali: {Ali}")
    print(f"Christopher: {Christopher}")
    print("** Score **")
    print(f"Score_Ali: {Score_Ali}")
    print(f"Score_Christopher: {Score_Christopher} \n")

    if Ali == "n":
        break