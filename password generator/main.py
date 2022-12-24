

# import pyperclip
from tkinter import *
from tkinter import messagebox
import random
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_symbols=[random.choice(symbols) for _ in range(nr_symbols)]
    password_letter=[random.choice(letters) for _ in range(nr_letters)]
    password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]
    password_list=password_letter +password_symbols +password_numbers

    random.shuffle(password_list)
    password="".join(password_list)
    # print(f"Your password is: {password}")
    password_entry.insert(0,password)
    # pyperclip.copy(password)
    # pyperclip.paste()


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    global real_data
    web=website_entry.get()
    mail=email_entry.get()
    pword=password_entry.get()
    new_data={
        web:{
            "email":mail,
            "password":pword,
            
        }
    }
    if len(web)==0 or len(pword) ==0:
        messagebox.showinfo(title="Oops",message="Please do not leave any of he filds empty")
    else:
        # it_ok=messagebox.askokcancel(title=web,message=f"These are the detail you entered: \n Email:{mail} \n Password: {pword}")
        # if it_ok:
        try:
            with open(r"\Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel\password generator/data.json",mode="r") as data_file:
                real_data=json.load(data_file)
        except FileNotFoundError:
            with open(r"\Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel\password generator/data.json",mode="w") as data_file:
                json.dump(new_data,data_file,indent=5)
        else:
            real_data.update(new_data)
            with open(r"\Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel\password generator/data.json",mode="w") as data_file:
                json.dump(real_data,data_file,indent=5)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)
    return real_data

def search():
    website=website_entry.get()
    try:
        with open(r"\Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel\password generator/data.json") as data_file:
            data=json.load(data_file)
         
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR",message="THE IS NO SUCH data IN THE DATABASE")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title="Acc details",message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No detail of {website} exists")
      
   
 
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(pady=50,padx=50)


canvas=Canvas(width=200,height=200)
image=PhotoImage(file=r"\Users\hp\Desktop/100DaysOfCode by Angela Yu/100IntermediateLevel\password generator/logo.png")
canvas.create_image(100,100,image=image)
canvas.grid(column=1,row=0)


#WEBSITE
website_label=Label(text="Website: ")
website_label.grid(column=0,row=1)

website_entry=Entry(width=35)
website_entry.grid(column=1,row=1)
website_entry.focus()

#EMIAL/USERNAME
email_label=Label(text="Email/Username: ")
email_label.grid(column=0,row=2)
email_entry=Entry(width=35)
email_entry.grid(column=1,row=2)
email_entry.insert(END,"olamidehassan@gmail.com")

#PASSWORD
password_label=Label(text="Password: ")
password_label.grid(column=0,row=3)
password_entry=Entry(width=35)
password_entry.grid(column=1,row=3)


#GENERATE PASSWORD
generate_password=Button(text="Generate Password",command=generate_password)
generate_password.grid(column=2,row=3)
window.config(padx=20,pady=20)


#ADD TO FILE
add_to_file=Button(text="Add",width=36,command=add)
add_to_file.grid(column=1,row=4,columnspan=2)
window.config(padx=20,pady=20)

#SEARCH
search=Button(text="Seach",command=search,width=13)
search.grid(column=2,row=1)

window.mainloop()