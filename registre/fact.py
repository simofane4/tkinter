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



app_title_frameF = tk.Frame(app, width=830, height=60, bg="#4F5A8B").place(x=10, y=10)


#Fact_date_lbl = tk.Label(app, text=localtime, bg="#4F5A8B", fg="#E8EFF3", font=("Arial Greek", 10, "bold")).place(x=70, y=18)

my_app_title = tk.Label(app_title_frameF, text="Gestion de Facturisation ", bg="#4F5A8B", fg="#6E0B4F", font=("Arial Greek", 17, "bold")).place(x=325, y=22)

List_fact_frm2 = tk.LabelFrame(app, width=830, height=450, bg="#4F5A5E", bd=4, font=("Arial Greek", 9, "bold"), fg="white").place(x=10, y=78)




List_fact_frm_ca = tk.LabelFrame(app, width=290, height=300, bg="#4F5A5E", bd=4, font=("Arial Greek", 9, "bold"), fg="white").place(x=535, y=110)


fact_lbl5 = tk.Label(app, text="Calculatrice ", fg="#A4FFF9", font=("Arial Greek", 12), bg="#4F5A5E").place(x=535, y=105)




def btnClick(number):
    global operator
    operator = operator+str(number)
    text_Input.set(operator)
operator = ""
text_Input = tk.StringVar()

def btnclearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def btnEqualsInpt():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

    #app.insert(0, number)
fact_lbl4 = tk.Entry(app, text=text_Input, fg="black", font=("Arial Greek", 13, "bold"), bg="white").place(x=584, y=150, width=210, height=35)


Ges_fact_vent4 = tk.Button(app, text="7", command=lambda:btnClick(7), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=586, y=200, width=40, height=25)
Ges_fact_vent5 = tk.Button(app, text="8", command=lambda:btnClick(8), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=642, y=200, width=40, height=25)
Ges_fact_vent6 = tk.Button(app, text="9", command=lambda:btnClick(9), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=698, y=200, width=40, height=25)
Ges_fact_vent7 = tk.Button(app, text="+", command=lambda:btnClick("+"),  bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=754, y=200, width=40, height=25)

Ges_fact_vent8 = tk.Button(app, text="4", command=lambda:btnClick(4), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=586, y=241, width=40, height=25)
Ges_fact_vent9 = tk.Button(app, text="5", command=lambda:btnClick(5), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=642, y=241, width=40, height=25)
Ges_fact_vent10 = tk.Button(app, text="6", command=lambda:btnClick(6), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=698, y=241, width=40, height=25)
Ges_fact_vent11 = tk.Button(app, text="-", command=lambda:btnClick("-"), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=754, y=241, width=40, height=25)


Ges_fact_vent12 = tk.Button(app, text="1", command=lambda:btnClick(1), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=586, y=282, width=40, height=25)
Ges_fact_vent13 = tk.Button(app, text="2", command=lambda:btnClick(2), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=642, y=282, width=40, height=25)
Ges_fact_vent14 = tk.Button(app, text="3", command=lambda:btnClick(3), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=698, y=282, width=40, height=25)
Ges_fact_vent11 = tk.Button(app, text="*", command=lambda:btnClick("*"), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=754, y=282, width=40, height=25)


Ges_fact_vent15 = tk.Button(app, text="0", command=lambda:btnClick(0), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=586, y=323, width=40, height=25)
Ges_fact_vent16 = tk.Button(app, text="C", command=btnclearDisplay, bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=642, y=323, width=40, height=25)
Ges_fact_vent17 = tk.Button(app, text="/", command=lambda:btnClick("/"), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=698, y=323, width=40, height=25)
Ges_fact_vent18 = tk.Button(app, text="=", command=btnEqualsInpt, bg="#6E0B14", font=("Arial Greek", 11, "bold"), bd=1, fg="white", activebackground="#091833").place(x=754, y=323, width=40, height=25)


search_btn1_fact = tk.Button(app, text="Chercher", bg="#4F5A5E", font=("Arial Greek", 10, "bold"), bd=1, fg="#6E0B16", activebackground="#091833").place(x=50, y=105, width=80, height=25)
filter_Ges_frm4 = tk.LabelFrame(app, width=150, height=40, bg="#4F5A5E", bd=3, font=("Arial Greek", 9, "bold"), fg="white").place(x=160, y=100)
fact_lbl20 = tk.Label(app, text="Id_Commande ", fg="#A4FFF9", font=("Arial Greek", 10), bg="#4F5A5E").place(x=159, y=88)
fact_lbl21 = tk.Entry(app, fg="black", font=("Arial Greek", 13, "bold"), bg="white").place(x=171, y=110, width=128, height=20)



filter_Ges_frm4 = tk.LabelFrame(app, width=150, height=40, bg="#4F5A5E", bd=3, font=("Arial Greek", 9, "bold"), fg="white").place(x=350, y=100)
fact_lbl22 = tk.Label(app, text="Date_Commande ", fg="#A4FFF9", font=("Arial Greek", 10), bg="#4F5A5E").place(x=349, y=88)
fact_lbl23 = tk.Entry(app, fg="black", font=("Arial Greek", 13, "bold"), bg="white").place(x=361, y=110, width=128, height=20)


fact_label24 = tk.Label(app, text="ID_Facture          :", bg="#4F5A5E", font=("Arial Greek", 10, "bold"), fg="black").place(x=40, y=230)
txt_fact_lb25 = ttk.Entry(app, font=("Arial Greek", 12, "bold")).place(x=190, y=233, width=130, height=18)


fact_label26 = tk.Label(app, text="Date_Facture      :", bg="#4F5A5E", font=("Arial Greek", 10, "bold"), fg="black").place(x=40, y=273)
txt_fact_lb27 = ttk.Entry(app, font=("Arial Greek", 12, "bold")).place(x=190, y=276, width=130, height=18)



Ges_fact19 = tk.Button(app, text="Enregistre", bg="#6E0B14", font=("Arial Greek", 11, "bold"), bd=1, fg="white", activebackground="#091833").place(x=40, y=410, width=100, height=25)
fact_Mod_btn3 = tk.Button(app, text="Modifier", bg="#6E0B14", font=("Arial Greek", 11, "bold"), bd=1, fg="white", activebackground="#091833").place(x=180, y=410, width=100, height=25)
Ges_vent_btn2 = tk.Button(app, text="Annuler", bg="#6E0B14", font=("Arial Greek", 11, "bold"), bd=1, fg="white", activebackground="#091833").place(x=320, y=410, width=100, height=25)



Ges_vent_btn5 = tk.Button(app, text="Afficher les Données", bg="#4F5A5E", font=("Arial Greek", 9, "bold"), bd=1, fg="#6E0B71", activebackground="#091833").place(x=700, y=450, width=130, height=25)

List_fact_frm5 = tk.LabelFrame(app, width=830, height=300, bg="#4F5A5E", bd=4, font=("Arial Greek", 9, "bold"), fg="white").place(x=10, y=540)

tree = ttk.Treeview(app)

tree["columns"] = ("one", "two")
tree.column("one", width=150)
tree.column("two", width=100)
tree.heading("one", text="column A")
tree.heading("two", text="column B")

tree.place(x=17, y=550, width=815)
#tree.pack()




lbl2 = tk.Label(app, font=("times new roman", 13, "bold"), bg="#4F5A8B")
def clock():
    string = strftime('%y-%m-%d' '  ''%H:%M:%S %p')
    lbl2.config(text=string)
    lbl2.after(1000,clock)
clock()
lbl2.pack()
lbl2.place(x=10,y=10)

#hour = time.strftime("%H")
#minute = time.strftime("%M")

#second = time.strftime("%S")
#day = time.strftime("%y")
#ans = time.strftime("%m")
#ans1 = time.strftime("%d")



app.mainloop()
