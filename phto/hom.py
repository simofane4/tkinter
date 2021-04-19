from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import time
from tkinter import ttk
from time import strftime

app = tk.Tk()

app.geometry("850x900+350+150")
app.title("Gestion de Stock des Pièces de Rechange")
app.configure(background="#6A6A6A")
app.resizable(width=False, height=True)
#localtime = time.strftime("%H:%M:%S %y-%m-%d")
icon = tk.PhotoImage(file="icon.png")
app.call("wm", "iconphoto", app._w, icon)





class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)



        self.image = Image.open("log.jpg")
        self.img_copy= self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = tk.Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)




    def _resize_image(self, event):

        new_width = event.width
        new_height = event.height
        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)
a = Example(app)
a.pack(fill=BOTH, expand=YES)

app.mainloop()








app.mainloop()
