from random import randint

# Still need to comment out the code

def limit():
    turns = 0

    num_limit = input("Enter the amount of numbers, starting at 1: ")
    while num_limit.isdigit() == False:
        num_limit = input("'" + num_limit + "'" + "is not a number!: ")
 
    user_guess = input("\nTurn " + str(turns) + '\nGuess a number between 1 and ' + num_limit + ': ')
    while user_guess.isdigit() == False:
        user_guess = input("'" + user_guess + "'" + "is not a number!: ")

    return number_guess(num_limit, user_guess, turns)


def number_guess(num_limit, user_guess, turns):

    num = randint(1, int(num_limit))
    print(num)
    while user_guess != str(num):

        if user_guess.isdigit() == True:
            user_guess = int(user_guess)
            turns += 1
            print("\nTurn", turns)
            if user_guess == num:
                print('Nice guess!')
                break
            elif user_guess < num:
                user_guess = input('You need to guess HIGHER: ')
            elif user_guess > num:
                user_guess = input('You need to guess LOWER: ')
        else:
            user_guess = input("'" + user_guess + "'" + "is not a number!: ")

    print("\n\n ----------Yay, you guessed the correct number '" + str(num) +  "'!----------\n\n")

limit()
