from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.value = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.display()

    # create a method for display
    # remember: we do not have to assign a new object here
    # because self() itself is already an object
    # we have defined inheritance a Turtle class before in __init__(self) as super()
    def display(self):

        self.goto(0, 280)
        self.write(f"Your Score : {self.value}", True, ALIGNMENT, FONT)

    def add_score(self):

        self.value += 1
        self.clear()
        self.display()

    def game_over(self):

        self.goto(0,0)
        self.write("GAME OVER!", False, ALIGNMENT, FONT)

