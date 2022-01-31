import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-290, 290)
        rand_y = random.randint(-290, 290)
        self.goto(rand_x, rand_y)
