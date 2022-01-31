from turtle import Turtle
from typing import Tuple, Sequence


class Paddle(Turtle):

    def __init__(self, position: Tuple[int, int]) -> None:
        super().__init__(shape="square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
