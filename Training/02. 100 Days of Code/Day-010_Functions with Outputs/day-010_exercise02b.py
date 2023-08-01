# Exercise 2: Calculator Part 1 - Combining Dictionaries and Functions

# add
def add(n1, n2):
    return n1 + n2


# subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


# create a new dictionary that the keys are the symbols, and the values are the name of functions
operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide}


# create function the calculator, if the user wants to refresh the calculator
def calculator():

    # receive input num1
    num1 = int(input("What's the first number?: "))

    # print the operator first
    for symbol in operations:
        print(symbol)

    # set flag should_continue
    should_continue = True

    while should_continue:

        # receive input operator
        opt = input("Pick an operation from the line above: ")

        # receive input num2
        num2 = int(input("What's the next number?: "))

        # define calculation function to store the values of the key
        calculation_function = operations[opt]

        # operations[opt] values is a function, so use it to calculate num1 and num2 and store it into answer
        answer = calculation_function(num1, num2)

        # print out the answer
        print(f"{num1} {opt} {num2} = {answer}")

        # prompt the user about the choice
        choice = input(f"Type 'y' to continue calculating with {answer}, or "
                       f"type 'n' to start a new calculation: \n").lower()

        # if choice = y
        if choice == "y":

            # put the answer into num1
            num1 = answer
            # should_continue = True

        elif choice == "n":
            # refresh the calculator, and start again from the beginning
            calculator()

        else:
            # end the program by exit the while loop
            should_continue = False


# Main Program
calculator()
