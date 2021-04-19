from tkinter import *
from tkinter import Button
from tkinter import ttk
from PIL import Image, ImageTk
import time


root = Tk()
#localtime = time.strftime("%H:%M:%S")

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

        self.lbl1 = Label(self.top, text="Management Spare Parts", font=("times new roman", 20, "bold")).place(x=300, y=65)
       # self.lbl2 = Label(self.top, text=, bg="#091833", font=("times new roman", 20, "bold")).place(x=300, y=85)


    def clock(self):
        hour = time.strftime("%H")
        minute = time.strftime("%M")

        second = time.strftime("%S")
        lable2 = Label.config(text=hour + ":" + minute + ":" + second).after(1000, clock())






e = App(root)
root.mainloop()
