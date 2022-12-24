from tkinter import *

def calculate():
    miles=float(entry.get())
    km=round(miles*1.609)
    result.config(text=f"{km}")
  


window=Tk()
window.title("Mile to Km Converter")
window.minsize(width=500,height=300)
window.config(padx=300,pady=300)

#MILES
label=Label(text="Miles")
label.grid(column=2,row=0)
window.config(padx=20,pady=20)

#ENTRY
entry=Entry(width=7)
entry.grid(column=1,row=0)



#RESULT
result=Label(text="0",)
result.grid(column=1,row=1)



#KILOMETRER
kilo=Label(text="Km")
kilo.config(text="Km")
kilo.grid(column=2,row=1)
window.config(padx=20,pady=20)

#equal
equal=Label(text="is equal to")
equal.config(text="is equal to")
equal.grid(column=0,row=1)
window.config(padx=20,pady=20)


# BUTTON
button=Button(text="calculate", command=calculate)
button.grid(column=1,row=3)
window.config(padx=20,pady=20)


# #TEXT
# text=Text(height=1,width=6)
# text.focus()
# text.insert(END ,0)
# print(text.get("1.0" ,END))
# text.grid(column=1,row=0)
# window.config(padx=200,pady=200)




window.mainloop()