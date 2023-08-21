# Exercise 03: Drawing Different Shape
from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

# global variable
num_side = 3
color = ["darkgreen", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue"]


# create a new function choose color
def choose_color():
    global color

    random.shuffle(color)
    pick_color = random.choice(color)
    print(pick_color)
    color.remove(pick_color)
    print(color)

    return pick_color


# create a new function draw shape
def draw_shape(num_sides):
    angles = 360 / num_sides
    for line in range(num_sides):
        tim.right(angles)
        tim.forward(100)


for _ in range(10):

    tim.color(choose_color())
    draw_shape(num_side)
    num_side += 1

screen.exitonclick()
