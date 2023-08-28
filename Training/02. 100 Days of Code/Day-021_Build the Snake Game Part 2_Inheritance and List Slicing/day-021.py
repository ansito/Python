# day-021: build the snake game part 2 with Inheritance and List Slicing

# continue steps for making snake game:
# 4: detect collision with food
# 5: create a scoreboard
# 6: detect collision with wall
# 7: detect collision with tail

# class inheritance

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


# inheritance: class Fish use class Animal as a parameter
class Fish(Animal):

    def __init__(self):
        # call all attributes, methods from super class which is Animal class
        super().__init__()

    def breathe(self):
        # call a method breathe from the super-class Animal. use super() as a refer to superclass
        super().breathe()
        # action to print from local breathe function itself
        print("doing this underwater.")

    def swim(self):
        print("moving in the water.")


nemo = Fish()
nemo.swim()

# example that objects nemo could use attributes and methods from Animal class
nemo.breathe()
print(nemo.num_eyes)
