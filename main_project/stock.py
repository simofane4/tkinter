import tkinter as tk
from PIL import Image, ImageTk
import time
from time import strftime
from tkinter import ttk
app = tk.Tk()

app.geometry("850x700+350+150")
app.title("Gestion de Stock des Pièces de Rechange")
app.configure(background="#0b2239")
app.resizable(width=False, height=True)


#localtime = time.strftime("%H:%M:%S %y-%m-%d")
icon = tk.PhotoImage(file="assets/icon.png")
app.call("wm", "iconphoto", app._w, icon)




top_menu = tk.Menu(app)
app.config(menu=top_menu)
Menu1 = tk.Menu(top_menu)
top_menu.add_cascade(menu=Menu1, label="file")
Menu1.add_command(label="new...")
Menu1.add_command(label="copier")

Menu1.add_separator()
Menu1.add_command(label="Quitter", command=app.quit)

option_menu = tk.Menu(top_menu)
top_menu.add_cascade(menu=option_menu, label="Gestion")
option_menu.add_command(label="Home")
option_menu.add_command(label="Gestion de Stock")
option_menu.add_command(label="Gestion de vente")
option_menu.add_command(label="Gestion de Achat")
option_menu.add_command(label="Gestion de client")
option_menu.add_command(label="Gestion de Fournisseur")
option_menu.add_command(label="Factorisation")

Aider_menu = tk.Menu(top_menu)
top_menu.add_cascade(menu=Aider_menu, label="A Propre")








app_title_frame = tk.Frame(app, width=830, height=60, bg="#4F5A60").place(x=10, y=10)
#date_lbl = tk.Label(app, text=localtime, bg="#4F5A60", fg="#E8EFF3", font=("times new roman", 10, "bold")).place(x=70, y=18)

my_Ges_title2 = tk.Label(app_title_frame, text="Gestion de Stock", bg="#4F5A60", fg="white", font=("times new roman", 17, "bold")).place(x=325, y=22)

app_Ges_frame2 = tk.Frame(app, bd=3, width=830, height=60, bg="#4F5A59").place(x=10, y=76)
search_lbl1 = tk.Label(app, text="Entrez le ID ou le nom de Pièece que vous recherchez", fg="white", font=("times new roman", 13), bg="#4F5A59").place(x=18, y=90)

filter_Ges_frm2 = tk.LabelFrame(app, width=150, height=40, bg="#4F5A59", bd=3, font=("times new roman", 11, "bold"), fg="white").place(x=440, y=85)
Ges_lbl6 = tk.Label(app, text="Le Nom de Pièce ", fg="#A4FFF9", font=("times new roman", 11), bg="#4F5A59").place(x=440, y=80)
Ges_lbl1 = tk.Entry(app, fg="black", font=("times new roman", 13, "bold"), bg="white").place(x=450, y=99, width=128, height=20)

filter_Ges_frm4 = tk.LabelFrame(app, width=150, height=40, bg="#4F5A59", bd=3, font=("times new roman", 11, "bold"), fg="white").place(x=595, y=85)
Ges_lbl4 = tk.Label(app, text="Id_Pièce ", fg="#A4FFF9", font=("times new roman", 11), bg="#4F5A59").place(x=595, y=77)
Ges_lbl4 = tk.Entry(app, fg="black", font=("times new roman", 13, "bold"), bg="white").place(x=605, y=99, width=128, height=20)


search_btn1_Ges = tk.Button(app, text="Chercher", bg="#4F5A59", font=("times new roman", 12, "bold"), bd=1, fg="#582900", activebackground="#091833").place(x=760, y=90, width=70, height=25)



filter_Ges_frm5 = tk.LabelFrame(app, width=830, height=330, bg="#6A6A6A", bd=3, font=("times new roman", 11, "bold"), fg="white").place(x=10, y=150)
Ges_lbl5 = tk.Label(app, text="Les Information Des Pièces", fg="#A4FFF9", font=("times new roman", 12), bg="#6A6A6A").place(x=10, y=146)


label = tk.Label(app, text="ID_Pièce  :", bg="#6A6A6A", font=("times new roman", 10, "bold"), fg="black").place(x=245, y=190)

txt_Ges_lb1 = ttk.Entry(app, font=("times new roman", 12, "bold")).place(x=320, y=193, width=130, height=18)


label = tk.Label(app, text="Nom_Pièce     :", bg="#6A6A6A", font=("times new roman", 10, "bold"), fg="black").place(x=12, y=230)
txt_Ges_lb1 = ttk.Entry(app, font=("times new roman", 12, "bold")).place(x=120, y=233, width=130, height=18)


label2 = tk.Label(app, text="Type_Pièce     :", bg="#6A6A6A", font=("times new roman", 10, "bold"), fg="black").place(x=12, y=273)
txt_lb2 = ttk.Entry(app, font=("times new roman ", 12, "bold")).place(x=120, y=276, width=130, height=18)


label4 = tk.Label(app, text="Poid_Pièce     :", bg="#6A6A6A", font=("times new roman", 10, "bold"), fg="black").place(x=12, y=310)
txt_lb4 = tk.Entry(app, font=("times new roman", 12, "bold")).place(x=120, y=313, width=130, height=18)


label5 = tk.Label(app, text="Prix_Achat      :", bg="#6A6A6A", font=("times new roman", 10, "bold"), fg="black").place(x=12, y=353)
txt_lb4 = tk.Entry(app, font=("times new roman", 12, "bold")).place(x=120, y=356, width=130, height=18)


label_Ges = tk.Label(app, text="Pay_Origine  :", bg="#6A6A6A", font=("times new roman", 10, "bold"), fg="black").place(x=415, y=230)
txt_lbl_four = ttk.Entry(app, font=("times new roman", 12, "bold")).place(x=512, y=233, width=130, height=18)


label_Ges2 = tk.Label(app, text="Qualité_pièce:", bg="#6A6A6A", font=("times new roman", 10, "bold"), fg="black").place(x=415, y=273)
txt_lb2_Ges = ttk.Entry(app, font=("times new roman ", 12, "bold")).place(x=512, y=276, width=130, height=18)

label3_Ges = tk.Label(app, text="Quantité_Max:", bg="#6A6A6A", font=("times new roman", 10, "bold"), fg="black").place(x=415, y=316)
txt_lb3_Ges = tk.Entry(app, font=("times new roman", 12, "bold")).place(x=512, y=319, width=130, height=18)

label4_Ges = tk.Label(app, text="Prix_Vent      :", bg="#6A6A6A", font=("times new roman", 10, "bold"), fg="black").place(x=415, y=359)
txt_lb4_Ges = tk.Entry(app, font=("times new roman", 12, "bold")).place(x=512, y=362, width=130, height=18)




Ges_Super_btn3 = tk.Button(app, text="Supprimer", bg="#4F5A69", font=("times new roman", 11, "bold"), bd=1, fg="white", activebackground="#091833").place(x=470, y=420, width=100, height=25)
Ges_Super_btn3 = tk.BuGes_Mod_btn3 = tk.Button(app, text="Modifier", bg="#4F5A69", font=("times new roman", 11, "bold"), bd=1, fg="white", activebackground="#091833").place(x=325, y=420, width=100, height=25)
Ges_btn5 = tk.Button(app, text="Ajouter", bg="#4F5A69", font=("times new roman", 11, "bold"), bd=1, fg="white", activebackground="#091833").place(x=180, y=420, width=100, height=25)


Ges_Super_btn4 = tk.Button(app, text="Afficher les Données", bg="#4F5A69", font=("times new roman", 11, "bold"), bd=1, fg="white", activebackground="#091833").place(x=680, y=420, width=150, height=25)



List_Ges_frm5 = tk.LabelFrame(app, width=830, height=200, bg="#6A6A6A", bd=3, font=("times new roman", 11, "bold"), fg="white").place(x=10, y=492)








liste_Ges_lbl5 = tk.Label(app, text="Liste Des Pièces", fg="#A4FFF9", font=("times new roman", 12), bg="#6A6A6A").place(x=10, y=480)




lbl2 = tk.Label(app, font=("times new roman", 13, "bold"), bg="#4F5A60")



def clock():
    string = strftime('%y-%m-%d' '  ''%H:%M:%S %p')
    lbl2.config(text=string)
    lbl2.after(1000,clock)
clock()
lbl2.pack()
lbl2.place(x=10,y=10)


tree = ttk.Treeview(app)

tree["columns"] = ("one", "two")
tree.column("one", width=150)
tree.column("two", width=100)
tree.heading("one", text="column A")
tree.heading("two", text="column B")

tree.place(x=17, y=505, width=815)
#tree.pack()









app.mainloop()
