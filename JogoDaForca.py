import time
import random

playerName = input('What is your name?: ')
gameList = ('Jorge', 'Pizza', 'Mulher', 'Alien', 'Oculos', 'Policial', 'Voador', 'Filme', 'Comunista', 'FuckBozo')
randomInt = random.randint(0, len(gameList) - 1)
guessWord = gameList[randomInt]
word = guessWord
turns = 10
guesses = ''

print('\nHello,', playerName, 'time to play hangman!')

time.sleep(1)

print('\nStart guessing...\n')

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print('_', end=' ')
            failed += 1

    if failed == 0:
        print('\n\nYou won!')
        break

    guess = input('\n\nGuess a char: ')
    guesses += guess

    if guess not in word:
        turns -= 1
        print('\nTry again!')
        print('You have', turns, 'more guesses.')

        if turns == 0:
            print('\n\nYou lost!')