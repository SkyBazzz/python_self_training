import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Input a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = list()

y_position = -100
x_start = -230
y_to_add = y_position * (-2) // len(colors)
for color in colors:
    tortoise = Turtle(shape="turtle")
    tortoise.color(color)
    tortoise.penup()
    y_position += y_to_add
    tortoise.goto(x=x_start, y=y_position)
    all_turtles.append(tortoise)

if user_input:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winner_color: str = turtle.pencolor()
            if winner_color == user_input:
                screen.numinput(title=f"You have won.{winner_color.title()} won.",
                                prompt="How did you enjoy the race? (0-10)",
                                minval=1,
                                maxval=10)
            else:
                screen.numinput(title=f"You have lost.{winner_color.title()} won.",
                                prompt="How did you enjoy the race? (0-10)",
                                minval=1,
                                maxval=10)
            screen.clear()
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
