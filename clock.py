from tkinter import *
from tkinter.ttk import *

from time import strftime


root = Tk()
root.title("CLOCK")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)

label = Label(root,font=("Aptos",80),background="black",foreground="#39E81C") 
label.pack(anchor="center")
time()

mainloop()