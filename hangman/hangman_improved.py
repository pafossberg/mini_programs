from getpass import getpass

class Hangman:

    def __init__(self, secret_word, lives):
        self.secret_word = secret_word.upper()
        self.lives = int(lives)
        self.letter_hits = ["-" for item in self.secret_word]
        self.used_letters = set()

    # Gets user input and checks if input is valid.
    # Entire method can be commented out if you want to set method attributes manually.
    # I.E set the "secret_word" and "lives" attributes.
    @classmethod
    def getInput(cls):
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
                secret_word = getpass(prompt="Please enter the 'secret' word of your choice: ")
                lives = input("Please enter the amount of lives you want to add: ")
        return cls(secret_word, lives)


    def matchLetter(self):
    # Checks 'letter_hits', the amount of 'lives' and 'used_letters' and prints the results.
    # Stops if 'letter_hits' matches 'secret_word' or if lives == 0.

        while self.letter_hits != list(self.secret_word) and self.lives > 0:
            print('\nYou have', self.lives, 'lives left and you have used these letters: ',
                    ' '.join(self.used_letters))
            print("Current word: ", " ".join(self.letter_hits))
            user_guess = input("Guess 1 or more letters: ").upper()

            # Checks if 'user_guess' is alphabetic and not already used.
            if user_guess.isalpha() == True and user_guess not in self.used_letters:
                self.used_letters.add(user_guess)
                if user_guess in self.secret_word:

                    # Adds 'user_guess' to 'letter_hits' in the corresponding index to match 'self.secret_word'.
                    for index, letter in enumerate(self.secret_word):
                        if letter in user_guess:
                            self.letter_hits[index] = letter
                else:
                    self.lives -= 1
            else:
                print("\n-----'" + user_guess + "'", "is NOT a valid character, or has already been used!-----")

        if self.lives == 0:
            print('\nHangman died. The word was:', "'" + self.secret_word + "'")
        else:
            print('\nYAY! You guessed the word:', "'" + self.secret_word + "'", '!!')

# un-comment line=62, and comment out line=61 to manually set attributes.
user = Hangman.getInput()
# user = Hangman('eXampleWord', 10)

if __name__ == '__main__':
    user.matchLetter()
