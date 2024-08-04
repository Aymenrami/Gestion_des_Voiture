from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
#test
class voiture:
    def __init__(self,root):
        self.root = root 
        self.root.geometry('1280x690+1+1')
        self.root.title('Projet De Gestion Des Voiture')
        self.root.configure(background = "#34495E")
        self.root.resizable(False,True)
        titre = Label(self.root, 
        text = '[Système De Enregistrement Des voitures]',
        bg = '#2E4053',
        font = ('monospace',14),
        fg = 'white'         
        )
        titre.pack(fill=X)

    #---------- mysqlworkbanch -------------
        

    # --------------- les variable ----------------------------------
        
        self.ID_Voiture = StringVar()  
        self.Lien = StringVar()
        self.Ville = StringVar()
        self.Marque = StringVar()
        self.Modele = StringVar() 
        self.Annee_Modele = StringVar()
        self.Kilometrage = StringVar () 
        self.TypeDeCarburant = StringVar()  
        self.Puissance_Fiscale = StringVar() 
        self.Boite_Vitesse = StringVar()
        self.PrixVoiture = StringVar()  
        self.dell = StringVar()
        self.sea_rch = StringVar()
        self.se_by = StringVar()
        self.sea_var = StringVar()

    #---------------- Les Outils de conrole de programe ----------------- #
        Manage_Frame = Frame(self.root , bg = '#566573')
        Manage_Frame.place(x=1050,y=40,width=210,height=590)

        ID_Voiture = Label(Manage_Frame,text='ID_Voiture',bg='#566573')
        ID_Voiture.pack()
        ID_Voiture_Entry = Entry(Manage_Frame ,textvariable=self.ID_Voiture, bd='5',justify='center',bg='#566573')
        ID_Voiture_Entry.pack()

        label_Lien = Label(Manage_Frame, text="Lien",bg='#566573')
        label_Lien.pack()
        entry_Lien = Entry(Manage_Frame,textvariable=self.Lien,bd='5',justify='center',bg='#566573')
        entry_Lien.pack()

        label_Ville = Label(Manage_Frame, text="Ville",bg='#566573')
        label_Ville.pack()
        entry_Ville = Entry(Manage_Frame,textvariable=self.Ville, bd='5',justify='center' ,bg='#566573')
        entry_Ville.pack()

        label_Marque = Label(Manage_Frame, text="Marque",bg='#566573')
        label_Marque.pack()
        entry_Marque = Entry(Manage_Frame,textvariable=self.Marque, bd='5',justify='center',bg='#566573')
        entry_Marque.pack()

        label_Modele = Label(Manage_Frame, text="Modele",bg='#566573')
        label_Modele.pack()
        entry_Modele = Entry(Manage_Frame,textvariable=self.Modele, bd='5',justify='center',bg='#566573')
        entry_Modele.pack()

        label_Annee_Modele = Label(Manage_Frame, text="Annee_Modele", bg='#566573')
        label_Annee_Modele.pack()
        entry_Annee_Modele= Entry(Manage_Frame,textvariable=self.Annee_Modele, bd='5',justify='center',bg='#566573')
        entry_Annee_Modele.pack()
    
        label_Kilometrage = Label(Manage_Frame, text="Kilometrage",bg='#566573')
        label_Kilometrage.pack()
        entry_Kilometrage = Entry(Manage_Frame,textvariable=self.Kilometrage, bd='5',justify='center',bg='#566573')
        entry_Kilometrage.pack()

        label_TypeDeCarburant = Label(Manage_Frame, text="TypeDeCarburant",bg='#566573')
        label_TypeDeCarburant.pack()
        combo_type = ttk.Combobox(Manage_Frame,textvariable=self.TypeDeCarburant, values=('Diesel', 'Essence', 'Hybride'), background ='#566573')
        combo_type.pack()

       

        label_Puissance_Fiscale = Label(Manage_Frame, text="Puissance_Fiscale", bg='#566573')
        label_Puissance_Fiscale.pack()
        entry_PuissanceFiscal = Entry(Manage_Frame,textvariable=self.Puissance_Fiscale, bd='5',justify='center',bg='#566573')
        entry_PuissanceFiscal.pack()
       
        
        label_Boite_Vitesse = Label(Manage_Frame, text="Boite_Vitesse", bg='#566573')
        label_Boite_Vitesse.pack()
        entry_Boite_Vitesse = Entry(Manage_Frame,textvariable=self.Boite_Vitesse, bd='5',justify='center' ,bg='#566573')
        entry_Boite_Vitesse.pack()

        label_PrixVoiture = Label(Manage_Frame, text="PrixVoiture", bg='#566573' )
        label_PrixVoiture.pack()
        entry_PrixVoiture = Entry(Manage_Frame,textvariable=self.PrixVoiture,bd='5',justify='center' , bg='#566573')
        entry_PrixVoiture.pack()

        lbl_delete = Label(Manage_Frame,fg ='#D98880', text="Supression de voiture", bg='#566573')
        lbl_delete.pack()
        lbl_delete = Entry(Manage_Frame,textvariable=self.dell, bd='5',justify='center' , bg='#566573')
        lbl_delete.pack()

        #---------------- Les Buttons  ----------------- #
        colour1 = '#020f12',
        colour2 = '#05d7ff',
        colour3 = '#65e7ff',
        colour4 = 'BLACK'

        btn_Frame = Frame(self.root,bg='#566573')
        btn_Frame.place(x=13,y=40,width=210,height=590)
        titre = Label(btn_Frame,text='Panneau de contrôle',font = ('Deco',14),fg='#D98880',bg='#566573')
        titre.pack(fill= X)



        ADD_btn = Button(btn_Frame,background=colour1,foreground=colour2,activebackground=colour3,activeforeground=colour4,highlightthickness=2,highlightbackground=colour2,highlightcolor='WHITE',width=13,height=2,border=0,cursor= 'hand1',text='Ajoter les donne',font=('Arial', 16, 'bold'),command=self.add_voiture)
        #ADD_btn.grid(column=0,row =0)
        ADD_btn.place(x=33,y=33,width=150,height=30)
        DEL_btn = Button(btn_Frame, text='Effacer les données',bg='#566573',command=self.delvoiture)
        DEL_btn.place(x=33,y=63,width=150,height=30)
        UPDATE_btn = Button(btn_Frame, text='Mise a Jour',bg='#5D6D7E',command=self.update)
        UPDATE_btn.place(x=33,y=93,width=150,height=30)
        CLEAR_btn = Button(btn_Frame, text='Vider le champ',bg='#566573',command=self.Clear)
        CLEAR_btn.place(x=33,y= 123,width=150,height=30)
        ABOUT_btn = Button(btn_Frame, text='Qui Sommes-nous',bg='#5D6D7E',command=self.AbouteUs)
        ABOUT_btn.place(x=33,y=153,width=150,height=30)
        EXITE_btn = Button(btn_Frame, text='Fermer le programme',bg='#566573',command=root.quit)
        EXITE_btn.place(x=33,y=183,width=150,height=30)

        # -----------------search manage ----------------------------

        search_frame = Frame(self.root , bg ='#566573')
        search_frame.place(x=230,y=40,width=813,height=50)

        Lbl_search = Label(search_frame,text='Chercher Pour Une Voiture',bg='#566573')
        Lbl_search.place(x=1,y=12)

        combo_search = ttk.Combobox(search_frame,textvariable=self.sea_var,justify='left')
        combo_search['value']=('ID_Voiture','Annee_Modele','Puissance_Fiscale','PrixVoiture','TypeDeCarburant','Ville')
        combo_search.place(x=150,y=12)

        search_Entry = Entry(search_frame ,textvariable=self.se_by, justify='left' , bd='5' ,bg='#566573',fg='white' )
        search_Entry.place(x=300,y=12)

        se_btn = Button(search_frame , text='Search' , bg='#566573',fg='Black',command=self.Searche)
        se_btn.place(x=700,y=12,width=100,height=25)
        
        #-------------------- detaille --------------------------

        Detaile_Frame = Frame(self.root , bg='#85929E')
        Detaile_Frame.place(x=230,y=100,width=813,height=530)
            # _____Scrool_____
        scrol_x = Scrollbar(Detaile_Frame,orient=HORIZONTAL)
        scrol_y = Scrollbar(Detaile_Frame,orient=VERTICAL)
            #______treeview_____
        self.Voiture_Table = ttk.Treeview(Detaile_Frame,
        columns=('ID_Voiture','Lien','Ville','Marque','Modele','Annee_Modele','Kilometrage','TypeDeCarburant','Puissance_Fiscale','Boite_Vitesse','PrixVoiture','Supression de Voiture'),
        xscrollcommand=scrol_x.set,
        yscrollcommand=scrol_y.set)
        self.Voiture_Table.place(x=18,y=1,width=1000,height=510)
        scrol_x.pack(side=BOTTOM,fill=X)
        scrol_y.pack(side=LEFT,fill=Y)
        scrol_x.config(command=self.Voiture_Table.xview)
        scrol_y.config(command=self.Voiture_Table.yview)

        self.Voiture_Table['show']='headings'
        self.Voiture_Table.heading('ID_Voiture',text='ID_Voiture')
        self.Voiture_Table.heading('Lien',text='Lien')
        self.Voiture_Table.heading('Ville',text='Ville')
        self.Voiture_Table.heading('Marque',text='Marque')
        self.Voiture_Table.heading('Modele',text='Modele')
        self.Voiture_Table.heading('Annee_Modele',text='Annee_Modele')
        self.Voiture_Table.heading('Kilometrage',text='Kilometrage')
        self.Voiture_Table.heading('TypeDeCarburant',text='TypeDeCarburant')
        self.Voiture_Table.heading('Puissance_Fiscale',text='Puissance_Fiscale')
        self.Voiture_Table.heading('Boite_Vitesse',text='Boite_Vitesse')
        self.Voiture_Table.heading('PrixVoiture',text='PrixVoiture')
        self.Voiture_Table.column('ID_Voiture',width=100)
        self.Voiture_Table.column('Lien',width=100)
        self.Voiture_Table.column('Ville',width=100)
        self.Voiture_Table.column('Marque',width=100)
        self.Voiture_Table.column('Modele',width=100)
        self.Voiture_Table.column('Annee_Modele',width=100)
        self.Voiture_Table.column('Kilometrage',width=100)
        self.Voiture_Table.column('TypeDeCarburant',width=100)
        self.Voiture_Table.column('Puissance_Fiscale',width=100)
        self.Voiture_Table.column('Boite_Vitesse',width=100)
        self.Voiture_Table.column('PrixVoiture',width=100)
        self.Voiture_Table.bind("<ButtonRelease-1>",self.Get_Curssor)
       
        #---------------- con Add ----------------
        self.fetch_all()
    def add_voiture(self):
        con = pymysql.connect(
                host='localhost',
                user = 'root',
                password='',
                database='data_voiture'
            )
        cur = con.cursor()
        cur.execute("insert into voitures values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
        self.ID_Voiture.get(),self.Lien.get(),self.Ville.get(),self.Marque.get(),
        self.Modele.get(),self.Annee_Modele.get(),self.Kilometrage.get(),
        self.TypeDeCarburant.get(),self.Puissance_Fiscale.get(),self.Boite_Vitesse.get(),self.PrixVoiture.get(),))
        con.commit()
        self.fetch_all()
        self.Clear()
        con.close()

        #------------- SHOW DATA -----------------
        
    def fetch_all(self):     
            con = pymysql.connect(host='localhost',user = 'root',password='',database='data_voiture')
            cur = con.cursor()
            cur.execute('select * from voitures')
            rows = cur.fetchall()
            if len (rows) != 0:
                    self.Voiture_Table.delete(* self.Voiture_Table.get_children())
                    for row in rows :
                            self.Voiture_Table.insert("",END,value=row)
                    con.commit()
            con.close() 
    
    # ---------- DELLE ----------
    
    def delvoiture(self):
            con = pymysql.connect(host='localhost',user = 'root',password='',database='data_voiture')
            cur = con.cursor()
            cur.execute('delete from voitures where ID_Voiture =%s',self.dell.get())
            con.commit()
            self.fetch_all()
            con.close()


    #----------------Clear-----------------
    def Clear(self):
            self.ID_Voiture.set(''),
            self.Lien.set(''),
            self.Ville.set(''),
            self.Marque.set(''),
            self.Modele.set(''),
            self.Annee_Modele.set(''),
            self.Kilometrage.set(''),
            self.TypeDeCarburant.set(''),
            self.Puissance_Fiscale.set(''),
            self.Boite_Vitesse.set(''),
            self.PrixVoiture.set('')      

# ------------- recuperer les doone ---------------
    def Get_Curssor(self,ev):
           curssor_row = self.Voiture_Table.focus()
           contents = self.Voiture_Table.item(curssor_row)
           row=contents['values']
           self.ID_Voiture.set(row[0]),
           self.Lien.set(row[1]),
           self.Ville.set(row[2]),
           self.Marque.set(row[3]),
           self.Modele.set(row[4]),
           self.Annee_Modele.set(row[5]),
           self.Kilometrage.set(row[6]),
           self.TypeDeCarburant.set(row[7]),
           self.Puissance_Fiscale.set(row[8]),
           self.Boite_Vitesse.set(row[9]),
           self.PrixVoiture.set(row[10])
           

        # ----------------La mise a joure --------------------
    def update(self):
                   
        con = pymysql.connect(
                host='localhost',
                user = 'root',
                password='',
                database='data_voiture'
            )
        cur = con.cursor()
        cur.execute("UPDATE voitures SET Lien=%s, Ville=%s, Marque=%s, Modele=%s, Annee_Modele=%s, Kilometrage=%s, TypeDeCarburant=%s, Puissance_Fiscale=%s, Boite_Vitesse=%s, PrixVoiture=%s WHERE ID_Voiture=%s",
       (self.Lien.get(),self.Ville.get(),self.Marque.get(),
        self.Modele.get(),self.Annee_Modele.get(),self.Kilometrage.get(),
        self.TypeDeCarburant.get(),self.Puissance_Fiscale.get(),self.Boite_Vitesse.get(),self.PrixVoiture.get(),self.ID_Voiture.get()))
        con.commit()
        self.fetch_all()
        con.close()

#----------------Search -----------------------    
    def Searche(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='data_voiture')
        cur = con.cursor()

        query = "SELECT * FROM voitures WHERE {} = %s".format(self.sea_var.get())

        cur.execute(query, (str(self.se_by.get())))

        rows = cur.fetchall()

        if len(rows) != 0:
            self.Voiture_Table.delete(*self.Voiture_Table.get_children())
            for row in rows:
                self.Voiture_Table.insert("", END, value=row)
            con.commit()
        con.close()

# ----------------About Us-------------------

    def AbouteUs(self):
          messagebox.showinfo("Stagaire Reda Amraoui "," Bienvenue Sur Mon Premier projet")
          
root = Tk()
ob = voiture(root)
root.mainloop()