from turtle import Turtle
class Game_Over(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

    def writer(self):
        self.write("GAME OVER", False, align="center", font=("Courier", 24, "normal"))