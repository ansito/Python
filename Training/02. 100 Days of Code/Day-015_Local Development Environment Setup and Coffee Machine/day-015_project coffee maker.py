# Project: Coffee Maker Machine

# import module
from main import menu, resources
from art import logo

# define a global variable
# define a new variable to store resource information
stock = resources
# add "money" as a new key in the stock dictionary
stock["money"] = 0
play_game = True


# 1. create a new function to ask what user like
def ask_you_like():
    print("The menu: 'Espresso', 'Latte', 'Cappuccino', 'Report', 'Off'.")
    choice = input("    What would you like?: ").lower()

    return choice


# 2. create a new function to process the choice
def proceed_choice(current_stock, choice):
    # define local variable
    need_water = 0
    need_coffee = 0
    need_milk = 0
    bill = 0

    val_water = current_stock["water"]
    val_milk = current_stock["milk"]
    val_coffee = current_stock["coffee"]
    val_money = current_stock["money"]

    if choice == "espresso":
        need_water = menu["espresso"]["ingredients"]["water"]
        need_coffee = menu["espresso"]["ingredients"]["coffee"]
        bill = 1.5

    elif choice == "latte":
        need_water = menu["latte"]["ingredients"]["water"]
        need_milk = menu["latte"]["ingredients"]["milk"]
        need_coffee = menu["latte"]["ingredients"]["coffee"]
        bill = 2.5

    elif choice == "cappuccino":
        need_water = menu["cappuccino"]["ingredients"]["water"]
        need_milk = menu["cappuccino"]["ingredients"]["milk"]
        need_coffee = menu["cappuccino"]["ingredients"]["coffee"]
        bill = 3.0

    else:
        print("You give invalid input.")

    val_water -= need_water
    val_milk -= need_milk
    val_coffee -= need_coffee
    val_money += bill

    if val_water >= 0 and val_milk >= 0 and val_coffee >= 0:
        # change the current stock
        current_stock["water"] = val_water
        current_stock["milk"] = val_milk
        current_stock["coffee"] = val_coffee
        current_stock["money"] = val_money
        return True

    elif val_water < 0:
        print("    Sorry, there is not enough water.")
        return False

    elif val_milk < 0:
        print("    Sorry, there is not enough milk.")
        return False

    elif val_coffee < 0:
        print("    Sorry, there is not enough coffee.")
        return False


# 3. create a new function to calculate the value of coins
def insert_coins():
    # define local variable for coins
    val_quarters = 0.25
    val_dimes = 0.10
    val_nickles = 0.05
    val_pennies = 0.01

    print("    Please insert coins.")
    num_quarters = int(input("    How many quarters @ $0.25 ?: ")) * val_quarters
    num_dimes = int(input("    How many dimes @ $0.10 ?: ")) * val_dimes
    num_nickles = int(input("    How many nickles @ $0.05 ?: ")) * val_nickles
    num_pennies = int(input("    How many pennies @ $0.01 ?: ")) * val_pennies

    total_coins = num_quarters + num_dimes + num_nickles + num_pennies

    return total_coins


# 4. create a new function to check input coins more than the price of coffee
def calculate_coins(sum_coins, choice):
    # local variable
    price = 0

    # put the price for each choice
    if choice == "espresso":
        price = menu["espresso"]["cost"]

    elif choice == "latte":
        price = menu["latte"]["cost"]

    elif choice == "cappuccino":
        price = menu["cappuccino"]["cost"]

    change = round(sum_coins - price, 2)

    # check if there is change
    if change > 0:
        print(f"    Here is ${change} in change.")
        return True

    # if there is no change or coins, are not enough to buy a coffee
    elif change < 0:
        print("    Sorry that's not enough money. Money refunded.")

        return False


# 5. create a new function to check if the money is enough to buy coffee
# def is_coins_enough(choice, sums)

# main program
print(logo)
while play_game:
    user_choice = ask_you_like()

    if user_choice == "off":
        # exit the game
        play_game = False
        print("Thank you for playing the game.")

    elif user_choice == "report":

        # print the report
        print(f"    Water: {stock['water']} ml.")
        print(f"    Milk: {stock['milk']} ml.")
        print(f"    Coffee: {stock['coffee']} gram.")
        print(f"    Money: ${stock['money']}.")
        play_game = True

    else:

        if proceed_choice(stock, user_choice):
            coins = insert_coins()
            if user_choice == "espresso":
                prices = 1.5
                if coins > prices:
                    calculate_coins(coins, user_choice)
                    print(f"    Here is your {user_choice} ☕. Enjoy!")

                else:
                    calculate_coins(coins, user_choice)

            elif user_choice == "latte":
                prices = 2.5

                if coins > prices:
                    calculate_coins(coins, user_choice)
                    print(f"    Here is your {user_choice} ☕. Enjoy!")

                else:
                    calculate_coins(coins, user_choice)

            elif user_choice == "cappuccino":
                prices = 3.0

                if coins > prices:
                    calculate_coins(coins, user_choice)
                    print(f"    Here is your {user_choice} ☕. Enjoy!")

                else:
                    calculate_coins(coins, user_choice)

        else:
            play_game = True
