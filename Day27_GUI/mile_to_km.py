from tkinter import *


def calculate():
    km = Entry1.get()
    mile = float(km) * 1.609
    Label4.config(text=mile)


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

Label1 = Label(text="Miles")
Label2 = Label(text="ie equal to")
Label3 = Label(text="Km")
Label4 = Label(text="0")

Label1.grid(row=0, column=2)
Label2.grid(row=1, column=0)
Label3.grid(row=1, column=2)
Label4.grid(row=1, column=1)

Entry1 = Entry(width=7)
Entry1.grid(row=0, column=1)

Button1 = Button(text="Calculate", command=calculate)
Button1.grid(row=2, column=1)


window.mainloop()