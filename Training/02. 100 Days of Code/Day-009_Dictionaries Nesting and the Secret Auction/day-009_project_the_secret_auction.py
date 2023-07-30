# Project: The Secret Auction Program

# import logo from art.py
from art import logo

# print the logo
print(logo)

# print welcome
print("Welcome to the secret auction program.")

# define bidding = True
bidding = True

# define a blank dictionary for store bidder
add_bidder = {}

# define largest bid as integer 0
largest_bid = 0

# define the name of the largest bid as a blank string
name_largest = ""


while bidding:

    # prompt the name of user
    input_name = input("What is your name?: ")

    # prompt the value of bid
    value_bid = int(input("What's your bid?: $"))

    # add to dictionary
    add_bidder[input_name] = value_bid

    # ask if there is other bid
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()

    if other_bidder == "yes":
        bidding = True
    else:
        bidding = False
        print(add_bidder)

        # check the largest bidder
        for names in add_bidder:

            # if the new bidder has a larger bid
            if add_bidder[names] > largest_bid:
                largest_bid = add_bidder[names]
                name_largest = names

            # if the new bidder has a lower bid than the current largest bidder
            else:
                largest_bid = largest_bid
                name_largest = name_largest

        # print out the name of the biggest bid and the value
        print(f"The winner is {name_largest} with a bid of ${largest_bid}.")
