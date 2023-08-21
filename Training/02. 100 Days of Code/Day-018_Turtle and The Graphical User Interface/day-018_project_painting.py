# Project: Painting

# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
# list_rgb = []
#
# for color in colors:
#
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#
#     tuple_rgb = (red, green, blue)
#     list_rgb.append(tuple_rgb)
#
# print(list_rgb)

from turtle import Screen
import turtle as turtle_module
import random

# important to put
turtle_module.colormode(255)
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

pick_color = random.choice(color_list)
tim = turtle_module.Turtle()
screen = Screen()
tim.speed(6)

n = -212.13

# get position
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

# start drawing
for column in range(10):

    for row in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()

        if row != 9:
            tim.forward(50)
            tim.pendown()

        else:
            tim.penup()

    n += 40
    tim.penup()

    if column != 9:
        tim.goto(-212.13, n)

screen.exitonclick()
