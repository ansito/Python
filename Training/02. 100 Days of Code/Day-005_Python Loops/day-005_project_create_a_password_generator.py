import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Expert level

# random for letter
random_letters = ""

for letter in range(0, nr_letters):
    random_letters += random.choice(letters)

# random for symbols
random_symbols = ""

for symbol in range(0, nr_symbols):
    random_symbols += random.choice(symbols)

# random for numbers
random_numbers = ""

for number in range(0, nr_numbers):
    random_numbers += random.choice(numbers)

# combine password
random_password = random_letters + random_symbols + random_numbers

# shuffle combine password
# shuffle function need list input

# convert the random_password into a list
random_password = list(random_password)

# shuffle the random_password list
random.shuffle(random_password)

# convert the shuffle random list into string, assign it to new variable new_random_password
new_random_password = ""

for random_pass in random_password:
    new_random_password += random_pass

# print out the new strong password
print(f"Here is your password: {new_random_password}")
