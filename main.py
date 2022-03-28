

# ----------------------------------------------------------------------------------------------------------------------

# Importando os pacotes nescessários


import tkinter as tk
from tkinter import *
import mysql.connector
from tkinter import ttk
from time import strftime
from PIL import ImageTk, Image
from tkinter import messagebox

# ----------------------------------------------------------------------------------------------------------------------










# ----------------------------------------------------------------------------------------------------------------------

# Realizando conexão com banco de dados MYSQL

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="outro"
)

cursor = banco.cursor()

# ----------------------------------------------------------------------------------------------------------------------










# ----------------------------------------------------------------------------------------------------------------------

# Funções do programa

def center(win):
    win.update_idletasks()

    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width

    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width

    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2

    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    win.deiconify()

# ---------------------------------------------------------------

def atualizar():
    m.update()
    root.update()
    m.update()

# ---------------------------------------------------------------

def time():
    string = strftime('%H:%M:%S')
    hora.config(text=string)
    hora.after(1000, time)

# ---------------------------------------------------------------

def date():
    string = strftime('%d/%m/%Y')
    data.config(text=("Data: " + string))


# ---------------------------------------------------------------

def adicionarCarro():

    def db():

        # Realizando conexão com banco de dados MYSQL
        banco = mysql.connector.connect(host="localhost", user="root", password="", database="outro")
        cursor2 = banco.cursor()

        aa = "SELECT id FROM estacionamento"

        cursor2.execute(aa)
        recordes1 = cursor2.fetchone()

        global b

        a = (int(recordes1[0]) + int(1))
        b = str(a)

        print(b)


    def enviar():

        db()


        # Realizando conexão com banco de dados MYSQL
        banco = mysql.connector.connect(host="localhost", user="root", password="", database="outro")
        cursor = banco.cursor()


        n = nome.get()
        m = modelo.get()
        p = placa.get()

        if n == "":
            tk.messagebox.showinfo(title="Alerta", message="Campo do nome está vazio! Formule-o novamente.")
            case.destroy()
            return adicionarCarro()

        if m == "":
            tk.messagebox.showinfo(title="Alerta", message="Campo do modelo está vazio! Formule-o novamente.")
            case.destroy()
            return adicionarCarro()

        if p == "":
            tk.messagebox.showinfo(title="Alerta", message="Campo da placa está vazio! Formule-o novamente.")
            case.destroy()
            return adicionarCarro()

        data = strftime('%d/%m/%Y')
        hora = strftime('%H:%M')




        c1 = "INSERT INTO estacionamento(nome,data,hora,modelo,placa,id) VALUES ('" + n + "','" + data + "','" + hora + "','" + m + "','" + p + "','" + b + "')"

        cursor.execute(c1)


        try:
            banco.commit()
            tk.messagebox.showinfo(title="Alerta", message="Sucesso! ")
            case.destroy()
            atualizar()
        except:
            tk.messagebox.showinfo(title="Alerta", message="Erro!")
            case.destroy()
            return adicionarCarro()



    case = tk.Toplevel()
    case.resizable(width=False, height=False)
    case.geometry('800x500')
    center(case)

    label = Image.open("add.jpg")
    photo = ImageTk.PhotoImage(label)

    Label(case, image=photo).place(x=-2, y=-2)


    nome = Entry(case, borderwidth=0, background='#ffffff', foreground='#151515', font='Poppins 14 normal')
    nome.place(x=365, y=118, width=365, height=37)

    modelo = Entry(case, borderwidth=0, background='#ffffff', foreground='#151515', font='Poppins 14 normal')
    modelo.place(x=313, y=221, width=325, height=37)

    placa = Entry(case, borderwidth=0, background='#ffffff', foreground='#151515', font='Poppins 14 normal')
    placa.place(x=200, y=331, width=352, height=37)

    enviar = Button(case, text='→', borderwidth=0, background='#003e62', foreground='white', font='Poppins 30 bold', command=enviar)
    enviar.place(x=27, y=410, height=70)

    case.mainloop()

# ---------------------------------------------------------------

def selecionado():

    try:

        # Realizando conexão com banco de dados MYSQL
        banco = mysql.connector.connect(host="localhost", user="root", password="", database="outro")
        cursor = banco.cursor()

        x = str(m.item(m.focus())['values'][5])

        cursor.execute("DELETE FROM estacionamento WHERE id = " + x + "")
        banco.commit()

        tk.messagebox.showinfo(title="Alerta", message="Sucesso!")

        atualizar()

    except:

        tk.messagebox.showinfo(title="Alerta", message="Erro! Selecione alguma linha.")




#-----------------------------------------------------------------------------------------------------------------------











#-----------------------------------------------------------------------------------------------------------------------

# Objeto principal

root = Tk()

root.title('Estacionamento')
root.geometry('1100x700')
root.configure(background='#999999')
root.resizable(width=False, height=False)
center(root)













#-----------------------------------------------------------------------------------------------------------------------

#Tabela com os carros


m = ttk.Treeview(root, columns=('Nome', 'Data', 'Hora', 'Modelo', 'Placa'), show='headings')

style = ttk.Style()
style.configure("Treeview", font='Poppins 15', rowheight=35)
style.configure("Treeview.Heading", font='Poppins 15')

m.column('Nome', minwidth=0, width=350)
m.column('Data', minwidth=0, width=160)
m.column('Hora', minwidth=0, width=100)
m.column('Modelo', minwidth=0, width=250)
m.column('Placa', minwidth=0, width=190)
m.heading('Nome', text='Nome')
m.heading('Data', text='Data')
m.heading('Hora', text='Hora')
m.heading('Modelo', text='Modelo')
m.heading('Placa', text='Placa')
m.place(x=24, y=215, height=460)


cursor = banco.cursor()

cursor.execute("SELECT * FROM estacionamento ORDER BY id")
recordes1 = cursor.fetchall()

global count
count = 0

for record3 in recordes1:
    m.insert(parent='', index='end', iid=count, text='', values=(( "  " + record3[0]), ( "     " + record3[1]), ( "     " + record3[2]), record3[3], record3[4], ( "     " + str(record3[5]))))

    count += 1

banco.commit()
banco.close()

#-----------------------------------------------------------------------------------------------------------------------







Label(root, text='', bg='#707070', fg='white', font='Poppins 20 bold', borderwidth=0).place(x=25, y=20, width=380, height=180)
Label(root, text='', bg='#707070', fg='white', font='Poppins 20 bold', borderwidth=0).place(x=420, y=20, width=655, height=180)
Label(root, text='01 Carro(s) No Total.', bg='#303030', fg='white', font='Poppins 20 bold', borderwidth=0).place(x=440, y=40, width=382, height=65)

hora = Label(root, text='', bg='#303030', fg='white', font='Gothic 30 normal', borderwidth=0)
hora.place(x=835, y=40, width=220, height=140)
time()

data = Label(root, text='', bg='#303030', fg='white', font='Gothic 20 bold', borderwidth=0)
data.place(x=440, y=115, width=382, height=64)
date()



# Botões com funções

btnAdicionar = Button(root, text='Adicionar Carro', bg='#202020', fg='white', font='Poppins 20 bold', borderwidth=0, command=adicionarCarro).place(x=40, y=35, width=350, height=70)

btnRemover = Button(root, text='Remover', bg='#303030', fg='white', font='Poppins 18 normal', borderwidth=0, command=selecionado).place(x=40, y=115, width=170, height=70)

btnRemoverTodos = Button(root, text='Atualizar', bg='#303030', fg='white', font='Poppins 18 normal', borderwidth=0, command=atualizar).place(x=220, y=115, width=170, height=70)



root.mainloop()

# ----------------------------------------------------------------------------------------------------------------------



