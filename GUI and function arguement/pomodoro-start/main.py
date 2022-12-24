
from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# WORK_MIN = 1
# SHORT_BREAK_MIN = 5
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def Timer_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    label.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
     
    global reps
    reps+=1
    work_sec=int(entry_w.get())*60
    short_break_sec=int(entry_sb.get())*60
    long_break_Sec=int(entry_lb.get())*60
    if reps % 8==0:
        count_down(long_break_Sec)
        label.config(text="Break", fg=RED)
    elif reps%2==0:
        count_down(short_break_sec)
        label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)
        

    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
   

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
      
        start_timer()
        mark=""
        working_session=math.floor(reps/2)
        for _ in range(working_session):
            mark+="✔"
            checkmark.config(text=mark,fg=GREEN)
# ---------------------------- UI SETUP ------------------------------- #window

window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=60)


#label
label=Label(text="Timer", fg=GREEN, font=(FONT_NAME, 34,"bold"))
label.grid(column=2,row=0)

#start button
start=Button(text="Start", font=(FONT_NAME,12,"bold"),highlightthickness=0,command=start_timer)
start.grid(column=0,row=3)
reset=Button(text="Reset", font=(FONT_NAME,12,"bold"),highlightthickness=0,command=Timer_reset)
reset.grid(column=3,row=3)


#SELCTING CHOICES
label_w=Label(text="Work" ,font=(FONT_NAME, 12,"bold"))
label_w.grid(column=0,row=0)
entry_w=Entry(width=7)
entry_w.grid(column=0,row=1)

label_sb=Label(text="Short Break" ,font=(FONT_NAME, 12,"bold"))
label_sb.grid(column=2,row=5)
entry_sb=Entry(width=7)
entry_sb.grid(column=2,row=6)

label_lb=Label(text="Long Break" ,font=(FONT_NAME, 12,"bold"))
label_lb.grid(column=3,row=0)
entry_lb=Entry(width=7)
entry_lb.grid(column=3,row=1)


#checkmark
checkmark=Label(font=("bold"),fg=GREEN,bg=YELLOW)
checkmark.grid(column=2,row=4)




canvas=Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
canvas.grid(column=2,row=2)
tomato_img=PhotoImage(file=r"\Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel\GUI and function arguement\pomodoro-start/tomato.png")
canvas.create_image(103,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00", fill="white",font=(FONT_NAME, 35  ,"bold"))
canvas.grid()




window.mainloop()