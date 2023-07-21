# Exercise 2: Reeborg's World Hurdle 3

def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def start_moving():
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


# Main Program

while not at_goal():
    if wall_in_front():
        turn_left()
        move()
        start_moving()
    else:
        move()