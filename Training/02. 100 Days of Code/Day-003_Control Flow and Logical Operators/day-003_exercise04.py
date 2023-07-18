# Exercise 4: Pizza Order Practice

print("Welcome to Python Pizza Deliveries!")
size = input("What size do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# put the price
if size == "S":
    price = 15

    # additional price for pepperoni on small pizza
    if add_pepperoni == "Y":
        price += 2

elif size == "M":
    price = 20

    # additional price for pepperoni on medium pizza
    if add_pepperoni == "Y":
        price += 3

else:
    price = 25

    # additional price for pepperoni on larger pizza
    if add_pepperoni == "Y":
        price += 3

# additional price for extra cheese for all size pizza
if extra_cheese == "Y":
    price += 1

# print the total price
print(f"Your final bill is: ${price}.")
