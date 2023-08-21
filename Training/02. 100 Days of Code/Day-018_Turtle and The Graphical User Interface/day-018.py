# Day 18: Turtle and the Graphical User Interface

from turtle import Turtle, Screen

# crete objects
tim = Turtle()
screen = Screen()

tim.shape("turtle")
tim.color("red")
tim.forward(100)
tim.right(90)

screen.exitonclick()

# Basic Import
import heroes
print(heroes.gen())

