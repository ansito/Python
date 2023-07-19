# Exercise 2 - Banker Roulette

# import random module
import random

# Split string method
name_string = input("Give me everybody's names, separated by a comma.\n")
names = name_string.split(", ")

# store the names of the list using len()
sum_names = len(names)

# generate a randomization number to choose the index names
random_index_names = random.randint(0, sum_names - 1)

# print out the names who will pay the meal
print(f"{names[random_index_names]} is going to buy the meal today!")
