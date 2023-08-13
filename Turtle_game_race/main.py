import random
from turtle import Turtle, Screen

# new_turtle = Turtle()
screen = Screen()

# def forward_move():
#     new_turtle.forward(10)
    
# def backward_move():
#     new_turtle.backward(10)
    
# def turn_right():
#     new_heading = new_turtle.heading() - 10
#     new_turtle.setheading(new_heading)
    
# def turn_left():
#     new_heading = new_turtle.heading() + 10
#     new_turtle.setheading(new_heading)
    
# def clearis():
#     new_turtle.penup()
#     new_turtle.clear()
#     new_turtle.home()
#     new_turtle.pendown()
    
# screen.listen()
# screen.onkey(forward_move,"w")
# screen.onkey(backward_move,"s")
# screen.onkey(turn_right,"d")
# screen.onkey(turn_left,"a")
# screen.onkey(clearis,"c")
# screen.exitonclick()
all_turtles = []
is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which Turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
y_position = [-70,-40,-10,20,50,80]
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_position[turtle_index])
    all_turtles.append(new_turtle)
    

if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} color turtle won the race")
                is_race_on = False
            else:
                print(f"You Lost and the {winning_color} color turtle won the race")
                is_race_on = False
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)
    
