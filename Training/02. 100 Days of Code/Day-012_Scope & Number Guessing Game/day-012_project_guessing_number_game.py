# Project: Guessing Number Game

# import module
from art import logo
import random

# define global variable
easy_level = 10
hard_level = 5


# 1: define a function to generate a new list for number
def generate_list_number():
    numbers = []
    for number in range(1, 101):
        numbers.append(number)

    return numbers


# 2: define a function to choose the difficulty level
def level_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    # if level is an easy, so the attempts = 10, otherwise = 5
    if level == "easy":
        return easy_level

    else:
        return hard_level


# 3: define a function to guess a game
def guess_number(choice_level, chosen_number):
    guess_numbers = True
    try_guess = choice_level

    while try_guess > 0 and guess_numbers:

        print(f"You have {try_guess} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        # if guess is not correct, and higher than chosen number
        if guess != chosen_number and guess > chosen_number:
            print("Too High. Guess Again!")
            try_guess -= 1

        # if guess is not correct, and lower than chosen number
        elif guess != chosen_number and guess < chosen_number:
            print("Too Low. Guess Again!")
            try_guess -= 1

        # if guess is correct
        elif guess == chosen_number:
            print(f"You got it! The answer was {chosen_number}.")
            guess_numbers = False

        else:
            print("You give the wrong input. Insert number between 1-100.")

        if try_guess == 0:
            print("Game Over! You do not have any attempts.")
            print(f"The correct number is {chosen_number}.")
            print("Thank you for playing the game.")
            guess_numbers = False


# main program
print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a random number between 1 and 100.")

target_number = random.choice(generate_list_number())
level_game = level_difficulty()
guess_number(level_game, target_number)
