from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

root = Tk()
root.title("Gestion de Stock des Pièeces de rechange")
root.geometry("600x700")
root.configure(background="black")
root.resizable(width=False, height=False)
icon = PhotoImage(file="assets/icon.png")
root.call("wm", "iconphoto", root._w, icon)




class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)



        self.image = Image.open("assets/bg_top.jpg")
        self.img_copy= self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        #frame
      


     


       


        email = lbl = Label(root, text="Email_utilisateur", font=("times new roman", 14, "bold"), fg="white", bg="#b2a489")
        email.place(x=170, y=320)
        self.txt_email = ttk.Entry(root, font=("times new roman", 13, "bold")).place(x=160, y=348, width=270 , height= 29)

        self.img3 = Image.open("assets/ema.jpg").resize((15, 15), Image.ANTIALIAS)
        self.photo_image3 = ImageTk.PhotoImage(self.img3)
        lbl_img3 = Label(image=self.photo_image3, fg="black", bg="#b2a489")
        lbl_img3.place(x=152, y=320, width=23, height=29)




        self.img4 = Image.open("assets/pas.jpg").resize((14, 14), Image.ANTIALIAS)
        self.photo_image4 = ImageTk.PhotoImage(self.img4)
        lbl_img4 = Label(image=self.photo_image4, fg="black", bg="#b2a489")
        lbl_img4.place(x=152, y=375, width=23, height=29)





        password = lbl = Label(root, text="Mot_de Passe", font=("times new roman", 13, "bold"), fg="white", bg="#b2a489")
        password.place(x=170, y=375)
        self.txt_pas = ttk.Entry(root, show="*", font=("times new roman", 13, "bold"))
        self.txt_pas.place(x=160, y=400, width=270,height=29)



        

        

        check_btn=Checkbutton(root, text="remember me!", font=("times new roman", 11, "bold") , bg="#b2a489" )
        check_btn.place(x=160, y=499)

        log_btn = Button(root, text="Login", font=("times new roman", 15, "bold"), bd=3, bg="#b2a489")
        log_btn.place(x=120, y=550, width=170, height=35 )
        log_btn = Button(root, text="Register", font=("times new roman", 15, "bold"), bd=3, bg="#b2a489")
        log_btn.place(x=300, y=550, width=170, height=35 )


    # self.img1 = Image.open("la.jpg").resize((100, 100), Image.ANTIALIAS)
        #self.photo_image1 = ImageTk.PhotoImage(self.img1)

        #lbl_img1 = Button(image=self.photo_image1, borderwidth=0, bg="#b2a489").place(x=130, y=530, width=90)




    def _resize_image(self, event):

        new_width = event.width
        new_height = event.height
        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)

e = Example(root)
e.pack(fill=BOTH, expand=YES)

root.mainloop()
