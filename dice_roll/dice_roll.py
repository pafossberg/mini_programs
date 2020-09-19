from random import randint

# Prints a number between 1 and 6 like a dice. Breaks if user input is "quit".
def dice_roll(roll: str) -> int:
    print("Press 'Enter to roll the dice")
    print("Type 'print' to print a number between 1 and 6")
    print("Type 'quit' to quit the program")
    while roll == '':
        user_input = input("Do you choose to 'Enter', 'Print' or 'Quit'? ->  ")
        if user_input == 'quit':
            break
        elif user_input == 'print':
            print(dice_num)
            break
        else:
            dice_num = str(randint(1, 6))
            print(dice_num)

dice_roll(input("Press 'Enter'"))


# I can change some of the text to make it look nicer and smoother, maybe get rid of the useless 'enter' press at the start.

# I can also make the program less case-sensitive and make it more stable in general.
