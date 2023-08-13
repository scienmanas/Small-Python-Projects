import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.MoveUp, "Up")
count = 1

while game_is_on:
    if count%6 == 0 :
        cars.CreateCars()
    for car in cars.cars :
        if player.distance(car) < 23 :
            score.GameOver()
            game_is_on = False
            break
    if player.ycor() > 290 :
        score.UpdateScoreAndLevel()
        player.UpdatePositionOnLevelUp()
        cars.IncreaseSpeed()
    time.sleep(0.1)
    screen.update()



    cars.Move()
    count += 1



screen.exitonclick()