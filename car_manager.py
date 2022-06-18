from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.shapesize(stretch_wid=1 , stretch_len=2)
        self.penup()
        self.color(random.choice(COLORS))
        self.setheading(180)



class Cars(CarManager):
    def __init__(self):
        super().__init__()
        self.showturtle()
        self.goto(x=300, y=(random.randint(-250, 250)))
        self.increase = 0

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE + self.increase)

    def increaseSpeed(self, increaseBy):
        self.increase = self.increase + increaseBy