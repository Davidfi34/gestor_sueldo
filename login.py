from tkinter import * 
import customtkinter
from admin.db import *
from alert import mens
from pantalla import App


customtkinter.set_appearance_mode("Ligth")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

login = customtkinter.CTk()
login.geometry("600x500")
login.title("Login")
login.iconbitmap("image/icono.ico")
login.resizable(0,0)
Consulta()


#=========VERIFICA ADMINISTRADOR==========#
#==USURIO = "admin" Y CONTRASENA = 1234 ==#
def Verificar():
        if LoginDB(entry_us.get(),entry_pass.get()):
            login.destroy()
            inicio = App()
            inicio.mainloop()     
        else:
          mens(1,"Usuario incorrecto")



frame_1 = customtkinter.CTkFrame(master=login)
frame_1.pack(pady=60, padx=60,fill="both", expand=True)

label_1 = customtkinter.CTkLabel(text='Gestor',master=frame_1, justify=LEFT)
label_1.config(font=("Helvatical bold", 20))
label_1.pack(pady=40, padx=40)


entry_us = customtkinter.CTkEntry(master=frame_1,  placeholder_text="Usuario",width=200)
entry_us.pack(padx=20, pady=10)

entry_pass = customtkinter.CTkEntry(master=frame_1, placeholder_text="Contraseña",show="*",width=200)
entry_pass.pack(padx=30, pady=10)

button_1 = customtkinter.CTkButton(master=frame_1,text="Ingresar",width=200,command=Verificar)
button_1.pack(padx=20, pady=20)


login.mainloop()