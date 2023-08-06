# Project: Blackjack

import random
from art import logo


# 1: create function if user or computer has a blackjack
def has_blackjack(deck_cards):
    blackjack = []

    for idx in deck_cards:
        # save position for card Ace or card 10 into a list
        if idx == 11:
            blackjack.append(idx)

        elif idx == 10:
            blackjack.append(idx)

    # if n == 2, it means card has Blackjack (10 and 11)
    if 10 in blackjack and 11 in blackjack:
        return True

    else:
        return False


# 2: create function to count the total value of cards
def count_cards(deck_cards):
    # define sum_card as variable to store the total value of cards
    sum_card = 0

    for card in deck_cards:
        sum_card += card

    return sum_card


# 3: create function to check if card user more than 21
def user_card_more_21(deck_cards):
    if count_cards(deck_cards) > 21:
        return True

    else:
        return False


# 4: create function to check if card computer more than 17
def comp_card_less_17(deck_cards):
    if count_cards(deck_cards) <= 17:
        return True

    else:
        return False


# 5: create function to check if there is "Ace" on the cards
def has_ace(deck_cards):
    for card in deck_cards:
        if card == 11:
            return True

        else:
            return False


# 6: create function to check if a user has "Ace" but the total score is lower than 21
def has_ace_lower_21(deck_cards):
    pos = deck_cards.index(11)

    # change Ace to be 1
    deck_cards[pos] = 1

    # count the cards
    if count_cards(deck_cards) <= 21:
        return True
    else:
        return False


# 7: create function to ask if player wants to play again or not
def ask_to_play():
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if choice == "y":
        return True
    else:
        return False


# 8: create the function to ask if the player wants Hit or Stand
def hit_or_stand(deck_cards, card_players, card_comps, money, bids):
    choice_player = input("Type 'y' to HIT, type 'n' to STAND: ").lower()

    # if player chose "y"
    if choice_player == "y":
        card_players.append(deck_cards[-1])
        deck_cards.pop()

        # if card player > 21
        if count_cards(card_players) > 21:
            print(f"Your cards: {card_players}. The sum is {count_cards(card_players)}.")
            print(f"Computer cards: {card_comps}. The sum is {count_cards(card_comps)}.")
            print("I am sorry. Your cards are more than 21. Computer Win!")
            money -= bids

        elif count_cards(card_players) > count_cards(card_comps):
            print(f"Your cards: {card_players}. The sum is {count_cards(card_players)}.")
            print(f"Computer cards: {card_comps}. The sum is {count_cards(card_comps)}.")
            print("Congratulations. Your cards are bigger than computer. Player Wins!")
            money += bids

        else:
            print(f"Your cards: {card_players}. The sum is {count_cards(card_players)}.")
            print(f"Computer cards: {card_comps}. The sum is {count_cards(card_comps)}.")
            print("I am sorry. Your cards are lower than computer. Computer Wins!")
            money -= bids

    # if player chose "n"
    else:

        # while loop to make card of computer more than 17
        while comp_card_less_17(card_comps):
            card_comps.append(deck_cards[-1])
            deck_cards.pop()

        if count_cards(card_comps) > 21:
            print(f"Your cards: {card_players}. The sum is {count_cards(card_players)}.")
            print(f"Computer cards: {card_comps}. The sum is {count_cards(card_comps)}.")
            print("Congratulations. Computer's cards are more than 21. Player Win!")
            money += bids

        else:
            if count_cards(card_players) > count_cards(card_comps):
                print(f"Your cards: {card_players}. The sum is {count_cards(card_players)}.")
                print(f"Computer cards: {card_comps}. The sum is {count_cards(card_comps)}.")
                print("Congratulations. Your cards are bigger than computer. Player Wins!")
                money += bids

            elif count_cards(card_players) < count_cards(card_comps):
                print(f"Your cards: {card_players}. The sum is {count_cards(card_players)}.")
                print(f"Computer cards: {card_comps}. The sum is {count_cards(card_comps)}.")
                print("I am sorry. Your cards are lower than computer. Computer Wins!")
                money -= bids

            else:
                print(f"Your cards: {card_players}. The sum is {count_cards(card_players)}.")
                print(f"Computer cards: {card_comps}. The sum is {count_cards(card_comps)}.")
                print("OMG. Your cards are same total with the computer. Draw!")

#    print(f"Player's money: ${money}")
    return money


# 9: create a function to check the card
def check_card(deck_cards, card_players, card_comps, money, bids):
    # check if a user or computer has a blackjack
    if has_blackjack(card_players):
        print("Player has BLACKJACK!")
        print("Player Win!")
        money += bids

    elif has_blackjack(card_comps):
        print("Computer has BLACKJACK!")
        print("Computer Win!")
        money -= bids

    else:
        if user_card_more_21(card_player):

            # check if user has ace
            if has_ace(card_players):
                if has_ace_lower_21(card_players):
                    # put ask the user if they want to get another card
                    hit_or_stand(deck_cards, card_players, card_comps, money, bids)

                else:
                    print(f"Your cards: {card_players}. The sum is {count_cards(card_players)}.")
                    print(f"Computer cards: {card_comps}. The sum is {count_cards(card_comps)}.")
                    print("I am sorry. Although Ace card become 1, your cards are still more than 21. Computer Win!")
                    money -= bids

            # if card player > 21 and no ace card inside.
            else:
                print(f"Your cards: {card_players}. The sum is {count_cards(card_players)}.")
                print(f"Computer cards: {card_comps}. The sum is {count_cards(card_comps)}.")
                print("I am sorry. Your cards are more than 21. Computer Win!")
                money -= bids

        # if user has card lower than 21
        else:
            money = hit_or_stand(deck_cards, card_players, card_comps, money, bids)

    return money


# main program

# define variable
play_game = True
budget_player = 0

print(logo)

budget = int(input("Please input your budget: $ "))

while play_game and budget > 0:

    print("\n## Start a new round of the game! ##")

    # ask the bidding
    bidding = int(input("Put the bid: $ "))

    # define variable
    # card
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_player = []
    card_comp = []

    # shuffle cards
    random.shuffle(cards)

    # define card for player and computer
    for index in range(2):
        card_player.append(cards[-1])
        cards.pop()
        card_comp.append(cards[-1])
        cards.pop()

    # Show player card
    print(f"Your cards: {card_player}")
    print(f"Computer's first card:  {card_comp[0]}")

    # add up the user's and the computer's scores
    sum_card_player = count_cards(card_player)
    sum_card_comp = count_cards(card_comp)

    # check card if there is blackjack, ace
    budget_player = check_card(cards, card_player, card_comp, budget, bidding)

    # print money
    print(f"Player's money: ${budget_player}")
    budget = budget_player

    if ask_to_play():
        play_game = True
    else:
        play_game = False
        print("Thank you for playing the game!")
