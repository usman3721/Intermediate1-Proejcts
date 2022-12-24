
import pandas as pd
import turtle
screen=turtle.Screen()
screen.title("U.S States Game")
map_image=r"/Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel\pandas and csv file\us-states-game-start/blank_states_img.gif"
guessed_state=[]
screen.addshape(map_image)
turtle.shape(map_image)
states=pd.read_csv(r"/Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel\pandas and csv file\us-states-game-start/50_states.csv")
states_list=states.state.to_list()
while len(guessed_state)< 50:

    answer_state=turtle.textinput(title=f"{len(guessed_state)}/50 State Correct", prompt="Type the country to be fixed").title()
    if answer_state == "Exit":
        missing_states=[names for names in states_list if names not in guessed_state]
        # missing_states=[]
        # for names in states_list:
        #     if names not in guessed_state:
        #         missing_states.append(names)
        
        new_data=pd.DataFrame(missing_states)
        new_data.to_csv("state_to_learn.csv")

        break
    if answer_state in states_list:
        guessed_state.append(answer_state)
        pro=turtle.Turtle()
        pro.hideturtle()
        pro.penup()
        extracted_state=states[states.state==answer_state]
        
        pro.goto(int(extracted_state.x), int(extracted_state.y))
        pro.write(answer_state)
        # pro.write(extracted_state.state.item())






    # def get_mouse_click_coor(x,y):
    #     print(x,y)
    # turtle.onscreenclick(get_mouse_click_coor)







    
        
      
