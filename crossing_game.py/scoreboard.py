from turtle import Turtle
FONT=("Courier", 22, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level=1
        self.goto(-240,250)
        self.updates_level()

    def updates_level(self):
        self.clear()   
        self.write(f"Level:{self.level}",align="center",font=FONT)

    def show_game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=FONT)


    
        

    def increase_level(self):
        self.level+=1
        self.updates_level()
       

        
    