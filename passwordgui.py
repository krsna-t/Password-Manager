from tkinter import *
from tkinter import messagebox
import random

def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '/', '?']

    password_list=[]

    for char in range (1,random.randint(3,5)):
        password_list.append(random.choice(letters))

    for char in range (1,random.randint(3,5)):
        password_list.append(random.choice(symbols))

    for char in range (1,random.randint(3,5)):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)
    password=""
    for char in password_list:
        password+=char
    password_entry.insert(0,f"{password}")   

def save():
    website=website_entry.get()
    password=password_entry.get()
    email=email_entry.get()
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Error",message="Enter valid information")
    else:    
        is_ok=messagebox.askokcancel(title="website",message=f"This is the website:{website} \n and  password:{password}.\n"
        f"Are you sure about that?")
        if is_ok:
            with open("/home/krishna/Documents/python/day26-30/day29/data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)
        else:
            pass        

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas=Canvas(height=228,width=228,bg="white")
logo=PhotoImage(file="/home/krishna/Documents/python/day26-30/day29/images.png")
canvas.create_image(114,114,image=logo)
canvas.grid(column=1,row=0)
website_label= Label(text='Website:')
website_label.grid(column=0,row=1)
Email_label=Label(text='E-Mail/G-Mail:')
Email_label.grid(column=0,row=2)
password_label=Label(text='Password:')
password_label.grid(column=0,row=3)

website_entry=Entry(width=70)
website_entry.grid(column=1,row=1,columnspan=2)
email_entry=Entry(width=70)
email_entry.insert(0,"krishna40tiwari@gmail.com")
email_entry.grid(column=1,row=2,columnspan=2)
password_entry=Entry(width=50)
password_entry.grid(column=1,row=3)

generate_button=Button(text="Generate Password",command=password_gen)
generate_button.grid(column=2,row=3)
add_button=Button(text="Add",width=30,command=save)
add_button.grid(column=1,row=4)

window.mainloop()