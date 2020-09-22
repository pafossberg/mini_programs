from getpass import getpass

# Still doesen't guard againt using a character more than once if the used character was a hit!
# I still need to comment out all the code, didn't have time to do this before i had to go.
# Note to self, comment WHILE coding.

def secret_phrase():
    secret_word = getpass(prompt="Please enter the 'secret' word of your choice: ").upper()
    while secret_word.isalpha() == False:
        print("'" + secret_word + "'", "is not a legal phrase, ONLY alphabetic characters please!\n")
        secret_word = getpass(prompt="Please enter the 'secret' word of your choice: ").upper()
    hangman(secret_word)


def hangman(secret_word):
    secret_list = list(secret_word)
    lives = 6
    letter_hits = ["-" for item in secret_word]
    used_letters = set()

    while len(secret_list) > 0 and lives > 0:
        print('\nYou have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        print("Current word: ", " ".join(letter_hits))
        letter = input("Guess a letter: ").upper()
        used_letters.add(letter)
        if letter.isalpha() == False:
            print("'" + letter + "'", "is not a valid character!")
        elif letter in secret_word:
            for a, i in enumerate(secret_word):
                if i in letter:
                    letter_hits[a] = i
                    secret_list.remove(i)
        else:
            lives -= 1
    if lives == 0:
        print('\nYou died, sorry. The word was:', "'" + secret_word + "'")
    else:
        print('\nYAY! You guessed the word:', "'" + secret_word + "'", '!!')

if __name__ == '__main__':
    secret_phrase()

