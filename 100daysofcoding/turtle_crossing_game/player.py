from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
Y_FINISH_LINE = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__(shape="turtle")
        self.color("green")
        self.penup()
        self.left(90)
        self.go_to_start()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        return self.ycor() > Y_FINISH_LINE

    def go_to_start(self):
        self.goto(STARTING_POSITION)
