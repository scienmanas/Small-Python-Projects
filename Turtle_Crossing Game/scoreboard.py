from turtle import Turtle
FONT = ("Courier", 24, "normal")
LevelCoordinate = (-300,265)

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(LevelCoordinate)
        self.color("black")
        self.write(f"Level: {self.level}", True, align="left", font=FONT)
        
    
    def GameOver(self):
        self.goto(0,0)
        self.write("Game Over", True, align="center", font=FONT)
        
    
    def UpdateScoreAndLevel(self):
        self.level = self.level + 1
        self.clear()
        self.goto(LevelCoordinate)
        self.write(f"Level: {self.level}", True, align="left", font=FONT)