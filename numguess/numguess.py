from random import randint

# I realized i should have swapped "lives" with "turns" and made it count turns instead of making you run out of lives.

lives = 4
print('You start off with ' + str(lives) + ' lives, for each wrong guess you lose 1 life.')

num = randint(1, 10)

while lives > 0:
    best_guess = int(input('Guess a number between 1 and 10: '))
    lives -= 1
    if best_guess == num:
        print('Nice guess!')
        break
    elif best_guess < num:
        print('You need to guess higher')
    elif best_guess > num:
        print('You need to guess lower')


"""

I Stuggled waaay to long solving this little puzzle by overthinking the "hints" the user would get, I was thinking about specific hints at first like: if your guess is not within 2 numbers of the random number you need to go up and down this and this much.

but when i realized it only had to check if the number was higher or lower and tell the user to go up or down accordingly i finished the entire program in about 10 seconds.

I need to stop overthinking stuff like this!

"""
