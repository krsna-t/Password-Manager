from tkinter import *
from tkinter import messagebox
import random
import string
import json

def password_gen():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '/', '?']

    password_list = []

    for char in range(random.randint(3, 5)):
        password_list.append(random.choice(letters))

    for char in range(random.randint(3, 5)):
        password_list.append(random.choice(symbols))

    for char in range(random.randint(3, 5)):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)
    password = "".join(password_list)
    
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    window.clipboard_clear()
    window.clipboard_append(password)
    check_password_strength()

def save():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Enter valid information")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showinfo(title="Error", message="Please enter the website name.")
        return

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Password Found",message=f"Website: {website}\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Not Found", message=f"No password found for {website}")
    

def check_password_strength(event=None):
    password = password_entry.get()
    if len(password) < 6:
        password_strength.config(bg='red', text='Weak')
    elif 6 <= len(password) <= 8 and any(char.isdigit() for char in password):
        password_strength.config(bg="orange", text="Medium")
    elif len(password) > 8 and any(char.isdigit() for char in password) and any(char.isupper() for char in password) and any(char in string.punctuation for char in password):
        password_strength.config(bg="green", text="Strong")
    else:
        password_strength.config(bg="yellow", text="Fair")

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=228, width=228, bg="white")
logo = PhotoImage(file="images.png")
canvas.create_image(114, 114, image=logo)
canvas.grid(column=1, row=0, padx=25, pady=25, columnspan=2)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1, pady=5)
email_label = Label(text='E-Mail/G-Mail:')
email_label.grid(column=0, row=2, pady=5)
password_label = Label(text='Password:')
password_label.grid(column=0, row=3, pady=5)

website_entry = Entry(width=53)
website_entry.grid(column=1, row=1, padx=8, pady=8, columnspan=2)
email_entry = Entry(width=53)
email_entry.insert(0, "krishna40tiwari@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=53)
password_entry.grid(column=1, row=3, columnspan=2)
password_entry.bind("<KeyRelease>", check_password_strength)

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="e")
generate_button = Button(text="Generate Password", command=password_gen)
generate_button.grid(column=2, row=4, padx=8, pady=8)
password_strength = Button(text="Password Strength")
password_strength.grid(column=1, row=4, padx=10, pady=10, sticky="w")
add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=1, row=5, padx=8, pady=8, columnspan=2)

window.mainloop()
