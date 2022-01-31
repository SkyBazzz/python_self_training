from turtle import Turtle
from typing import List

LEFT = 180

RIGHT = 0

DOWN = 270

UP = 90


class Snake:
    STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_DISTANCE = 20

    def __init__(self) -> None:
        self.segments: List[Turtle] = list()
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in self.STARTING_POSITION:
            self.add_segment(position)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[number - 1].xcor()
            new_y = self.segments[number - 1].ycor()
            self.segments[number].goto(new_x, new_y)
        self.head.forward(self.MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
