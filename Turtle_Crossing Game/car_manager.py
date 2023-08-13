import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        self.cars = []
        self.CreateCars()
    
    def CreateCars(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(1,2)
        car.color(random.choice(COLORS))
        car.penup()
        car.setheading(180)
        car.goto(300, random.randint(-250,250))
        self.cars.append(car)
    
    def Move(self):
        for car in self.cars :
            car.forward(STARTING_MOVE_DISTANCE)
            
    def IncreaseSpeed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT