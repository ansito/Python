# Exercise 2: Replacing Blanks with Guesses

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# create a blank list
display = []

print(f"Pssst, the solution is {chosen_word}")

# convert to list for chosen_word
chosen_word = list(chosen_word)

# prompt user input guess
guess = input("Guess a letter: ").lower()

# check the letter, if same, print out the same letter
for idx, letter in enumerate(chosen_word):
    if letter == guess:
        display.append(letter)
    else:
        display.append("_")

# print out the list_chosen
print(display)
