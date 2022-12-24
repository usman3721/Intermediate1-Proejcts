

from turtle import Turtle,Screen
import random
colors=["red", "yellow", "orange", "green", "blue", "purple"]
y_keys=[-130,-80,-10,50,80,130]
all_turtles=[]
race_on=False
screen=Screen()
screen.setup(width=500,height=400)

user_input=screen.textinput(title="Guess the winner", prompt="Which turtle willl win the race? Enter the color!")
for turtle_index in range(0,6):
    pro=Turtle(shape="turtle")
    pro.speed("fast")
    pro.penup()
    pro.goto(x=-230,y=y_keys[turtle_index])
    pro.color(colors[turtle_index])
    all_turtles.append(pro)

if user_input:
    race_on=True
while race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_input:
                print(f"you hsve won.The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost. The {winning_color} turtle won the race")
        random_distance=random.randint(0,10)
        turtle.forward(random_distance)
screen.exitonclick()