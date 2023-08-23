# Day 19 - Instances, State, and Higher Order Functions

from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator(n1, n2, func):
    return func(n1, n2)


# listen() will listen key that be pushed, and fun means action if the key be pushed
screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()

result = calculator(2, 3, divide)
print(result)

print(tim.xcor())
print(tim.color())

color = tim.color()
print(color[0])
