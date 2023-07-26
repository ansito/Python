# Project: Hangman

# import module
import random
# import hangman_words.py as word
import hangman_words as word
# import hangman_art.py as art
import hangman_art as art

# call the word_list using module word.
chosen_word = random.choice(word.word_list)

# count a length of the chosen word
word_length = len(chosen_word)

# count a length of stages
stages_length = len(art.stages)

# define lives for player
lives = 6

# define a history guess as blank string
hist_guess = ""

# print the logo
print(art.logo)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create a blank list, and fill each member with "_"
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

    # if player guess a same word, it will not reduce lives
    if guess in hist_guess:
        print(f"You've already guess '{guess}' ")

    # if player guess a correct word in chosen_word, it will not reduce a life.
    elif guess in chosen_word:
        print(f"You guessed '{guess}' as a correct word. Keep Going.!")
        lives = lives

    elif guess in chosen_word and lives == 0:
        print(f"Hey I am sorry. You guess '{guess}' as a correct word, but life is empty.")

    else:
        # if the guess is not right, lives reduce -1
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")

    # record all input guess
    hist_guess += guess

    # == here is a step for print out art stages ==

    # check if all guess has been completed, and lives is still no 0, then while loop was over
    if display == list(chosen_word):

        # exit for while loop if actually lives i
        print("You win.")
        lives = 0

    # check if lives is not 0, always print stages
    elif lives != 0 and guess not in hist_guess:
        print(art.stages[lives])

    # check if lives is 0, but the last guess is correct, so it will be a win, and not print the stages
    elif lives == 0 and display == list(chosen_word):
        print("You win.")

    # when the live is 0, and the guess is not completed.
    elif lives == 0:
        print("You lose.")
        print(art.stages[lives])

    else:
        print(art.stages[lives])
