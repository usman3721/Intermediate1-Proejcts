from tkinter import *

from turtle import right, width


def button_clicked():
    # print("i got clicked")
    # new_text=input.get()
    # my_label.config(text=new_text)
    pass




window=Tk()
window.title("My first GUI project")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)


#LABEL
my_label=Label(text="I am a Lbael", font=("Arial", 24 ,"bold"))
my_label.config(text="new Text")
my_label.grid(column=0,row=0)
my_label.config(padx=50,pady=50)



#BUTTON
button=Button(text="click me",command=button_clicked)
button.grid(column=1,row=1)


#NEW_BUTTON
new_button=Button(text="click me again", command=button_clicked)
new_button.grid(column=2,row=0)




input=Entry(width=30)
print(input.get())
input.grid(column=3,row=2)



window.mainloop()
