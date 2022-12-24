from tkinter import *
from turtle import right, width

from numpy import multiply
window=Tk()
window.title("My first GUI project")
window.minsize(width=500,height=300)







#LABEL
my_label=Label(text=" My name is usman", font=("Arial", 24 ,"bold"))
my_label.pack()
my_label["text"]="New_text"

#MAKE THE BUTTON FUNCTION
def button_clicked():
    print("i got clicked")
    new_text=input.get()
    my_label.config(text=new_text)

    # print("i got clicked")

#BUTTON
button=Button(text="click me",command=button_clicked)
button.pack()

input=entry=Entry(width=30)
entry.insert(END,string="Some text to begin with.")
print(entry.get())
entry.pack()

#text
text=Text(height=5,width=30)
text.focus()
text.insert(END ,"Example of multiple text entry")
print(text.get("1.0" ,END))
text.pack()

#Spinbox
def spinbox_used():
    print(spinbox.get())
spinbox=Spinbox(from_=0,to=10,width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value
def scale_used(value):
    print(value)
scale=Scale(from_=0,to=100,command=scale_used)
scale.pack()

#checkbutton
def checkbutton_used():
    #print 1 if on button checked
    #otherwise 0
    print(checked_state.get())
checked_state=IntVar()
checkbutton=Checkbutton(text="Is on?",variable=checked_state,command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#radiobutton
def radio_used():
    print(radio_state.get())
radio_state=IntVar()
radiobutton1=Radiobutton(text="Option",value=1,variable=radio_state,command=radio_used)
radiobutton2=Radiobutton(text="Option2",value=2,variable=radio_state)
radiobutton1.pack()
radiobutton2.pack()

#listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))
listbox=Listbox(height=4)
fruits=["Apple", "Peal","Orange","Banana"]
for item in fruits:
    listbox.insert(fruits.index(item),item)
    listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()


window.mainloop()

# def add(*args):
#     sum=0
#     for b in args:
#         sum+=b
#         print(sum)
# add(2,3,4,5,5)



# def calculate(n,**kwargs):
#     # print(kwargs["add"])
#     # for key,value in kwargs.items():
#     #     print(value)
#     n+=kwargs["add"]
#     n*=kwargs["multiply"]
#     print(n)

# calculate(3,add=3,multiply=5)



#HOW METHODS ARE CREATED AND THE BEST WAY IS TO USE THE METHOD GET() IT SELF
# class Car:
#     def _
# _init__(self,**kw):
#         self.make=kw["make"]
#         self.model=kw.get("model")



# my_car=Car(make="Nissan",)
# print(my_car.make)                                                        