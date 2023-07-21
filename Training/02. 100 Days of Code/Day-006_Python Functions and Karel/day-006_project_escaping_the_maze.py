# Project: Escaping the Maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()


# Main Program

while not at_goal():

    # if it is wall in front

    if wall_in_front() and not right_is_clear():
        turn_left()

    elif wall_in_front() and right_is_clear():
        turn_right()
        move()

    else:
        # no wall in front
        if not right_is_clear():
            move()

        else:
            turn_right()
            move()