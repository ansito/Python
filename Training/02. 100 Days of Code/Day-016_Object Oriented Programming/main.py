# test
import another_module
print(another_module.another_variable)

# Turtle() is a class
# turtle is a module
# create a new object of turtle called timmy

# import turtle
from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

# Object Attributes
# object.attributes
my_screen = Screen()
print(my_screen.canvheight)

# Object Methods
# object.methods
# my_screen.exitonclick()

from prettytable import PrettyTable
# create a new variable from class PrettyTable
table = PrettyTable()

print(table.align)
# object methods
table.add_column("Pokemon Name", ["Pikachu", "Squirrel", "Chandelier"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# object attributes
table.align = "l"
print(table)
