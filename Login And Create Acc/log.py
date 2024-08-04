

import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import messagebox
import mysql.connector

background = "#06283D"
framebg = "#EDEDED"
framefg = "#06283D"

trial_no=0
def trial():
    global trial_no
    trial_no+=1
    if trial_no == 3:
        messagebox.showwarning("Warninge","You Have tried more then limit !! ")
        root.destroy()#programe Close

def login():
    username = user.get()
    password = code.get()

    if (username == "" or username =="Username") or (password =="" or password == "password"):
        messagebox.showerror("Entry Error", "Invalide UserName or password")
    else:
        try:
            MyDb = mysql.connector.connect(host='localhost', user='root', password='', database='data_voiture')
            MyCursor = MyDb.cursor()
            print("Connected To DataBase")
        except:
            messagebox.showerror('Connection Failed', "DataBase connection not Stablish !!")
            return
        command = "use data_voiture"
        MyCursor.execute(command)
        command = "Select * From login_employes Where UserName=%s and Password = %s"
        MyCursor.execute(command, (username, password))
        Myresult = MyCursor.fetchone()
        print(Myresult)

        if Myresult == None:
            messagebox.showinfo("Invalid","Invalid User_ID And Password")
            # LE NOMBRE DE TRIER
            trial()

        else : 
            messagebox.showinfo("Login","Sucessfully Login !!!")

            root.destroy()
            import GestiondeVoitur

root = Tk()
root.title("welcom")
root.geometry("500x550+400+50")
root.config(bg=background)
root.resizable(False, False)

frame = Frame(root, bg="white")
frame.pack(fill=BOTH, expand=True)

frame = Frame(root, bg="white")
frame.pack(fill=BOTH, expand=True)
Image_Icon=PhotoImage(file=r"Desktop\gestion-des-voitures\Login And Create Acc\image\Login2.png")
root.iconphoto(False,Image_Icon)

frame=Frame(root,bg="black")
frame.pack(fill=Y)
backgroundImage = PhotoImage(file=r"Desktop\gestion-des-voitures\Login And Create Acc\image\Frame_1.png") 
Label(frame, image=backgroundImage).pack()

user = Entry(frame, width=13, fg="black", border=0, bg="#d9d9d9", font=("arial bold", 20))
user.insert(0, 'Username')
user.bind("<FocusIn>", lambda e: user.delete(0, "end"))
user.bind("<FocusOut>", lambda e: user.insert(0, ''))
user.place(x=150, y=153)

code = Entry(frame, width=13, fg="black", border=0, bg="#d9d9d9", font=("arial bold", 20))
code.insert(0, 'password')
code.bind("<FocusIn>", lambda e: code.delete(0, "end"))
code.bind("<FocusOut>", lambda e: code.insert(0, ''))
code.place(x=150, y=256)

openeye = PhotoImage(file=r"Desktop\gestion-des-voitures\Login And Create Acc\image\open_aye.png")
closeeye = PhotoImage(file=r"Desktop\gestion-des-voitures\Login And Create Acc\image\closed_aye.png")
button_mode = True
def hide():
    global button_mode
    if button_mode:
        eyeButton.config(image=closeeye, activebackground="#d9d9d9") 
        code.config(show="*")
        button_mode = False
    else:
        eyeButton.config(image=openeye, activebackground="#d9d9d9")
        code.config(show="")
        button_mode = True

eyeButton = Button(frame, image=openeye, bg="#d9d9d9", bd=0, command=hide)
eyeButton.place(x=345, y=256) 

button_bg_image = PhotoImage(file=r"Desktop\gestion-des-voitures\Login And Create Acc\image\Frame_4.png")
loginbutton = Button(root, text="",bg="#FFFFFF", width=150, height=70, bd=0, command=login)
loginbutton.config(image=button_bg_image, compound="center")
loginbutton.place(x=170, y=350)
loginbutton.image = button_bg_image

def register():
    print("Register button clicked")

registerButton = Button(root, text="Sign Up", width=16, border=0, bg="#FFFFFF", cursor="hand2", fg="purple", command=register)
registerButton.place(relx=0.5, rely=0.93, anchor=CENTER)

root.mainloop()


















































