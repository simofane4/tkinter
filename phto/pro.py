from tkinter import *
from PIL import ImageTk, Image
root = Tk()


root.title(" welcome a your system ")
root.geometry("400x400")

       # self.bg = ImageTk.PhotoImage(Image.open("py.jpg"))
       # self.bg_i = Label(self.root, image=self.bg).place(x=0, y=0)
my_menu = Menu(root)
root.config(menu=my_menu)
#creat menu
file_menu = Menu(my_menu)
my_menu.add_cascade(label="file", menu=file_menu)
file_menu.add_command(label="new...")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

#creat an edit menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="cut")
edit_menu.add_command(label="copy")

#creat option menu
option_menu = Menu(my_menu)
my_menu.add_cascade(label="option", menu=option_menu)
edit_menu.add_command(label="find")
edit_menu.add_command(label="find Next")


root.mainloop()
