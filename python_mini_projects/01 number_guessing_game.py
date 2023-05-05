'''
computer guess
user input
conditional check
answer
'''

import random

def guessing_game():
    computer_answer = random.randint(0,100)

    while True:
        user_guess = int(input('What is your guess?  '))

        if user_guess ==  computer_answer:
            print(f'Right! The answer is {user_guess}')
            break

        elif user_guess < computer_answer:
            print(f'Your guess of {user_guess} is too low.')

        else:
            print(f'Your guess of {user_guess} is too high.')

guessing_game()
