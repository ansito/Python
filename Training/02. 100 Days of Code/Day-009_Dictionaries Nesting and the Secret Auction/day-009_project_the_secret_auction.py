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


# define function to find the largest bid, by input as a dictionary

def find_largest_bidder(bidding_record):

    # define variable max_bid and winner
    max_bid = 0
    winner = ""

    # do loop for every "keys" in dictionary, to give output "values"
    for bidder in bidding_record:

        # if dict_bid[idx] > max_bid
        if bidding_record[bidder] > max_bid:
            max_bid = bidding_record[bidder]
            winner = bidder

    # print out the bidder
    print(f"The winner is {winner} with a bid of ${max_bid}.")


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

        # run the function find_largest_bidder
        find_largest_bidder(add_bidder)
