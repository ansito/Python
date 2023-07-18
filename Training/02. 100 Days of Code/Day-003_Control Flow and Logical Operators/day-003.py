# Day 3 - Conditional Statements, Logical Operators, Code Blocks, and Scope

# Conditional Statements
# Nested If Statement and Elif Statements
# If and Elif Statements
# Multiple If Statements in Succession
# Logical Operators : AND, OR, NOT

print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))

    if age < 12:
        bill = 5
        print("Child tickets are $5.")

    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")

    elif age >= 45 and age <= 55:
        bill = 0

    else:
        bill = 12

    # asking if you want photo
    wants_photo = input("Do you want a photo taken? Y or N. ")

    if wants_photo == "Y":
        # Add $3 to their bill
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
