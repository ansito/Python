# Exercise 3: Checking if the Player has Won

#  TODO-1: - Use a while loop to let the user guess again.
#  The loop should only stop once the user has guessed all the letters in the chosen_word
#  and 'display' has no more blanks ("_"). Then you can tell the user they've won.

import random
word_list = ["aardvark", "baboon", "camel"]

# choose a random word as a string
chosen_word = random.choice(word_list)

# count a length of the chosen word
word_length = len(chosen_word)

# set play_on = True
play_on = True

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

#  TODO-1: - Use a while loop to let the user guess again.
#   The loop should only stop once the user has guessed all the letters in the chosen_word
#   and 'display' has no more blanks ("_"). Then you can tell the user they've won.

# Check guessed letter
while play_on:
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

    print(display)

    # check if all guess has been completed, then while loop was over
    if display == list(chosen_word):

        # exit for while loop
        print("You win.")
        play_on = False
