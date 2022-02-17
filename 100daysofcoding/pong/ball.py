from turtle import Turtle

DEFAULT_SPEED = 0.1


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__(shape="circle")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = DEFAULT_SPEED
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto((0, 0))
        self.move_speed = DEFAULT_SPEED
        self.bounce_x()
