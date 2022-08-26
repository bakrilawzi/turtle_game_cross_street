import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
from game_over import Game_Over
screen = Screen()
screen.title("i bet that you can cross this street alone :p")
screen.setup(600, 600)
screen.bgcolor("white")
screen.listen()
screen.tracer(0)
man = Player()
car = CarManager()
game= Game_Over()

level = Scoreboard()
screen.onkey(fun=man.moving_player, key="Up")
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car.the_car()
    car.moving()
    if man.ycor() >= 290:
        man.wall_condition()
        level.increasing_level()
        man.color_change()
        car.icreasing_speed()
    for cars in car.turtle_name:
        if cars.distance(man)<20:
            game_on = False
            game.writer()








screen.exitonclick()


