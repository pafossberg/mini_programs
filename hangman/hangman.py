from getpass import getpass


def get_values():
    # Sets the values for 'secre_word' and 'lives' by getting input from the user.
    # The 'secret_word value is hidden with the 'getpass' method.

    # Checks whether the input values are valid, and keeps asking if not.
    secret_word = getpass(
        prompt="Please enter the 'secret' word of your choice: ").upper()
    lives = input("Please enter the amount of lives you want to add: ")
    while True:
        try:
            if not secret_word.isalpha():
                print("\n'" + secret_word + "'", "is not a WORD.")
                raise Exception
            elif not lives.isdigit():
                print("\n'" + lives + "'", "Is not a NUMBER.")
                raise Exception
            break
        except Exception:
            secret_word = getpass(
                prompt="Please enter the 'secret' word of your choice: ").upper()
            lives = input("Please enter the amount of lives you want to add: ")

    hangman(secret_word, int(lives))


def hangman(secret_word: str, lives: int) -> 'letter_hits':
    # Checks 'letter_hits', the amount of 'lives' and 'used_letters' and prints the results.
    # Stops if 'letter_hits' matches 'secret_word' or if lives == 0.

    letter_hits = ["-" for item in secret_word]
    # Keeps tracks of all unique letters that have been guessed.
    used_letters = set()

    while letter_hits != list(secret_word) and lives > 0:
        print('\nYou have', lives,
              'lives left and you have used these letters: ', ' '.join(used_letters))
        print("Current word: ", " ".join(letter_hits))
        user_guess = input("Guess 1 or more letters: ").upper()

        # Checks if 'user_guess' is alphabetic and not already used.
        if user_guess.isalpha() == True and user_guess not in used_letters:
            used_letters.add(user_guess)
            if user_guess in secret_word:

                # Adds 'user_guess' to 'letter_hits' in the corresponding index to match 'secret_word'.
                for index, letter in enumerate(secret_word):
                    if letter in user_guess:
                        letter_hits[index] = letter
            else:
                lives -= 1
        else:
            print("\n-----'" + user_guess + "'",
                  "is NOT a valid character, or has already been used!-----")

    if lives == 0:
        print('\nHangman died. The word was:', "'" + secret_word + "'")
    else:
        print('\nYAY! You guessed the word:', "'" + secret_word + "'", '!!')


if __name__ == '__main__':
    get_values()
