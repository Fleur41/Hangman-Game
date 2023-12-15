''''
Hangman Game
-------------------------------------------------------------
'''

import random
import time
import os

def play_again():
    question = "Do you want to play again? y = yes, n = no\n"
    play_game = input(question)
    while play_game.lower() not in ['y', 'n']:
        play_game = input(question)
    if play_game.lower() == 'y':
        return True
    else:
        return False
    
def hangman(word):
    display = '_' * len(word)
    count = 0
    limit = 5
    letters = list(word)
    guessed = []
    while count < limit:
        guess = input(f'Hangman Word: {display} Enter your guess: \n').strip()
        while len(guess) == 0 or len(guess) > 1:
            print('Invalid input. Enter a single letter\n')
            guess = input(
                f'Hangman Word: {display} Enter your guess: \n').strip()
            
        if guess in guessed:
            print('Ooops! You already tried that guess, try again!\n')
            continue

        if guess in letters:
            letters.remove(guess)
            index = word.find(guess)
            display = display[:index] + guess + display[index + 1:]

        else:
            guessed.append(guess)
            count += 1
            if count == 1:
                time.sleep(1)
                print('   _____ \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '  |      \n'
                    '__|__\n') 
