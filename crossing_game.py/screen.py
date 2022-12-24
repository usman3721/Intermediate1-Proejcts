from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkeypress(fun=player.go_to , key="Up")

game_on=True
while game_on: 
   
   
    
    time.sleep(0.1)
    screen.update()
   
    car_manager.create_turtle()
    car_manager.car_movement()
  
  
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.show_game_over()
            game_on=False
            

    if player.finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
    
  
    
   
        
       
        
         
    
    

screen.exitonclick()