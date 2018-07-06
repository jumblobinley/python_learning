#4_5_hangman_play.py

import random

def pick_a_word():
    return random.choice (words)

def play ():
    word = pick_a_word()
    while True:
        guess = get_guess(word)
        if process_guess(guess, word):
             print ('You win! Well Done!')
             break
        if lives_remaining == 0:
            print ('You are Hung!')
            print ('the word was: ' + word)
            break
        
def get_guess(word):
    print ('getting guess')
    return 'a'

def process_guess (guess, word):
    global lives_remaining
    lives_remaining = lives_remaining - 1
    print (lives_remaining)
    return False


#mainline program

words = ['chicken', 'dog', 'cat', 'mouse', 'frog']
print(pick_a_word())

lives_remaining = 14

#Call the first function
play()

