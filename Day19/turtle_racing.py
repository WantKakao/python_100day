import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-225, y=-100 + 40 * i)
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() > 220:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            is_race_on = False
            break

screen.exitonclick()
