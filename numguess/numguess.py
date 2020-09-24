from random import randint

# Doesent check if the inputs are legal
# Still need to comment out the code

def limit():
    num_limit = input("Enter the amount of numbers, starting at 1: ")
    return number_guess(num_limit)


def number_guess(num_limit):
    turns = 0
    user_guess = int(input("\nTurn " + str(turns) + '\nGuess a number between 1 and ' + num_limit + ': '))
    num = randint(1, int(num_limit))

    while user_guess != num:
        turns += 1
        print("\nTurn", turns)
        if user_guess == num:
            print('Nice guess!')
            break
        elif user_guess < num:
            user_guess = int(input('You need to guess HIGHER: '))
        elif user_guess > num:
            user_guess = int(input('You need to guess LOWER: '))

limit()
