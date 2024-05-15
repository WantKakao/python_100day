from tkinter import *


def button_clicked():
    my_label.config(text=input_.get())
    print("Button Clicked!")


# make Window
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# make Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
# my_label.pack()
# my_label.place(x=10, y=10)
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click me", command=button_clicked)
new_button = Button(text="New Button")
# button.pack()
button.grid(column=1, row=1)
new_button.grid(column=2, row=0)

# Entry
input_ = Entry(width=10)
# input_.pack()
input_.grid(column=3, row=2)





window.mainloop()
