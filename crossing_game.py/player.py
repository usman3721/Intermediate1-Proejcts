from turtle import Turtle



STARTING_POSITION=(0,-280)
MOVE_DISTANCE=10
FINISH_LINE_Y=280



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_to(self):
        self.forward(MOVE_DISTANCE)
    

    def finish_line(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)

        


  
   
        

    


  

        
    # def back(self):
    #     new_y=self.ycor()-70
    #     self.goto(self.xcor(),y=new_y)



 
     
    
    