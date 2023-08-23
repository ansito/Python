# Project: Turtle Race

# import
from turtle import Turtle, Screen
from art import logo
import random

# create an object from Turtle and Screen class
screen = Screen()

# define global variable
is_race_on = False

screen.setup(500, 400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# create finish line
finish_line = Turtle()

finish_line.hideturtle()
finish_line.penup()
finish_line.goto(150, 100)
finish_line.right(90)
finish_line.pendown()
finish_line.pensize(5)
finish_line.goto(150, -100)


# main program
print(logo)

for num in range(6):

    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[num])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[num])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for member in all_turtles:
        move = random.randint(0, 10)
        member.forward(move)

        if member.xcor() > 150:

            is_race_on = False

            if member.pencolor() == user_bet:
                print(f"Congratulation!! Your guess '{user_bet}' is the winner.")

            else:
                print(f"I am sorry. Your guess '{user_bet}' is not the winner.")
                print(f"The winner is '{member.pencolor()}'.")

screen.exitonclick()
