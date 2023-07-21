# Exercise 2: Reeborg's World Hurdle 4

def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_right()
    move()
    turn_right()


# Main Program

while not at_goal():
    if wall_in_front():
        turn_left()

        while wall_on_right():
            move()

        jump()
        move()

        while not wall_in_front():
            move()

        turn_left()

    else:
        move()



