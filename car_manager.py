import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Turtle_name = []
class CarManager:
    def __init__(self):
        # self.y =[-250,-220,-190,-160,-130,-100,-70,-40,-10,20,50,80,110,140,170,200,230,260]
        self.turtle_name = []
    def the_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            random_y = random.randint(-250, 250)
            tim = Turtle("square")
            tim.color(random.choice(COLORS))
            tim.shapesize(stretch_wid=1, stretch_len=3)
            tim.penup()
            tim.goto(x=290, y=random_y)
            self.turtle_name.append(tim)

    def moving(self):
        for turtles in self.turtle_name:
              turtles.backward(STARTING_MOVE_DISTANCE)

    def icreasing_speed(self):
        for turtles in self.turtle_name:
            MOVE = MOVE_INCREMENT
            MOVE += MOVE_INCREMENT
            turtles.backward(MOVE + 10)