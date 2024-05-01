import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.segment = []
        self.hideturtle()
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        t = Turtle("square")
        t.penup()
        t.color(random.choice(COLORS))
        t.shapesize(stretch_wid=1, stretch_len=2)
        t.goto(300, random.randint(-240, 240))
        self.segment.append(t)

    def move(self):
        for s in self.segment:
            s.backward(self.move_speed)
            if s.xcor() < -350:
                self.segment.remove(s)

    def speed_up(self):
        self.move_speed += MOVE_INCREMENT
