from random import randint

def get_limit():
    # Get the number limit
    num_limit = input("Enter the amount of numbers, starting at 1: ")

    # Validate the number limit
    while num_limit.isdigit() == False:
        num_limit = input("'" + num_limit + "'" + "is not a number! Enter again: ")

    return int(num_limit)

def guess(num_limit, random_num):
    # Set the turn to 1
    turn = 1

    # Get the first guess
    user_guess = input("\nTurn " + str(turn) + '.\nGuess a number between 1 and ' + str(num_limit) + ': ')

    # Validate the first guess
    while user_guess.isdigit() == False:
        user_guess = input("'" + user_guess + "'" + "is not a number! Guess again: ")

    # While the users guess is not equal to the random number
    while user_guess != random_num:

        # If the guess is valid
        if user_guess.isdigit() == True:
            # Convert the guess from a string to a integer
            user_guess = int(user_guess)

            # Increment the turn
            turn += 1

            # Print the turn number
            print("\nTurn " + str(turn) + ".")

            # If the guess was correct
            if user_guess == random_num:
                # Print message and break
                print('Nice guess!')
                break

            # If the guess was lower than the random number
            elif user_guess < random_num:
                user_guess = input('You need to guess HIGHER: ')

            # If the guess was higher than the random number
            elif user_guess > random_num:
                user_guess = input('You need to guess LOWER: ')
        # Else if the guess is invalid
        else:
            user_guess = input("'" + user_guess + "'" + "is not a number!: ")

    print("\n\n ----------Yay, you guessed the correct number '" + str(random_num) +  "'!----------\n\n")


# Get the number limit
num_limit = get_limit()

# Get a random number
random_num = randint(1, (num_limit + 1))

# Call the main guessing loop
guess(num_limit, random_num)
