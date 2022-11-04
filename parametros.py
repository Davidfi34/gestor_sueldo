"""
from doctest import master
from struct import pack
import tkinter as tk
from tkinter import ttk
from turtle import bgcolor, width
from mysqlx import Column
from prettytable import PrettyTable
import tkinter
import tkinter.messagebox
import customtkinter


class Parametros(customtkinter.CTk):
    WIDTH = 100
    HEIGHT = 400

    def __init__(self,master,descrip):
        customtkinter.CTkFrame.__init__(self,master,descrip)
        self.master = master
        self.descrip = descrip
    


        self.tabla = customtkinter.CTkFrame(master=self.opciones,height=100,width=400)
        self.tabla.grid(row=0, column=0,sticky="n",padx=20, pady=20)
        #self.tabla.pack(fill="x",expand=False)

        self.descrip = customtkinter.CTkLabel(master=self.tabla,
                                              text=self.descrip,
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.descrip.grid(row=0, column=0, pady=10, padx=0, sticky="n")

        self.descrip = customtkinter.CTkLabel(master=self.tabla,
                                              text="3%",
                                              text_font=("Roboto Medium", -14))  # font name and size in px
        self.descrip.grid(row=0, column=1, pady=10, padx=0, sticky="n")
        
        self.edit = customtkinter.CTkButton(master=self.tabla,
                                                text="Editar",
                                                width=50,
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event)
        self.edit.grid(row=0, column=4, columnspan=1, pady=10, padx=30, sticky="e")




"""