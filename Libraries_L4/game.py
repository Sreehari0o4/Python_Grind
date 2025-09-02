"""
Number Guessing Game
This script implements a simple number guessing game. The user is prompted to enter a positive integer as the upper bound (`level`) for the random number to guess. The program then generates a random integer between 1 and `level` (inclusive). The user repeatedly guesses the number, receiving feedback if their guess is too large, too small, or correct. Input validation ensures only positive integers are accepted for both the level and guesses.
# Problem Description:
The goal is to create an interactive guessing game where the user must guess a randomly chosen number within a specified range. The program provides hints and handles invalid inputs gracefully.
"""

import random

level = 0
while level <= 0 :
    level = int(input("Level: "))
rand = random.randint(1,level)
while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            raise ValueError
        if(guess == rand):
            print("Just right!")
            break
        elif(guess > rand):
            print("Too large!")
        else:
            print("Too small!")
    except ValueError:
        pass
