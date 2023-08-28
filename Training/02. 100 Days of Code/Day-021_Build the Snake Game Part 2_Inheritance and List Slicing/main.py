# 4: detect collisions with food

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # 4: detect collision with food
    # compare distance between object snake.head with object food
    if snake.head.distance(food) < 15:
        # change the position of food randomly
        food.refresh()
        # add a tail of the snake
        snake.extend()

        # 5: add scoreboard
        score.add_score()

    # 6: detect collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    # 7: detect collision with tail
    # if head collides with any segment in the tail
    # trigger game over

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
