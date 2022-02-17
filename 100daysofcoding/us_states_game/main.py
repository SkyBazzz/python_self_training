from turtle import Screen, Turtle
from typing import List

import pandas

screen = Screen()
screen.setup(width=725, height=491)
screen.title("US states game")
screen.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")

turtle = Turtle()
turtle.penup()
turtle.hideturtle()
all_states: List[str] = data.state.to_list()
guessed_states = list()


def show_missing_states():
    missing_states = [state for state in all_states if state not in guessed_states]
    missing_data = pandas.DataFrame(missing_states)
    missing_data.to_csv("missing_states.csv")


def check_attempt(user_guess: str):
    if user_guess in data.state.to_list():
        turtle.goto(
            int(data[data.state == user_guess].x), int(data[data.state == user_guess].y)
        )
        turtle.write(user_guess)
        guessed_states.append(user_guess)


def remember_all_states():
    if len(guessed_states) == 50:
        turtle.goto(0, 0)
        turtle.write("You remember all states")


for _ in range(1, 51):
    attempt = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct", prompt="Enter a state: "
    ).title()
    if attempt == "Exit":
        show_missing_states()
        break

    check_attempt(attempt)
    remember_all_states()

else:
    show_missing_states()

screen.exitonclick()
