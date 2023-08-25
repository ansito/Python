# snake class

from turtle import Turtle
# define global variable
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
# 0 = goes right, 90 = goes up, 180 = goes left, 270 = goes down
DIRECTION = [0, 90, 180, 270]


class Snake:

    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):

        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()

            self.segments[seg_num].goto(new_x, new_y)

        # head of snake
        self.head.forward(MOVE_DISTANCE)

    def up(self):

        # if the current heading of head is not to the downside
        if self.head.heading() != DIRECTION[3]:
            self.head.setheading(DIRECTION[1])

    def down(self):

        # if the current heading of head is not to the upside
        if self.head.heading() != DIRECTION[1]:
            self.head.setheading(DIRECTION[3])

    def left(self):

        # if the current heading of head is not to the right side
        if self.head.heading() != DIRECTION[0]:
            self.head.setheading(DIRECTION[2])

    def right(self):

        # if the current heading of head is not to the left side
        if self.head.heading() != DIRECTION[2]:
            self.head.setheading(DIRECTION[0])
