from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from time import strftime

root = Tk()
lbl2 = Label(root, font=("times new roman", 20, "bold"))
def clock():
    string = strftime('%H:%M:%S %p')
    lbl2.config(text=string)
    lbl2.after(1000,clock)
class App:
    def __init__(self, top):
        self.top = top
        top.title("stock management")
        top.geometry("1028x500")
        top.configure(background="#091833")

        font10 = "{courier New} 10 normal"
        font11 = "{U.S . 101} 30 bold"
        font12 = "Al-Aramco 11 bold"
        font13 = "{courier New} 10 bold"
        font14 = "{Segoe UI} 15 bold"
        font15 = "Arial 13 bold"
        font16 = "{Segoe UI} 13 bold"

        self.lbl1 = Label(self.top, text="Management Spare Parts", font=("times new roman", 20, "bold")).place(x=300,y=65)
clock()
lbl2.pack()
lbl2.place(x=370,y=110)
e = App(root)
root.mainloop()
