from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, win_condition=5) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.win_condition = win_condition
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto((-100, 200))
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto((100, 200))
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def announce_winner(self):
        self.goto((0, 0))
        self.write(
            f"The winner is {'left player' if self.l_score == self.win_condition else 'right player'}",
            align="center",
            font=("Courier", 20, "normal"),
        )

    def continue_game(self):
        return self.l_score == self.win_condition or self.r_score == self.win_condition
