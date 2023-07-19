# Day 4 - Randomisation and Python Lists

# import Random and Module
import random
import my_module

# random integer, between 1 to 9
random_integer = random.randint(1, 10)
print(random_integer)

# random float, between 0.0 to 4.999
random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

print(my_module.pi)
print("\n")

# Lists
# ex: fruits = [item1, item2]

states_of_america = ["Delaware", "Pennsylvania", "Michigan", "Utah", "Oklahoma"]

print(states_of_america[0])
print(states_of_america[-1])
print(states_of_america[::-1])

states_of_america.append("Andar")
print(states_of_america)

states_of_america.extend(["Iowa", "Colorado"])
print(states_of_america)

# Nested List
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen[0][1])