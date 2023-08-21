# Exercise 01: Draw a Square

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.shape("turtle")
tim.color("blue")

for index in range(5):
    tim.forward(100)
    tim.right(90)

screen.exitonclick()
