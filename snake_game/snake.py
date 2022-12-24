# # pro=Turtle()

# segment1=Turtle(shape="square")
# segment1.color("white")
# # segment1.shapesize(0.3,0.3,0.3)


# segment2=Turtle(shape="square")
# # segment2.shapesize(0.3,0.3,0.3)
# segment2.color("white")
# segment2.goto(x=-20, y=0)


# segment3=Turtle(shape="square")
# # segment3.shapesize(0.3,0.3,0.3)
# segment3.color("white")
# segment3.goto(x=-40, y=0)




from turtle import Turtle, forward
# segment=[]
STARTING_POSITION=[(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE=20
import time


PAUSED=False

class Snake():
    def __init__(self):
        self.segment=[]  
        self.create_snake()
        self.head=self.segment[0]
    
    def create_snake(self):   
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment=Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head=self.segment[0]
            
    def move(self):
        for seg_num in range(len(self.segment)-1,0,-1):
            new_x=self.segment[seg_num-1].xcor()
            new_y=self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        self.head.setheading(90)
    def down(self):
        self.head.setheading(270)
    def left(self):
        self.head.setheading(180)
    def right(self):
        self.head.setheading(0)

   


    

    


