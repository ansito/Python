# Exercise 4: Keep Track of the Player's Lives

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# list of word
word_list = ["aardvark", "baboon", "camel"]

# choose a random word as a string
chosen_word = random.choice(word_list)

# count a length of the chosen word
word_length = len(chosen_word)

# count a length of stages
stages_length = len(stages)

# define lives for player
lives = 6

# set play_on = True
play_on = True

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

# Check guessed letter
while lives != 0:

    guess = input("Guess a letter: ").lower()

    # do loop check one by one letter in chosen word
    for idx in range(word_length):

        # if guess same with the current letter index of chosen word then change list display index to the guess
        if guess == chosen_word[idx]:
            display[idx] = guess

        # if display[idx] is not "_", it means that it is already contain of correct letter, so do not change it.
        elif display[idx] != "_":
            display[idx] = display[idx]

        else:
            display[idx] = "_"

    # print out the current display
    print(display)

    # for each guess, it will reduce -1 of lives.
    lives = lives - 1

    # check if all guess has been completed, and lives is still no 0, then while loop was over
    if display == list(chosen_word):

        # exit for while loop if actually lives i
        print("You win.")
        lives = 0

    # check if lives is not 0, always print stages
    elif lives != 0:
        print(stages[lives])

    # check if lives is 0, but the last guess is correct, so it will be a win, and not print the stages
    elif lives == 0 and display == list(chosen_word):
        print("You win.")

    # when the live is 0, and the guess is not completed.
    else:
        print("You lose.")
        print(stages[lives])
