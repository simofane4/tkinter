from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import time
from tkinter import ttk
from time import strftime

app = tk.Tk()

app.geometry("800x800+350+150")
app.title("Gestion de Stock des Pièces de Rechange")
app.configure(background='#0b2239')
app.resizable(width=False, height=True)
#localtime = time.strftime("%H:%M:%S %y-%m-%d")
def enter(event):
    
    lbl_img5.config(bg='white')
def leave(event):
    
    lbl_img5.config(bg='#164777')

def enter_1(event):
    
    lbl_img6.config(bg='white')
def leave_1(event):
    
    lbl_img6.config(bg='#164777')
def enter_2(event):
    
    lbl_img7.config(bg='white')
def leave_2(event):
    
    lbl_img7.config(bg='#164777')
def enter_3(event):
    
    lbl_img8.config(bg='white')
def leave_3(event):
    
    lbl_img8.config(bg='#164777')
def enter_4(event):
    
    lbl_img4.config(bg='white')
def leave_4(event):
    
    lbl_img4.config(bg='#164777')
def enter_5(event):
    
    lbl_img9.config(bg='white')
def leave_5(event):
    
    lbl_img9.config(bg='#164777')

    
    


icon = tk.PhotoImage(file="icon.png")
app.call("wm", "iconphoto", app._w, icon)

app.img1 = Image.open("settings.png").resize((80, 80), Image.ANTIALIAS)
app.photo_image1 = ImageTk.PhotoImage(app.img1)
lbl_img1 = Label(image=app.photo_image1, fg="black", bg="#0b2239").place(x=20, y=15, width=80, height=80)


ho_lbl6 = tk.Label(app, text="Gestion de Stock  ", fg="white", font=("Times New roman", 16), bg='#0b2239').place(x=115, y=40)

#app.img4 = Image.open("client.png").resize((100, 100), Image.ANTIALIAS)
#app.photo_image4 = ImageTk.PhotoImage(app.img4)
#lbl_img4 = Button(image=app.photo_image4, borderwidth=0, bg="white", activebackground="red").place(x=50, y=150, width=100, height=100)


app.img5 = Image.open("group.png").resize((100, 100), Image.ANTIALIAS)
app.photo_image5 = ImageTk.PhotoImage(app.img5)
lbl_img5 = Button(image=app.photo_image5, borderwidth=0, bg="#164777", activebackground="red")
lbl_img5.place(x=150, y=250, width=150, height=150)
lbl_img5.bind('<Enter>' , enter)
lbl_img5.bind('<Leave>', leave)

app.img6 = Image.open("service.png").resize((100, 100), Image.ANTIALIAS)
app.photo_image6 = ImageTk.PhotoImage(app.img6)
lbl_img6 = Button(image=app.photo_image6, borderwidth=0, bg="#164777", activebackground="red")
lbl_img6.place(x=150, y=410, width=150, height=150)
lbl_img6.bind('<Enter>' , enter_1)
lbl_img6.bind('<Leave>', leave_1)

app.img7 = Image.open("tool-box.png").resize((100, 100), Image.ANTIALIAS)
app.photo_image7 = ImageTk.PhotoImage(app.img7)
lbl_img7 = Button(image=app.photo_image7, borderwidth=0, bg="#164777", activebackground="red")
lbl_img7.place(x=310, y=250, width=150, height=150)
lbl_img7.bind('<Enter>' , enter_2)
lbl_img7.bind('<Leave>', leave_2)

app.img8 = Image.open("cart.png").resize((100, 100), Image.ANTIALIAS)
app.photo_image8 = ImageTk.PhotoImage(app.img8)
lbl_img8 = Button(image=app.photo_image8, borderwidth=0, bg="#164777", activebackground="red")
lbl_img8.place(x=310, y=410, width=150, height=150)
lbl_img8.bind('<Enter>' , enter_3)
lbl_img8.bind('<Leave>', leave_3)


app.img4 = Image.open("invoice.png").resize((100, 100), Image.ANTIALIAS)
app.photo_image4 = ImageTk.PhotoImage(app.img4)
lbl_img4 = Button(image=app.photo_image4, borderwidth=0, bg="#164777", activebackground="red")
lbl_img4.place(x=470, y=250, width=150, height=150)
lbl_img4.bind('<Enter>' , enter_4)
lbl_img4.bind('<Leave>', leave_4)

app.img9 = Image.open("warehouse.png").resize((100, 100), Image.ANTIALIAS)
app.photo_image9 = ImageTk.PhotoImage(app.img9)
lbl_img9 = Button(image=app.photo_image9, borderwidth=0, bg="#164777", activebackground="red")
lbl_img9.place(x=470, y=410, width=150, height=150)
lbl_img9.bind('<Enter>' , enter_5)
lbl_img9.bind('<Leave>', leave_5)



app.mainloop()