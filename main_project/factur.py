from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import time
from tkinter import ttk
from time import strftime

app = tk.Tk()


app.geometry("1000x700+350+150")
app.title("Gestion de Stock des Pièces de Rechange")
app.configure(background='#0b2239')
app.resizable(width=False, height=False)




icon = tk.PhotoImage(file="assets/icon.png")
app.call("wm", "iconphoto", app._w, icon)

app.img1 = Image.open("assets/invoice.png").resize((80, 80), Image.ANTIALIAS)
app.photo_image1 = ImageTk.PhotoImage(app.img1)
label_icon = Label(image=app.photo_image1, fg="black", bg="#0b2239").place(x=20, y=15, width=80, height=80)
label_title = Label(app, text="Factur  ", fg="white", font=("Times New roman", 16), bg='#0b2239').place(x=115, y=40)

search_lbl1 = Label(app, text="Entrez le ID ou le nom que vous recherchez", fg="white", font=("Times New roman", 13), bg="#0b2239")
search_lbl1.place(x=250, y=143)
search_lbl1 = Entry(app, fg="black", font=("Arial Greek", 13, "bold"), bg="#164777")
search_lbl1.place(x=600, y=140, width=220, height=30)
search_btn1 = Button(app, text="Chercher", bg="#164777", font=("Times New roman", 12, "bold"), bd=1, fg="#6E0B14", activebackground="#091833")
search_btn1.place(x=840, y=140, width=120, height=30)


text_Input = tk.StringVar()

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

fact_lbl4 = Entry(app, text=text_Input, fg="black", font=("Arial Greek", 13, "bold"), bg="white").place(x=10, y=515 , width=190, height=35)


Ges_fact_vent4 = Button(app, text="7", command=lambda:btnClick(7), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833")
Ges_fact_vent4.place(x=10, y=555, width=40, height=25)
Ges_fact_vent5 = Button(app, text="8", command=lambda:btnClick(8), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=60, y=555, width=40, height=25)
Ges_fact_vent6 = Button(app, text="9", command=lambda:btnClick(9), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=110, y=555, width=40, height=25)
Ges_fact_vent7 = Button(app, text="+", command=lambda:btnClick("+"),  bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=160, y=555, width=40, height=25)

Ges_fact_vent8 = Button(app, text="4", command=lambda:btnClick(4), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=10, y=590, width=40, height=25)
Ges_fact_vent9 = Button(app, text="5", command=lambda:btnClick(5), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=60, y=590, width=40, height=25)
Ges_fact_vent10 = Button(app, text="6", command=lambda:btnClick(6), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=110, y=590, width=40, height=25)
Ges_fact_vent11 = Button(app, text="-", command=lambda:btnClick("-"), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=160, y=590, width=40, height=25)


Ges_fact_vent12 = Button(app, text="1", command=lambda:btnClick(1), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=10, y=625, width=40, height=25)
Ges_fact_vent13 = Button(app, text="2", command=lambda:btnClick(2), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=60, y=625, width=40, height=25)
Ges_fact_vent14 = Button(app, text="3", command=lambda:btnClick(3), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=110, y=625, width=40, height=25)
Ges_fact_vent11 = Button(app, text="*", command=lambda:btnClick("*"), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=160, y=625, width=40, height=25)


Ges_fact_vent15 = Button(app, text="0", command=lambda:btnClick(0), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=10, y=660, width=40, height=25)
Ges_fact_vent16 = Button(app, text="C", command=btnclearDisplay, bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=60, y=660, width=40, height=25)
Ges_fact_vent17 = Button(app, text="/", command=lambda:btnClick("/"), bg="#4F5A5E", font=("Arial Greek", 11, "bold"), bd=1, fg="#6E0B14", activebackground="#091833").place(x=110, y=660, width=40, height=25)
Ges_fact_vent18 = Button(app, text="=", command=btnEqualsInpt, bg="#6E0B14", font=("Arial Greek", 11, "bold"), bd=1, fg="white", activebackground="#091833").place(x=160, y=660, width=40, height=25)

Ges_vent_btn5 = Button(app, text="Afficher les Données", bg="#4F5A5E", font=("Arial Greek", 9, "bold"), bd=1, fg="#6E0B71", activebackground="#091833").place(x=700, y=450, width=130, height=25)



tree = ttk.Treeview(app)

tree["columns"] = ("1", "2","3","4")
tree.column("1", width=100)
tree.column("2", width=100)
tree.column("3", width=100)
tree.column("4", width=100)
tree.heading("1", text="column A")
tree.heading("2", text="column B")
tree.heading("3", text="column C")
tree.heading("4", text="column D")




tree.place(x=210, y=180, width=780,height=500)




app.mainloop()