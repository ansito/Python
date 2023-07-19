# Project: Rock, Paper, Scissors

# import random module
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# make a list for rock, paper, and scissors as rps, to draw a picture of choice
rps = [rock, paper, scissors]

# prompt the input user
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

# if user input wrong number, then print error
if user_choice >= 3:
    print("You typed an invalid number, you lose! ")

else:
    # print the image of user choice
    print(rps[user_choice])

    # generate random number by computer
    comp_choice = random.randint(0, 2)
    print("Computer chose: ")

    # print the image of computer choice
    print(rps[comp_choice])

    # make a rule for win or lose condition
    if user_choice == 0 and comp_choice == 2:
        print("You win")

    elif user_choice == 2 and comp_choice == 1:
        print("You win")

    elif user_choice == 1 and comp_choice == 0:
        print("You win")

    elif user_choice == comp_choice:
        print("You draw")
    else:
        print("You lose")
