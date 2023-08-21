# Exercise 5: Make a Spirograph

from turtle import Turtle
import turtle as t

import random

timmy = Turtle()
t.colormode(255)
directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


timmy.speed("fastest")
draw_spirograph(5)

screen = t.Screen()

screen.exitonclick()
