# Exercise 02: Draw a Dashed Line

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

for _ in range(15):
    tim.forward(10)     # tim forward with condition drawing
    tim.penup()         # pen is up, means no drawing while moving
    tim.forward(10)     # tim forward with condition no drawing
    tim.pendown()       # pen is down, means pen is ready to drawing if next action is moving

screen.exitonclick()
