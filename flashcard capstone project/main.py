from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn={}
        
try:#
    data=pd.read_csv(r"\Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel/flashcard capstone project\data/word_to_learn.csv")
except FileNotFoundError:
    original_data=pd.read_csv(r"\Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel/flashcard capstone project\data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")
#------------------DEFINING THE RIGHT AND WRONG FUNCTION----------------#
def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_back_ground,image=card_front)
    flip_timer=window.after(3000,func=flip_card)
    

def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_back_ground,image=card_back)        


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data=pd.DataFrame(to_learn)
    data.to_csv(r"\Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel/flashcard capstone project\data/word_to_learn.csv", index="False")
    next_card()
    
   

#------------------------SCREEN--------------------------
window=Tk()
window.title("flashcard project")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip_card)

#front card
canvas=Canvas(width=800,height=526)
card_front=PhotoImage(file=r"\Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel/flashcard capstone project/images/card_front.png")
card_back_ground=canvas.create_image(400,263,image=card_front)
card_word=canvas.create_text(400,263,text="",font=("Ariel",60,"bold"),tags="Word")
card_title=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)

#back_card
card_back=PhotoImage(file=r"\Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel/flashcard capstone project/images/card_back.png")


#correct button
correct=PhotoImage(file=r"\Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel/flashcard capstone project\images/right.png")
correct_button=Button(image=correct,command=is_known)
correct_button.grid(column=1,row=1)

#wrong button
wrong=PhotoImage(file=r"\Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel/flashcard capstone project\images/wrong.png")
wrong_button=Button(image=wrong,highlightthickness=0,command=next_card)
wrong_button.grid(column=0,row=1)


next_card()
window.mainloop()

