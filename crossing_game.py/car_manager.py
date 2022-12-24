from turtle import Turtle
import random
COLORS=["red", "orange", "yellow","green", "blue", "purple"]
STARTING_MOVE_DISTANCE=3
MOVE_INCREMENT=8




class CarManager():
    def __init__ (self):  
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_turtle(self):
        random_choice=random.randint(0,6)
        if random_choice==1:
            pro=Turtle("square")
            pro.penup()
            pro.shapesize(stretch_len=2,stretch_wid=1)
            pro.color(random.choice(COLORS))
            random_y=random.randint(-250,250)
            pro.goto(300,random_y)
            self.all_cars.append(pro)

    def car_movement(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT



    

      





    #     :
    # pro=Turtle(shape="turtle")
    # pro.speed("fast")
    # pro.penup()
    # pro.goto(x=-230,y=y_keys[turtle_index])
    # pro.color(colors[turtle_index])
    # all_turtles.append(pro)