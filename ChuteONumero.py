from random import randint

randomNumber = randint(0, 100)
playerGuess = int(input('Digite um número: '))
playerAttempts = 1

while (playerGuess != randomNumber):
    if playerGuess > randomNumber:
        print('\nTente um número menor.')
    else:
        print('\nTente um número maior.')
    
    playerAttempts += 1
    playerGuess = int(input('\nDigite um número: '))

    if playerGuess == randomNumber:
        print('\nVoce ganhou!')
        print('Voce chutou,', playerAttempts, 'vezes.')
