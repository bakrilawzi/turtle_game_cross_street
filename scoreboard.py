from turtle import Turtle
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.write(f"level: {self.score}", False, "left", font=("Courier", 24, "normal"))

    def increasing_level(self):
        self.score += 1
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.write(f"level: {self.score}", False, "left", font=("Courier", 24, "normal"))

