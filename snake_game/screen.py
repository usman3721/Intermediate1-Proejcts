#setting up the screen
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("blue")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()

screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")
game_is_on=True
while game_is_on:
    screen.update()  
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_scoreboard()
    if snake.head.xcor()>295 or snake.head.xcor()<-295 or snake.head.ycor()>295 or snake.head.ycor()<-295:
        scoreboard.reset()
        snake.reset()
        scoreboard.update_scoreboard()
    for segment in snake.segment[1:]: 
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
  

screen.exitonclick()
