from getpass import getpass

# I still need to comment out all the code, didn't have time to do this before i had to go.
# I can probaby change alot of the "Secret_word" into "secret_phrase" function calls instead.

def get_values():
    secret_word = getpass(prompt="Please enter the 'secret' word of your choice: ").upper()
    while secret_word.isalpha() == False:
        print("'" + secret_word + "'", "is not a legal phrase, ONLY alphabetic characters please!\n")
        secret_word = getpass(prompt="Please enter the 'secret' word of your choice: ").upper()
    lives = input("Please enter the amount of lives you want to add: ")
    while lives.isdigit() == False:
        print("'" + lives + "'", "Is not a NUMBER.\n")
        lives = input("Please enter the amount of lives you want to add: ")
    hangman(secret_word, int(lives))


def hangman(secret_word, lives):
    secret_list = list(secret_word)
    letter_hits = ["-" for item in secret_word]
    used_letters = set()

    while len(secret_list) > 0 and int(lives) > 0:
        print('\nYou have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        print("Current word: ", " ".join(letter_hits))
        letter = input("Guess 1 or more letters: ").upper()
        if letter.isalpha() == False or letter in used_letters:
            print("\n-----'" + letter + "'", "is NOT a valid character, or has already been used!-----")
        elif letter in secret_word:
            used_letters.add(letter)
            for a, i in enumerate(secret_word):
                if i in letter and i in secret_list:
                    letter_hits[a] = i
                    secret_list.remove(i)
        else:
            lives -= 1
    if lives == 0:
        print('\nYou died, sorry. The word was:', "'" + secret_word + "'")
    else:
        print('\nYAY! You guessed the word:', "'" + secret_word + "'", '!!')

if __name__ == '__main__':
    get_values()

