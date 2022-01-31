from turtle import Turtle

FONT = ("courier", 24, "normal")

ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)
