from turtle import Turtle

ALIGNMENT="center"
FONT=("Arial",24,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
       
        self.score=0
        with open("data.txt") as record:
            self.high_score=int(record.read())
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()
        
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score {self.high_score}",align=ALIGNMENT,font=FONT)
        
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open("data.txt", mode="w") as record:
                record.write(f"{self.high_score}")
        self.score=0
        self.update_scoreboard
        

    def increase_scoreboard(self):
        self.score+=1
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER",align="center",font=FONT)


        