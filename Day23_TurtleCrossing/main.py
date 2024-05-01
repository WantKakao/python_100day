import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
T = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    T += 1
    if T == 6:
        car.create_car()
        T = 0
    car.move()

    if player.ycor() >= 280:
        player.goto(player.starting_pos)
        car.speed_up()
        scoreboard.level_up()

    for s in car.segment:
        if player.distance(s) < 25:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()