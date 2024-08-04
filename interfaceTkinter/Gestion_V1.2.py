from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
from customtkinter import *
from PIL import Image
from customtkinter import CTkEntry
import customtkinter

#test
class voiture:
    def __init__(self,root):
        self.root = root 
        self.root.geometry('1260x650+1+1')
        self.root.title('GDV-Programme')
        set_appearance_mode("dark")
        self.root.resizable(False,True)
        titre = Label(self.root, 
        text = '[Système Des Gestion de Voiture]',
        bg = '#302221',
        font = ('monospace',14),
        fg = '#D5BDB9'         
        )
        titre.pack(fill=X)

        self.ID_Voiture = StringVar()
        self.Ville = StringVar()
        self.Secteur = StringVar()
        self.Marque = StringVar()
        self.Modele = StringVar() 
        self.Annee_Modele = StringVar()
        self.Kilometrage = StringVar()
        self.TypeDeCarburant = StringVar()  
        self.Puissance_Fiscale = StringVar() 
        self.Boite_Vitesse = StringVar()
        self.Nombre_Portes = StringVar()
        self.Origine = StringVar()
        self.Premiere_Main = StringVar()
        self.Etat = StringVar()
        self.Jantes_Aluminium = StringVar()
        self.Airbags = StringVar()
        self.Climatisation = StringVar()
        self.Navigation_GPS = StringVar()
        self.Toit_Ouvrant = StringVar()
        self.Sieges_Cuir = StringVar()
        self.Radar_Recul = StringVar()
        self.Camera_Recul = StringVar()
        self.Vitres_Electriques = StringVar()
        self.ABS = StringVar()
        self.ESP = StringVar()
        self.Regulateur_Vitesse = StringVar()
        self.Limiteur_Vitesse = StringVar()
        self.CD_MP3_Bluetooth = StringVar()
        self.Ordinateur_Bord = StringVar()
        self.Verrouillage_Centralise = StringVar()
        self.Prix = StringVar()
        self.dell = StringVar()
        self.sea_rch = StringVar()
        self.se_by = StringVar()
        self.sea_var = StringVar()

    #-------------- les outile de controle de programme ---------
        Manage_Frame = customtkinter.CTkFrame(self.root, width=100, height=150,fg_color='#302221')
        Manage_Frame.place(x=1080, y=50)
        # Manage_Frame = Frame(self.root , bg = '#302221')
        # Manage_Frame.place(x=1630,y=40,width=240,height=900)
        # ID_Voiture = Label(Manage_Frame,text='ID_Voiture',bg='#566573')
        # ID_Voiture.pack()
        label = CTkLabel(Manage_Frame , text="    Ajouter les information    ", font=("Arial",14),text_color="#D5BDB9")
        label.pack()

        ID_Voiture_entry = CTkEntry(Manage_Frame, placeholder_text="ID Voiture", width=120, fg_color='#8A4C16')
        ID_Voiture_entry.place(y=35)
        ID_Voiture_entry.pack()

        Ville_entry = CTkEntry(Manage_Frame, placeholder_text="Ville", width=120, fg_color='#8A4C16')
        Ville_entry.pack()

        Marque_entry = CTkEntry(Manage_Frame, placeholder_text="Marque", width=120, fg_color='#8A4C16')
        Marque_entry.pack()

        Modele_entry = CTkEntry(Manage_Frame, placeholder_text="Modèle", width=120, fg_color='#8A4C16')
        Modele_entry.pack()

        Annee_Modele_entry = CTkEntry(Manage_Frame, placeholder_text="Année Modèle", width=120, fg_color='#8A4C16')
        Annee_Modele_entry.pack()

        Kilometrage_entry = CTkEntry(Manage_Frame, placeholder_text="Kilométrage", width=120, fg_color='#8A4C16')
        Kilometrage_entry.pack()

        Type_de_carburant_entry = CTkEntry(Manage_Frame, placeholder_text="Type de Carburant", width=120, fg_color='#8A4C16')
        Type_de_carburant_entry.pack()

        Puissance_fiscale_entry = CTkEntry(Manage_Frame, placeholder_text="Puissance Fiscale", width=120, fg_color='#8A4C16')
        Puissance_fiscale_entry.pack()

        Boite_de_vitesse_entry = CTkEntry(Manage_Frame, placeholder_text="Boîte de Vitesse", width=120, fg_color='#8A4C16')
        Boite_de_vitesse_entry.pack()

        Nombre_de_portes_entry = CTkEntry(Manage_Frame, placeholder_text="Nombre de Portes", width=120, fg_color='#8A4C16')
        Nombre_de_portes_entry.pack()

        Origine_entry = CTkEntry(Manage_Frame, placeholder_text="Origine", width=120, fg_color='#8A4C16')
        Origine_entry.pack()

        Premiere_main_entry = CTkEntry(Manage_Frame, placeholder_text="Première Main", width=120, fg_color='#8A4C16')
        Premiere_main_entry.pack()

        Etat_entry = CTkEntry(Manage_Frame, placeholder_text="État", width=120, fg_color='#8A4C16')
        Etat_entry.pack()

        Jantes_en_aluminium_entry = CTkEntry(Manage_Frame, placeholder_text="Jantes en Aluminium", width=120, fg_color='#8A4C16')
        Jantes_en_aluminium_entry.pack()

        Airbags_entry = CTkEntry(Manage_Frame, placeholder_text="Airbags", width=120, fg_color='#8A4C16')
        Airbags_entry.pack()

        Climatisation_entry = CTkEntry(Manage_Frame, placeholder_text="Climatisation", width=120, fg_color='#8A4C16')
        Climatisation_entry.pack()

        Navigation_GPS_entry = CTkEntry(Manage_Frame, placeholder_text="Navigation GPS", width=120, fg_color='#8A4C16')
        Navigation_GPS_entry.pack()

        Toit_ouvrant_entry = CTkEntry(Manage_Frame, placeholder_text="Toit Ouvrant", width=120, fg_color='#8A4C16')
        Toit_ouvrant_entry.pack()

        Sieges_en_cuir_entry = CTkEntry(Manage_Frame, placeholder_text="Sièges en Cuir", width=120, fg_color='#8A4C16')
        Sieges_en_cuir_entry.pack()

        # Radar_de_recul_entry = CTkEntry(Manage_Frame, placeholder_text="Radar de Recul", width=120, fg_color='#8A4C16')
        # Radar_de_recul_entry.pack()

        label = CTkLabel(Manage_Frame , text="                         ", font=("Arial",14),text_color="#D5BDB9")
        label.pack()
        # Camera_de_recul_entry = CTkEntry(Manage_Frame, placeholder_text="Caméra de Recul", width=120, fg_color='#8A4C16')
        # Camera_de_recul_entry.pack()

        # Vitres_electriques_entry = CTkEntry(Manage_Frame, placeholder_text="Vitres Électriques", width=120, fg_color='#8A4C16')
        # Vitres_electriques_entry.pack()

        # ABS_entry = CTkEntry(Manage_Frame, placeholder_text="ABS", width=120, fg_color='#8A4C16')
        # ABS_entry.pack()

        # ESP_entry = CTkEntry(Manage_Frame, placeholder_text="ESP", width=120, fg_color='#8A4C16')
        # ESP_entry.pack()

        # Regulateur_de_vitesse_entry = CTkEntry(Manage_Frame, placeholder_text="Régulateur de Vitesse", width=120, fg_color='#8A4C16')
        # Regulateur_de_vitesse_entry.pack()

        # Limiteur_de_vitesse_entry = CTkEntry(Manage_Frame, placeholder_text="Limiteur de Vitesse", width=120,fg_color='#8A4C16')
        # Limiteur_de_vitesse_entry.pack()
root = CTk()
ob = voiture(root)
root.mainloop()