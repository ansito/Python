# Day 10: Building the Snake Game Part 1

"""
Step by step creating Snake Game:
1. Create snake body
2. Move the snake
3. Control the snake
4. Detect Collision with food
5. Create a scoreboard
6. Detect collision with wall
7. Detect collision with tail
"""

from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to Snake Game")
screen.tracer(0)

# define global variable
segments = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]


for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


is_move = True
while is_move:

    screen.update()
    time.sleep(0.1)

    # to move the snake,
    # the last segment coordinate follows the front segment coordinate (reverse)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()

        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)
    segments[0].left(90)
