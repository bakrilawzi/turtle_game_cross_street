import random
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
color_list = ["grey","blue","black","pink","purple","green","red"]
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.start_position()

    def start_position(self):
        self.penup()
        self.goto(STARTING_POSITION[0], STARTING_POSITION[1])
        self.setheading(90)

    def moving_player(self):
        self.penup()
        self.fd(MOVE_DISTANCE)

    def wall_condition(self):
        self.start_position()

    def color_change(self):
        self.color(random.choice(color_list))