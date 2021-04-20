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









app_title_frame = tk.Frame(app, width=830, height=60, bg="#4F5A6B").place(x=10, y=10)

#vent_date_lbl = tk.Label(app, text=localtime, bg="#4F5A6B", fg="#E8EFF3", font=("times new roman", 10, "bold")).place(x=70, y=18)

my_vent_title2 = tk.Label(app_title_frame, text="Gestion de vente", bg="#4F5A6B", fg="white", font=("times new roman", 17, "bold")).place(x=325, y=22)

app_vent_frame1 = tk.Frame(app, bd=3, width=830, height=60, bg="#4F5A5E").place(x=10, y=76)

List_vent_frm2 = tk.LabelFrame(app, width=830, height=405, bg="#4F5A5E", bd=4, font=("times new roman", 9, "bold"), fg="white").place(x=10, y=78)
vent_lbl5 = tk.Label(app, text="Les Information De vente", fg="#A4FFF9", font=("times new roman", 12), bg="#6A6A6A").place(x=10, y=75)

search_btn1_Ges = tk.Button(app, text="Chercher", bg="#4F5A5E", font=("times new roman", 10, "bold"), bd=1, fg="#6E0B16", activebackground="#091833").place(x=90, y=117, width=80, height=25)
filter_Ges_frm4 = tk.LabelFrame(app, width=150, height=40, bg="#4F5A5E", bd=3, font=("times new roman", 9, "bold"), fg="white").place(x=200, y=105)
vent_lbl4 = tk.Label(app, text="Id_Commande ", fg="#A4FFF9", font=("times new roman", 10), bg="#4F5A5E").place(x=199, y=94)
vent_lbl4 = tk.Entry(app, fg="black", font=("times new roman", 13, "bold"), bg="white").place(x=211, y=117, width=128, height=20)



filter_Ges_frm4 = tk.LabelFrame(app, width=150, height=40, bg="#4F5A5E", bd=3, font=("times new roman", 9, "bold"), fg="white").place(x=450, y=105)
vent_lbl4 = tk.Label(app, text="Date_Commande ", fg="#A4FFF9", font=("times new roman", 10), bg="#4F5A5E").place(x=449, y=94)
vent_lbl4 = tk.Entry(app, fg="black", font=("times new roman", 13, "bold"), bg="white").place(x=461, y=117, width=128, height=20)

vent_label6 = tk.Label(app, text="ID_Client    :", bg="#4F5A5E", font=("times new roman", 10, "bold"), fg="black").place(x=190, y=190)
txt_vent_lb6 = ttk.Entry(app, font=("times new roman", 12, "bold")).place(x=290, y=193, width=130, height=18)

vent_label7 = tk.Label(app, text="ID_Commande          :", bg="#4F5A5E", font=("times new roman", 10, "bold"), fg="black").place(x=40, y=230)
txt_vent_lb7 = ttk.Entry(app, font=("times new roman", 12, "bold")).place(x=190, y=233, width=130, height=18)

vent_label8 = tk.Label(app, text="Quantité_commande :", bg="#4F5A5E", font=("times new roman", 10, "bold"), fg="black").place(x=40, y=273)
txt_vent_lb8 = ttk.Entry(app, font=("times new roman", 12, "bold")).place(x=190, y=276, width=130, height=18)


vent_label9 = tk.Label(app, text="Quantité_commande :", bg="#4F5A5E", font=("times new roman", 10, "bold"), fg="black").place(x=40, y=316)
txt_vent_lb9 = ttk.Entry(app, font=("times new roman", 12, "bold")).place(x=190, y=319, width=130, height=18)


label_vent10 = tk.Label(app, text="Date_Commande   :", bg="#4F5A5E", font=("times new roman", 9, "bold"), fg="black").place(x=470, y=230)
txt_lbl_vent = ttk.Entry(app, font=("times new roman", 12, "bold")).place(x=595, y=233, width=130, height=18)



Ges_vent_btn2 = tk.Button(app, text="Supermier", bg="#4F5A5E", font=("times new roman", 11, "bold"), bd=1, fg="white", activebackground="#091833").place(x=470, y=380, width=100, height=25)
Ges_Mod_btn3 = tk.Button(app, text="Modifier", bg="#4F5A5E", font=("times new roman", 11, "bold"), bd=1, fg="white", activebackground="#091833").place(x=325, y=380, width=100, height=25)

Ges_vent_vent4 = tk.Button(app, text="Ajouter", bg="#4F5A5E", font=("times new roman", 11, "bold"), bd=1, fg="white", activebackground="#091833").place(x=180, y=380, width=100, height=25)
Ges_vent_btn5 = tk.Button(app, text="Afficher les Données", bg="#4F5A5E", font=("times new roman", 9, "bold"), bd=1, fg="#6E0B27", activebackground="#091833").place(x=700, y=420, width=130, height=25)






List_vent_frm5 = tk.LabelFrame(app, width=830, height=300, bg="#4F5A5E", bd=4, font=("times new roman", 9, "bold"), fg="white").place(x=10, y=492)
vent_lbl5 = tk.Label(app, text="Liste De vente", fg="#A4FFF9", font=("times new roman", 12), bg="#6A6A6A").place(x=10, y=480)


lbl2 = tk.Label(app, font=("times new roman", 13, "bold"), bg="#4F5A6B")
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

tree.place(x=17, y=504, width=815)
#tree.pack()



app.mainloop()