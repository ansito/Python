# Day 10 - Functions with Outputs

def format_name(f_name, l_name):
    # give Upper Case for every first char in the word, and other char will be lowercase automatically
    first_name = f_name.title()
    last_name = l_name.title()

    return f"{first_name} {last_name}"


# must use print to run the function
print(format_name("andar", "COOL"))


# function with multiple outputs
def format_name(f_name, l_name):
    # if inputs are blanks
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"

    first_name = f_name.title()
    last_name = l_name.title()

    return f"{first_name} {last_name}"


print(format_name(input("What is your first name: "), input("What is your last name? ")))


# Docstring

def format_name(f_name, l_name):
    """ Take a first and last name and format it
    to return the title case version of the game
    """
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"

    first_name = f_name.title()
    last_name = l_name.title()

    return f"{first_name} {last_name}"

# Print vs Return
# Use print for the function will generate the print out of all print functions and return value
# Use return for the function. If we put some new variable, we could store only the return value into the variable
