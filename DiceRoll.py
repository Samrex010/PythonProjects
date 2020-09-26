import random

x = "y"

while x == "y":
    number = random.randint(1, 6)

    if number == 1:
        print(" ___________")
        print("|           |")
        print("|           |")
        print("|     O     |")
        print("|           |")
        print("|___________|")
    if number == 2:
        print(" ___________")
        print("|           |")
        print("|           |")
        print("|  O     O  |")
        print("|           |")
        print("|___________|")
    if number == 3:
        print(" ___________")
        print("|           |")
        print("|  O     O  |")
        print("|           |")
        print("|     O     |")
        print("|___________|")
    if number == 4:
        print(" ___________")
        print("|           |")
        print("|  O     O  |")
        print("|           |")
        print("|  O     O  |")
        print("|___________|")
    if number == 5:
        print(" ___________")
        print("|           |")
        print("|  O     O  |")
        print("|     O     |")
        print("|  O     O  |")
        print("|___________|")
    if number == 6:
        print(" ___________")
        print("|           |")
        print("|  O     O  |")
        print("|  O     O  |")
        print("|  O     O  |")
        print("|___________|")
    x = input("\nRoll again?\nType y for Yes or n for No: ")
