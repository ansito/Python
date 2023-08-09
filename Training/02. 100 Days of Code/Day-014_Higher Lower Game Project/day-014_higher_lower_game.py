# Project: Higher Lower Game

# import module
import random
from art import logo, vs
from game_data import data

# define global variable
list_data = data


# 1. create a new function for random A
def random_generate_a():
    data_a = random.choice(list_data)

    return data_a


# 2. create a new function for random B
def random_generate_b():
    data_b = random.choice(list_data)

    return data_b


# 3. create a function to check random a and b is not the same
def is_random_different(random_a, random_b):
    while random_a == random_b:
        random_a = random_generate_a()
        random_b = random_generate_b()

    return True


# 4. make a new function to compare the num of follower between A and B
def check_follower(random_a, random_b):
    # define variable for value a and b to store the follower value
    value_a = random_a["follower_count"]
    value_b = random_b["follower_count"]

    # define return 0 if value_a > value_b
    if value_a > value_b:
        return 0

    else:
        return 1


# 5. create a new function to print out the part A and B
def show_versus(random_a, random_b):
    number = 2

    # print part A
    print(f"Compare A: {random_a['name']}, a {random_a['description']}, from {random_a['country']}.")

    # print versus
    print(vs)

    # print part B
    print(f"Against B: {random_b['name']}, a {random_b['description']}, from {random_b['country']}.")

    # prompt user input to choose
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    # assign a new variable number to store the choice
    if choice == "a":
        number = 0

    elif choice == "b":
        number = 1

    else:
        print("Game Over. You give the invalid input!")

    return number


# 6. make a new function to play a game
def play_game():

    not_mistake = True
    score = 0

    # print logo
    print(logo)

    b = random_generate_b()

    # make sure random A is not the same with random B
    while not_mistake:

        # define variable for part A
        a = b
        b = random_generate_b()

        # make random A and B would not be the same
        is_random_different(a, b)

        # call show_versus function
        if show_versus(a, b) == check_follower(a, b):
            score += 1
            print(f"You're right! Current Score: {score}.")
            not_mistake = True

        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            print("Thank you for playing the game!")
            not_mistake = False


# main program
play_game()
