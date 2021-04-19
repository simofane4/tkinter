from tkinter import *
from tkinter import ttk
from tkinter import Button
from tkinter import messagebox


from PIL import Image, ImageTk

root = Tk()
root.title("Gestion de Stock des Pièces de Rechange")
root.geometry("600x600")
root.configure(background="black")
icon = PhotoImage(file="icon.png")
root.call("wm", "iconphoto", root._w, icon)


class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)



        self.image = Image.open("log.jpg")
        self.img_copy= self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)
        self.frame = Frame(self.background, bg="black").place(x=100, y=150, width=300, height=450)

        self.img1 = Image.open("uzr.png").resize((100, 100), Image.ANTIALIAS)
        self.photo_image1 = ImageTk.PhotoImage(self.img1)
        lbl_img1 = Label(image=self.photo_image1, fg="black", bg="black").place(x=200, y=155, width=100, height=90)

        get_str = Label(self.frame, text="Commencez Now", font=("times new raman", 17, "bold"), fg="white", bg="black").place(x=160, y=250)
        User_name = lbl = Label(self.frame, text="Nom_Utilisateur", font=("time new roman", 13, "bold"), fg="white", bg="black").place(x=130, y=290)
        self.txt_user = ttk.Entry(self.frame, font=("times new roman", 13, "bold")).place(x=110, y=320, width=270)

        Password = lbl = Label(self.frame, text="Mot_de_passe", font=("time new roman", 13, "bold"), fg="white", bg="black").place(x=128, y=350)

        self.txt_pass = ttk.Entry(self.frame, show="*", font=("times new roman", 13, "bold")).place(x=110, y=380, width=270)
        #icon_image
        self.img2 = Image.open("az.jpg").resize((24, 24), Image.ANTIALIAS)
        self.photo_image2 = ImageTk.PhotoImage(self.img2)
        lbl_img2 = Label(image=self.photo_image2, fg="black", bg="black").place(x=105, y=290, width=25, height=25)

        self.img3 = Image.open("kad.png").resize((24, 24), Image.ANTIALIAS)
        self.photo_image3 = ImageTk.PhotoImage(self.img3)
        lbl_img2 = Label(image=self.photo_image3, fg="black", bg="black").place(x=104, y=350, width=24, height=24)

        self.reg_btn = Button(self.frame, text=" Nouvel Utilisateur", font=("times new roman", 10, "bold"), bd=1, fg="white", bg="black", borderwidth=0, activeforeground="white", activebackground="black").place(x=103, y=420, width=150)
        self.frg_btn = Button(self.frame, text="Mot de Passe Oublié", font=("times new roman", 10, "bold"), bd=1, fg="white", bg="black", borderwidth=0, activeforeground="white", activebackground="black").place(x=110, y=460, width=150)

        self.img4 = Image.open("tr.jpg").resize((100, 100), Image.ANTIALIAS)
        self.photo_image4 = ImageTk.PhotoImage(self.img4)

        lbl_img4 = Button(image=self.photo_image4, borderwidth=0, bg="black", activebackground="black").place(x=102, y=500, width=300, height=70)

        #self.log_btn = Button(self.frame, command=self.login(), text="Login", font=("times new roman", 15, "bold"), bd=3, bg="red").place(x=200, y=550, width=120, height=35)

    def Login(self):
        if self.txt_user.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("Error", "all field required")
        elif self.txt_user.get()=="kap" and self.txt_pass.get()=="ash":
            messagebox.showinfo("success", "welcome to code channel please sub my channel")

        else:
            messagebox.showerror("Invalid", "Invalid user_name&password")









    def _resize_image(self, event):

        new_width = event.width
        new_height = event.height
        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)




e = Example(root)
e.pack(fill=BOTH, expand=YES)



root.mainloop()
