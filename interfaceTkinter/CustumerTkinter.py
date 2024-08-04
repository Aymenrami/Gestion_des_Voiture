from tkinter import *
from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("500x400")

set_appearance_mode("dark")
img = Image.open(r"Desktop\gestion-des-voitures\Nizar_Fathi\image\Login2.png")
btn = CTkButton(master =app , text = "Brek Hna",corner_radius=10 ,fg_color="#000000",hover_color="#C850C0",border_color="#FFCC70",
                border_width=2,image=CTkImage(dark_image=img, light_image=img))

btn.place(relx=0.5, rely=0.5, anchor="center")


# # label = CTkLabel(master=app , text="CHI Hajja....", font=("Arial",20),text_color="#FFCC70")
# # label.place(relx=0.5,rely=0.7,anchor="center")

# # combobox = CTkComboBox(master=app, values=["option 1", "option 2", "option 3"], fg_color="#0093E9",
# # border_color="#FBAB7E", dropdown_fg_color="#0093E9")
# # combobox.place(relx=0.5, rely=0.2, anchor="center")


# # entry = CTkEntry (master=app, placeholder_text="Start typing...", width=300,
# # text_color="#FFCC70")
# # entry.place(relx=0.5, rely=0.3, anchor="center")
# def  information():
#         ID_Voiture_entry = CTkEntry(master=app,placeholder_text="ID Voiture", width=120, fg_color='#8A4C16')
#         ID_Voiture_entry.pack()

# set_default_color_theme("MoonlitSky.json")

# # Créer un onglet
# tabview = CTkTabview(master=app)
# tabview.pack(padx=20, pady=20)

# # Créer un champ de saisie dans l'onglet avec place
# Annee_Modele_entry = CTkEntry(tabview, placeholder_text="Année Modèle", width=120, fg_color='#8A4C16')
# Annee_Modele_entry.place(x=30, y=30) 
# # tabview.add("Tab 1")
# # tabview.add("Tab 2")
# # tabview.add("Tab 3")
# # label_1 = CTkLabel(master=tabview.tab("Tab 1"))
# # label_1.pack(padx=20, pady=20)
# # label_2 = CTkLabel(master=tabview.tab("Tab 2"), text="This is tab 2")
# # label_2.pack(padx=20, pady=20)
# # label_3 =CTkLabel(master=tabview.tab("Tab 3"), text="This is tab 3")
# # label_3.pack(padx=20, pady=20)



app.mainloop()
# customtkinter.set_appearance_mode("dark") # Modes: system (default
# customtkinter.set_default_color_theme("dark-blue") # Themes:
# #root = Tk()
# root = customtkinter.CTk()
# root.title('Tkinter.com - CustomTkinter Widget Animations')

# root.geometry( '700x450')
# root.mainloop()