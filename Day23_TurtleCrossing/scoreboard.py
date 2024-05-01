from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.level = 1
        self.write_level()

    def write_level(self):
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
