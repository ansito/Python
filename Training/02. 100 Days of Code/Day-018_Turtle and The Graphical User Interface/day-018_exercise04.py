# Exercise 04: Draw a Random Walk

from turtle import Turtle, Screen
import turtle as t
import random

timmy = Turtle()
screen = Screen()
# define color mode on module t
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)
    return color


# color = ["darkgreen", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue"] color = [
# "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# ways: 0 = east, 90 = north, 180 = west, 270 = south
directions = [0, 90, 180, 270]


def pick_directions():
    global directions

    direction = random.choice(directions)
    return direction


timmy.pensize(10)
timmy.speed(3)


for _ in range(100):

    pick_way = pick_directions()

    # set color
    timmy.color(random_color())

    # start moving
    timmy.forward(20)
    timmy.setheading(pick_way)
    print(pick_way)

screen.exitonclick()
