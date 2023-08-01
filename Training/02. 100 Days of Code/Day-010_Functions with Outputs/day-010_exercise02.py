# Exercise 2: Calculator Part 1: Combining Dictionaries and Functions

# call art.py and import logo
from art import logo

# import module os to clear screen later
import os

# Define variable
play_on = True


# define function for choice +, -, *, /

def operator():
    # print the list of operation
    return """
    +
    -
    *
    /
    """


# define calculate function
def calculate(num_one, num_two, opt):
    # if opt = "+"
    if opt == "+":
        total = num_one + num_two
        print(f"{num_one} + {num_two} = {total}")

    # if opt = "-"
    elif opt == "-":
        total = num_one - num_two
        print(f"{num_one} - {num_two} = {total}")

    # if opt = "*"
    elif opt == "*":
        total = num_one * num_two
        print(f"{num_one} * {num_two} = {total}")

    # if opt = "/"
    elif opt == "/":
        total = num_one / num_two
        print(f"{num_one} / {num_two} = {total}")

    # if opt is different, so print out the invalid input operation
    else:
        total = ""
        print("Invalid input operation.!")

    return total


# define function program_part_one as the first program
def program_part_one():
    # print the logo
    print(logo)

    # prompt the input user for first number
    nums = int(input("What's the first number?: "))

    # print the operator
    print(operator())

    return nums


# define function program_part_two as the second program
def program_part_two(num1):
    # put the input parameter as a first_num
    first_num = num1

    # prompt the input user for operator chosen
    chose_opt = input("Pick an operation: ")

    # prompt the input user for second number
    second_num = int(input("What's the next number?: "))

    # calculate the numbers and store into total_now
    total_now = calculate(first_num, second_num, chose_opt)

    return total_now


# main program

# store the first_digit
first_digit = program_part_one()

# run the program_part_two, and store the return value of total_now
total_digit = program_part_two(first_digit)

# put the while loop here because the choice could be many times
while play_on:

    # ask if you want to continue
    choice = input(f"Type 'y' to continue calculating with {total_digit}, "
                   f"type 'n' to start a new calculation "
                   f"or type 'x' to exit the program: \n").lower()

    if choice == "y":
        total_digit = program_part_two(total_digit)

        # put play_on = True, will make it back to the first condition of while loop
        play_on = True

    # if choice = "n"
    elif choice == "n":

        # clear screen
        os.system('cls')

        # run program from starting point
        first_digit = program_part_one()
        total_digit = program_part_two(first_digit)

        # put play_on = True, will make it back to the first condition of while loop
        play_on = True

    elif choice == "x":

        # put play_on = False, will make it will be exited from the while loop
        play_on = False
