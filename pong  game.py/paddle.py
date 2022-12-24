from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("red")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)  
     
    def up(self):
        new_y=self.ycor()+70
        self.goto(self.xcor(),y=new_y)       
    def back(self):
        new_y=self.ycor()-70
        self.goto(self.xcor(),y=new_y)


