from getpass import getpass

class Hangman:

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
            secret_word = getpass(prompt="Please enter the 'secret' word of your choice: ").upper()
            lives = input("Please enter the amount of lives you want to add: ")

    lives = int(lives)
    letter_hits = ["-" for item in secret_word]
    used_letters = set() # Keeps tracks of all unique letters that have been guessed.

    @classmethod
    def matchLetter(cls):

        while cls.letter_hits != list(cls.secret_word) and cls.lives > 0:
            print('\nYou have', cls.lives, 'lives left and you have used these letters: ', ' '.join(cls.used_letters))
            print("Current word: ", " ".join(cls.letter_hits))
            user_guess = input("Guess 1 or more letters: ").upper()

            # Checks if 'user_guess' is alphabetic and not already used.
            if user_guess.isalpha() == True and user_guess not in cls.used_letters:
                cls.used_letters.add(user_guess)
                if user_guess in cls.secret_word:

                    # Adds 'user_guess' to 'cls.letter_hits' in the corresponding index to match 'cls.secret_word'.
                    for index, letter in enumerate(cls.secret_word):
                        if letter in user_guess:
                            cls.letter_hits[index] = letter
                else:
                    cls.lives -= 1
            else:
                print("\n-----'" + user_guess + "'", "is NOT a valid character, or has already been used!-----")

        if cls.lives == 0:
            print('\nHangman died. The word was:', "'" + cls.secret_word + "'")
        else:
            print('\nYAY! You guessed the word:', "'" + cls.secret_word + "'", '!!')

if __name__ == '__main__':
    Hangman.matchLetter()

