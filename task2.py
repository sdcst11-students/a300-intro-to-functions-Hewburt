"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""
import random
def title():
    print("Welcome to the Number Guessing Game!")
    print("Instructions:")
    print("1. I will think of a random number between 1 and 100.")
    print("2. You have to guess the correct number.")
    print("3. I will provide feedback on whether your guess is too high, too low, or correct.")
    print("Let's see if you can guess the number!\n")
def game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10  
    print("I've picked a number between 1 and 100. Can you guess it?\n")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        attempts += 1
        if guess == secret_number:
            print(f"Congratulations! You've guessed the correct number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
    if attempts == max_attempts:
        print(f"\nSorry, you've run out of attempts. The correct number was {secret_number}.")
title()
game()
