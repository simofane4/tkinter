from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

root = Tk()
root.title("Gestion de Stock des Pièeces de rechange")
root.geometry("600x600")
root.configure(background="black")
icon = PhotoImage(file="icon.png")
root.call("wm", "iconphoto", root._w, icon)




class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)



        self.image = Image.open("si.jpg")
        self.img_copy= self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        #frame
        self.frame = Frame(self.background, bg="gray").place(x=100, y=170, width=300, height=450)



        self.img1 = Image.open("ico.jpg").resize((17, 17), Image.ANTIALIAS)
        self.photo_image1 = ImageTk.PhotoImage(self.img1)
        lbl_img1 = Label(image=self.photo_image1, fg="black", bg="gray").place(x=102, y=200, width=23, height=29)



        family_name = lbl = Label(self.frame, text="Nom_Utilisateur", font=("times new roman", 13, "bold"), fg="white", bg="gray").place(x=120, y=200)

        self.txt_user = ttk.Entry(self.frame, font=("times new roman", 13, "bold")).place(x=110, y=230, width=270)


        self.img2 = Image.open("p.jpg").resize((17, 17), Image.ANTIALIAS)
        self.photo_image2 = ImageTk.PhotoImage(self.img2)
        lbl_img2 = Label(image=self.photo_image2, fg="black", bg="gray").place(x=102, y=260, width=23, height=29)




        first_name = lbl = Label(self.frame, text="Prénom_utilisateur", font=("times new roman", 13, "bold"), fg="white", bg="gray").place(x=120, y=260)
        self.txt_first = ttk.Entry(self.frame, font=("times new roman", 13, "bold")).place(x=110, y=290, width=270)


        email = lbl = Label(self.frame, text="Email_utilisateur", font=("times new roman", 14, "bold"), fg="white", bg="gray").place(x=120, y=320)
        self.txt_email = ttk.Entry(self.frame, font=("times new roman", 13, "bold")).place(x=110, y=348, width=270)

        self.img3 = Image.open("ema.jpg").resize((15, 15), Image.ANTIALIAS)
        self.photo_image3 = ImageTk.PhotoImage(self.img3)
        lbl_img3 = Label(image=self.photo_image3, fg="black", bg="gray").place(x=102, y=320, width=23, height=29)




        self.img4 = Image.open("pas.jpg").resize((14, 14), Image.ANTIALIAS)
        self.photo_image4 = ImageTk.PhotoImage(self.img4)
        lbl_img4 = Label(image=self.photo_image4, fg="black", bg="gray").place(x=102, y=375, width=23, height=29)





        password = lbl = Label(self.frame, text="Mot_de Passe", font=("times new roman", 13, "bold"), fg="white", bg="gray").place(x=120, y=375)
        self.txt_pas = ttk.Entry(self.frame, show="*", font=("times new roman", 13, "bold")).place(x=110, y=400, width=270)



        self.img5 = Image.open("ver.png").resize((20, 20), Image.ANTIALIAS)
        self.photo_image5 = ImageTk.PhotoImage(self.img5)
        lbl_img5 = Label(image=self.photo_image5, fg="black", bg="gray").place(x=104, y=425, width=12, height=26)


        confirm_passe = lbl = Label(self.frame, text=" confirme_Mot_de_Passe", font=("times new roman", 13, "bold"), fg="white", bg="gray").place(x=116, y=425)
        self.txt_passe = ttk.Entry(self.frame, show="*", font=("times new roman", 13, "bold")).place(x=110, y=450, width=270)


        check_btn=Checkbutton(self.frame, text="J'accepte Tous les Condition ", font=("times new roman", 11, "bold")).place(x=110, y=499)

        self.log_btn = Button(self.frame, text="Login", font=("times new roman", 15, "bold"), bd=3, bg="gray").place(x=200, y=550, width=120, height=35 )

    # self.img1 = Image.open("la.jpg").resize((100, 100), Image.ANTIALIAS)
        #self.photo_image1 = ImageTk.PhotoImage(self.img1)

        #lbl_img1 = Button(image=self.photo_image1, borderwidth=0, bg="gray").place(x=130, y=530, width=90)




    def _resize_image(self, event):

        new_width = event.width
        new_height = event.height
        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)

e = Example(root)
e.pack(fill=BOTH, expand=YES)

root.mainloop()
