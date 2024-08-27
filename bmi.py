from tkinter.constants import BOTTOM, R1

from tkinter import *
import random, string


def Tk():
    pass


root = Tk()
root.geometry("400x280")
root.title("Password Generator")


def StringVar():
    pass


title = StringVar()


class Label:
    pass


label = Label(root, textvariable=title).pack()
title.set("The strength of our password:")



def selection():
    selection = choice.get()


def IntVar():
    pass


choice = IntVar()


def Radiobutton(root, text, variable, value, command):
    pass


R1 = Radiobutton(root, text="POOR", variable=choice, value=1, command=selection).pack(anchor=R1)


def Radiobutton(root, text, variable, value, command):
    pass


R2 = Radiobutton(root, text="AVERAGE", variable=choice, value=2, command=selection).pack(anchor=R1)


class Radiobutton:
    pass


R3 = Radiobutton(root, text="ADVANCED", variable=choice, value=3, command=selection).pack(anchor=R1)
labelchoice = Label(root)
labelchoice.pack()


def StringVar():
    pass


lenlabel = StringVar()
lenlabel.set("Password length:")
lentitle = Label(root, textvariable=lenlabel).pack()

#
val = IntVar()


def Spinbox(root, from_, to_, textvariable, width):
    pass


spinlenght = Spinbox(root, from_=8, to_=24, textvariable=val, width=13).pack()

# passprint


def callback():
    lsum.config(text=passgen())


# clickable button
def Button(root, text, bd, height, command, pady):
    pass


passgenButton = Button(root, text="Generate Password", bd=5, height=2, command=callback, pady=3)
passgenButton.pack()
password = str(callback)

# password result message
lsum = Label(root, text="")
lsum.pack(side=BOTTOM)

# function
poor= string.ascii_uppercase + string.ascii_lowercase
average= string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols = """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?/"""
advance = poor+ average + symbols


def passgen():
    if choice.get() == 1:
        return "".join(random.sample(poor, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(advance, val.get()))


root.mainloop()
