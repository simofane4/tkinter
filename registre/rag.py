import tkinter as tk
from PIL import Image, ImageTk
import time
from time import strftime
from tkinter import ttk
app = tk.Tk()
#localtime = time.strftime("%H:%M:%S %y-%m-%d")

app.geometry("850x900+350+150")
app.title("Gestion de Stock des Pièces de Rechange")
app.configure(background="#6A6A6A")
app.resizable(width=False, height=True)
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







icon = tk.PhotoImage(file="icon.png")
app.call("wm", "iconphoto", app._w, icon)
app_title_frame = tk.Frame(app, width=830, height=60, bg="#4F5A60").place(x=10, y=10)
#date_lbl = tk.Label(app, text=localtime, bg="#4F5A60", fg="#E8EFF3", font=("Arial Greek", 10, "bold")).place(x=70, y=18)



my_app_title = tk.Label(app_title_frame, text="Gestion de client", bg="#4F5A60", fg="#582900", font=("Arial Greek", 17, "bold")).place(x=325, y=22)

app_title_frame2 = tk.Frame(app, width=830, height=60, bg="#4F5A59").place(x=10, y=76)

search_lbl1 = tk.Label(app, text="Entrez le ID ou le nom que vous recherchez", fg="white", font=("Arial Greek", 13), bg="#4F5A59").place(x=18, y=90)
search_lbl1 = tk.Entry(app, fg="black", font=("Arial Greek", 13, "bold"), bg="#53515F").place(x=500, y=90, width=160, height=25)
search_btn1 = tk.Button(app, text="Chercher", bg="#4F5A59", font=("Arial Greek", 12, "bold"), bd=1, fg="white", activebackground="#091833").place(x=700, y=90, width=90, height=25)
filter_date_frm = tk.LabelFrame(app, width=830, height=60, bg="#6A6A6A", bd=3, font=("Arial Greek", 9, "bold"), fg="white").place(x=10, y=140)
search_lbl3 = tk.Label(app, text="Choisissez la Période que vous Souhaitez Rechercher", fg="white", font=("Arial Greek", 13), bg="#6A6A6A").place(x=18, y=159)
from_lbl4 = tk.Label(app, text="De", fg="white", font=("Arial Greek", 13), bg="#6A6A6A").place(x=450, y=159)
from_lbl4 = tk.Entry(app, fg="black", font=("Arial Greek", 13, "bold"), bd=1, bg="white").place(x=500, y=159, width=100, height=25)
to_lbl5 = tk.Label(app, text="à", fg="white", font=("Arial Greek", 13), bg="#6A6A6A").place(x=680, y=159)
to_lbl5 = tk.Entry(app, fg="black", font=("Arial Greek", 13, "bold"), bd=1, bg="white").place(x=720, y=159, width=100, height=25)
filter_date_frm2 = tk.LabelFrame(app, width=830, height=300, bg="#6A6A6A", bd=3, font=("Arial Greek", 9, "bold"), fg="white").place(x=10, y=208)
ifm_lbl6 = tk.Label(app, text="Les Information des clients  ", fg="#A4FFF9", font=("Arial Greek", 13), bg="#6A6A6A").place(x=13, y=200)



label = tk.Label(app, text="ID_client      :", bg="#6A6A6A", font=("Arial Greek", 10, "bold"), fg="black").place(x=20, y=250)
txt_lb1 = ttk.Entry(app, font=("Arial Greek", 12, "bold")).place(x=115, y=253, width=130, height=18)

label2 = tk.Label(app, text="Nom_client  :", bg="#6A6A6A", font=("Arial Greek", 10, "bold"), fg="black").place(x=20, y=293)
txt_lb2 = ttk.Entry(app, font=("Arial Greek ", 12, "bold")).place(x=115, y=296, width=130, height=18)

label3 = tk.Label(app, text="Pré_client    :", bg="#6A6A6A", font=("Arial Greek", 10, "bold"), fg="black").place(x=20, y=336)
txt_lb3 = tk.Entry(app, font=("Arial Greek", 12, "bold")).place(x=115, y=339, width=130, height=18)


label4 = tk.Label(app, text="Email_Client :", bg="#6A6A6A", font=("Arial Greek", 10, "bold"), fg="black").place(x=400, y=250)
txt_lb4 = tk.Entry(app, font=("Arial Greek", 12, "bold")).place(x=503, y=253, width=130, height=18)

label5 = tk.Label(app, text="Télé_client    :", bg="#6A6A6A", font=("Arial Greek", 10, "bold"), fg="black").place(x=400, y=293)
txt_lb5 = ttk.Entry(app, font=("Arial Greek", 12, "bold")).place(x=503, y=296, width=130, height=18)

label6 = tk.Label(app, text="Ad_Client           :", bg="#6A6A6A", font=("Arial Greek", 9, "bold"), fg="black").place(x=400, y=336)
txt_lb6 = tk.Entry(app, font=("Arial Greek", 12, "bold")).place(x=503, y=339, width=130, height=18)

# information de Fourniseur

#label_four = tk.Label(app, text="ID_Four         :", bg="#6A6A6A", font=("Arial Greek", 9, "bold"), fg="black").place(x=430, y=230)
#txt_lbl_four = ttk.Entry(app, font=("Arial Greek", 12, "bold")).place(x=512, y=233, width=130, height=18)

#label_four2 = tk.Label(app, text="Nom_Four    :", bg="#6A6A6A", font=("Arial Greek", 9, "bold"), fg="black").place(x=430, y=273)
#txt_lb2_Four = ttk.Entry(app, font=("Arial Greek ", 12, "bold")).place(x=512, y=276, width=130, height=18)


#label3_four = tk.Label(app, text="Pré_Four      :", bg="#6A6A6A", font=("Arial Greek", 9, "bold"), fg="black").place(x=430, y=316)
#txt_lb3_Four = tk.Entry(app, font=("Arial Greek", 12, "bold")).place(x=512, y=319, width=130, height=18)


#label4_four = tk.Label(app, text="Email_Four  :", bg="#6A6A6A", font=("Arial Greek", 9, "bold"), fg="black").place(x=430, y=359)
#txt_lb4_Four = tk.Entry(app, font=("Arial Greek", 12, "bold")).place(x=512, y=362, width=130, height=18)


#label5_Four = tk.Label(app, text="Télé_Four    :", bg="#6A6A6A", font=("Arial Greek", 9, "bold"), fg="black").place(x=430, y=402)
#txt_lb5_Four = ttk.Entry(app, font=("Arial Greek", 12, "bold")).place(x=512, y=405, width=130, height=18)


#label6_Four = tk.Label(app, text="Ad_Four       :", bg="#6A6A6A", font=("Arial Greek", 9, "bold"), fg="black").place(x=430, y=445)
#txt_lb6_Four = tk.Entry(app, font=("Arial Greek", 12, "bold")).place(x=512, y=448, width=130, height=18)

Super_btn3 = tk.Button(app, text="Supermier", bg="#4F5A69", font=("Arial Greek", 11, "bold"), bd=1, fg="white", activebackground="#091833").place(x=470, y=420, width=100, height=25)
Mod_btn3 = tk.Button(app, text="Modifier", bg="#4F5A69", font=("Arial Greek", 11, "bold"), bd=1, fg="white", activebackground="#091833").place(x=325, y=420, width=100, height=25)
Super_btn3 = tk.Button(app, text="Ajouter", bg="#4F5A69", font=("Arial Greek", 11, "bold"), bd=1, fg="white", activebackground="#091833").place(x=180, y=420, width=100, height=25)


filter_date_frmF = tk.LabelFrame(app, width=830, height=330, bg="#6A6A6A", bd=3, font=("Arial Greek", 9, "bold"), fg="white").place(x=10, y=525)
ifm_lbl_F = tk.Label(app, text="Liste des Employés ", fg="#A4FFF9", font=("Arial Greek", 13), bg="#6A6A6A").place(x=13, y=510)

Super_btn3 = tk.Button(app, text="Afficher les Données", bg="#4F5A69", font=("Arial Greek", 9, "bold"), bd=1, fg="#582900", activebackground="#091833").place(x=700, y=470, width=130, height=25)



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

tree.place(x=17, y=543, width=815)
#tree.pack()



app.mainloop()

