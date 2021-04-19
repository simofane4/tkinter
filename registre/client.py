from tkinter import *
from tkinter import Button
from tkinter import ttk
# from PIL import Image, ImageTk
import time

root = Tk()




class App:
    def __init__(self, top):
        self.top = top
        top.title("client Register")
        top.geometry("1028x500")
        top.configure(background="#091833")




        self.lbl1 = Label(self.top, text="Client Register", font=("times new roman", 22, "bold")).place(x=300,
                                                                                                               y=62, width=350)

        #--label food
        self.label = Label(self.top, text="ID_client :", bg="#091833", font=("times new roman", 17, "bold"), fg="black").place(x=20, y=150)
        self.txt_lb1 = ttk.Entry(self.top, font=("times new roman", 13, "bold")).place(x=135, y=153, width=170, height=24)

        self.label2 = Label(self.top, text="F_N_C    :", bg="#091833", font=("times new roman", 17, "bold"), fg="black").place(x=20, y=193)
        self.txt_lb2 = ttk.Entry(self.top, font=("times new roman", 13, "bold")).place(x=135, y=196, width=170, height=24)

        self.label3 = Label(self.top, text="L_N_C    :", bg="#091833", font=("times new roman", 17, "bold"), fg="black").place(x=20, y=236)
        self.txt_lb3 = ttk.Entry(self.top, font=("times new roman", 13, "bold")).place(x=135, y=239, width=170, height=24)


        self.label4 = Label(self.top, text="Email_C  :", bg="#091833", font=("times new roman", 17, "bold"), fg="black").place(x=20, y=279)
        self.txt_lb4 = ttk.Entry(self.top, font=("times new roman", 13, "bold")).place(x=135, y=282, width=170, height=24)

        self.label5 = Label(self.top, text="N_Ph_C  :", bg="#091833", font=("times new roman", 17, "bold"), fg="black").place(x=20, y=322)
        self.txt_lb5 = ttk.Entry(self.top, font=("times new roman", 13, "bold")).place(x=135, y=325, width=170, height=24)


        self.label5 = Label(self.top, text="Ad_C       :", bg="#091833", font=("times new roman", 17, "bold"), fg="black").place(x=20, y=365)
        self.txt_lb5 = ttk.Entry(self.top, font=("times new roman", 13, "bold")).place(x=135, y=368, width=170, height=24)



        self.btn1 = Button(self.top, text="Add", bg="black", font=("times new roman", 15, "bold"), fg="white" , activebackground="#091833").place(x=310, y=391, width=90, height=30)

        self.btn2 = Button(self.top, text="Edit", bg="black", font=("times new roman", 15, "bold"), fg="white" , activebackground="#091833").place(x=440, y=391, width=90, height=30)

        self.btn3 = Button(self.top, text="Delete", bg="black", font=("times new roman", 15, "bold"), fg="white", activebackground="#091833").place(x=570, y=391, width=90, height=30)


        search_lbl = Label(self.top, text="Search", bg="#091833", font=("times new roman", 15, "bold"), fg="black").place(x=600, y=103)
        self.btn4 = ttk.Entry(self.top, font=("times new roman", 15, "bold")).place(x=670, y=109, width=150, height=20)








e = App(root)
root.mainloop()
