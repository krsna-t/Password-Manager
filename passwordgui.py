from tkinter import *
from tkinter import messagebox
import random
import string #***

def password_gen():
    letters = string.ascii_letters #***
    numbers = string.digits #***
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
    # password_entry.
    password_entry.delete(0,END)    
    password_entry.insert(0,f"{password}")
    check_password_strength()   

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
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)
        else:
            pass   

def check_password_strength(event=None):
    password=password_entry.get()
    if len(password)<6:
        password_strength.config(bg='red',text='weak')
    elif 6 <= len(password) <= 8 and any(char.isdigit() for char in password):
        password_strength.config(bg="orange", text="Medium")
    elif len(password) > 8 and any(char.isdigit() for char in password) and any(char.isupper() for char in password) and any(char in string.punctuation for char in password):
        password_strength.config(bg="green", text="Strong")
    else:
        password_strength.config(bg="yellow",text="Fair")          

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas=Canvas(height=228,width=228,bg="white")
logo=PhotoImage(file="images.png")
canvas.create_image(114,114,image=logo)
canvas.grid(column=1,row=0,padx=25,pady=25) #this is incude 
website_label= Label(text='Website:')
website_label.grid(column=0,row=1,pady=5)
Email_label=Label(text='E-Mail/G-Mail:')
Email_label.grid(column=0,row=2,pady=5)
password_label=Label(text='Password:')
password_label.grid(column=0,row=3,pady=5)

website_entry=Entry(width=53)
website_entry.grid(column=1,row=1,columnspan=2)
email_entry=Entry(width=53)
email_entry.insert(0,"krishna40tiwari@gmail.com")
email_entry.grid(column=1,row=2,columnspan=2)
password_entry=Entry(width=53)
password_entry.grid(column=1,row=3,columnspan=2)
password_entry.bind("<KeyRelease>", check_password_strength)
generate_button=Button(text="Generate Password",command=password_gen)
generate_button.grid(column=2,row=4,padx=8,pady=8)
password_strength=Button(text="Password Strength")
password_strength.grid(column=1, row=4, padx=10, pady=10, sticky="w")  
add_button=Button(text="Add",width=30,command=save)
add_button.grid(column=1,row=5,padx=8,pady=8)

window.mainloop()
