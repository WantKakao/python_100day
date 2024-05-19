from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_list = []
    letters = list(range(65, 91)) + list(range(97, 123))
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list += ([chr(choice(letters)) for _ in range(randint(8, 10))])
    password_list += ([choice(symbols) for _ in range(randint(2, 4))])
    password_list += ([str(randint(0, 9)) for _ in range(randint(2, 4))])

    shuffle(password_list)
    pwd = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, pwd)
    pyperclip.copy(pwd)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    w = website_input.get()
    u = username_input.get()
    p = password_input.get()
    new_data = {
        w: {
            "email": u,
            "password": p
        }
    }

    if not w or not p:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)   # Reading old data
                # print(type(data))   --> dictionary
                data.update(new_data)   # Updating old data

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)  # Saving updated data
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        website_input.delete(0, END)
        password_input.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    w = website_input.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            if data.get(w):
                messagebox.showinfo(title=w, message=f"{data[w]["email"]} \n{data[w]["password"]}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for the website exists")

    except (json.decoder.JSONDecodeError, FileNotFoundError):
        messagebox.showinfo(title="Error", message=f"No Data File Found")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
username = Label(text="Email/Username:")
password = Label(text="Password:")
generate_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=45, command=save)
search_button = Button(text="Search", width=15, command=find_password)
website_input = Entry(width=29)
website_input.focus()
username_input = Entry(width=45)
username_input.insert(0, "sm@naver.com")
password_input = Entry(width=29)

website.grid(row=1, column=0)
username.grid(row=2, column=0)
password.grid(row=3, column=0)
generate_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)
search_button.grid(row=1, column=2)
website_input.grid(row=1, column=1)
username_input.grid(row=2, column=1, columnspan=2)
password_input.grid(row=3, column=1)


window.mainloop()