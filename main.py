import turtle
from turtle import Turtle, Screen
import random

colors = ["red", "green", "blue", "orange"]
x = -230
y = -100

all_turtles = []

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)


user_bet = screen.textinput(title="Bet on your turtle", prompt="Choose your turtle by color - red, green, blue and orange")


# Creating 5 turtles
for i in range(4):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=x, y=y)
    y += 50
    all_turtles.append(new_turtle)

# Game logic

if user_bet:
    is_race_on = True

while is_race_on:

    for one_turtle in all_turtles:
        random_distance = random.randint(0, 10)
        one_turtle.forward(random_distance)

        if one_turtle.xcor() > 230:
            is_race_on = False
            winner = one_turtle.pencolor()
            if user_bet == winner:
                print("You win")
            else:
                print(f"You lose! The winner was the {winner} turtle")






screen.exitonclick()


