# Day 8

# Function and Inputs

def greet():
    print("Hello. Welcome to Day 8.")
    print("Today, we will talk more about Function and Inputs.")
    print("Good luck.! \n")


greet()


# Function that allows for input

def greet_with_name(name):
    print(f"Hello {name}. Welcome to Day 8.")
    print("Today, we will talk more about Function and Inputs.")
    print("Good luck.! \n")


greet_with_name("Andar")


# Function with more than 1 input


def greet_with(name, location):
    print(f"Hello {name}. Welcome to Day 8.")
    print(f"You are live at {location}. \n")


greet_with("Andar", "Sydney")
greet_with(location="Melbourne", name="Andy")
