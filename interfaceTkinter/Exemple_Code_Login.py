from tkinter import *
from tkinter import messagebox
import mysql.connector
import pymysql

background="#06283D"
Framebg="EDEDED"
FrameFG="06283D"

trial_no=0
def trial():
    global trial_no
    trial_no+=1
    if trial_no == 3:
        messagebox.showwarning("Warninge","You Have tried more then limit !! ")
        root.destroy()#programe Close

def LoginUser():
    username=user.get()
    password=code.get()
    
    if (username == "" or username =="Admin_ID") or (password =="" or password == "Password"):
        messagebox.showerror("Entry Error" , "Type username or password!!")
    else :
        try:
            MyDb = pymysql.connect(
                    host='localhost',
                    user = 'root',
                    password='',
                    database='data_voiture'
                )
            MyCursor = MyDb.cursor()
            print("Connected To DataBase")
        except:
            messagebox.showerror('Connection Failed',"DataBase connection not Stablish !!")
            return
        
        command = "use devlopeureregistration"
        MyCursor.execute(command)
        command = "Select * From Login Where Username=%s and Password = %s"
        MyCursor.execute(command,(username,password))
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


root=Tk()
root.title("Login System")
root.geometry("500x550+2+1")
root.config(bg=background)
root.resizable(False,False)
#\LOGIN.png
# Icon Image
Image_Icon=PhotoImage(file="Desktop\gestion-des-voitures\Aymen\Image\Login2.png")
root.iconphoto(False,Image_Icon)
#Background Image
Fram=Frame(root,bg="red")
Fram.pack(fill=Y)
backgroundImage = PhotoImage(file="Desktop\gestion-des-voitures\Aymen\Image\Login.png") 
Label(Fram,image=backgroundImage).pack()

########user entry
def user_enter(e):
    user.delete(0,'end')
def user_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Admin_ID')

user=Entry (Fram, width=16, fg="#737373", border=0, bg="#F1EFFD", font=('Arial Bold', 20))
user.insert(1,'Admin_ID')
user.bind("<FocusIn>", user_enter)
user.bind("<FocusOut>", user_leave)
user.place(x=150, y=200)

########Password entry
def code_enter(e):
    code.delete(0,'end')
def code_leave(e):
    if code.get()=='':
        code.insert(0,'Password')

code=Entry (Fram, width=14, fg="#737373", border=0, bg="#F1EFFD", font=('Arial Bold', 20))
code.insert(1,'Password')
code.bind("<FocusIn>", code_enter)
code.bind("<FocusOut>", code_leave)
code.place(x=150, y=276)


# hide and show button
button_mode=True
def hide():
    global button_mode
    if button_mode:
        eyeButton.config(image=closeeye,activebackground="White") 
        code.config(show="*")
        button_mode=False
    else : 
        eyeButton.config(image=openeye,activebackground="White")
        code.config(show="")
        button_mode=True
openeye=PhotoImage(file="Desktop\gestion-des-voitures\Aymen\Image\yeuxOvert.png")
closeeye=PhotoImage(file="Desktop\gestion-des-voitures\Aymen\Image\closeye.png")
eyeButton=Button(Fram,image=openeye,bg="#F1EFFD",bd=0,command=hide)
eyeButton.place(x=360,y=275) 

########login Botton
LoginButton=Button(root,text="LOGIN",bg="#EB5A00",width=7,height=0,font=("arial",16,"bold"),bd=0,command=LoginUser)
LoginButton.place(x=200,y=350)

Label1=Label(root,text="Don't have an account ?",fg="black",bg="#F1EFFD",font=('Microsoft Hahemi UI Light',9))
Label1.place(x=500,y=510)
registerButton=Button(root,width=10,text="Add New User",border=0,bg="#F1EFFD",cursor='hand2',fg="#5A2F2D")
registerButton.place(x=640,y=510)


root.mainloop()
