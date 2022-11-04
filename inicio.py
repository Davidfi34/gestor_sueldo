
from struct import pack
from textwrap import fill
import tkinter as tk
from tkinter import IntVar, StringVar, ttk
from turtle import bgcolor, left, width
from mysqlx import Column
from prettytable import PrettyTable
import tkinter
import tkinter.messagebox
import customtkinter
#from DatosEmp.dbEmpleados import Consulta


from parametros import Parametros

customtkinter.set_Ultimaearance_mode("Ligth")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class Ultima(customtkinter.CTk):

    WIDTH = 1100
    HEIGHT = 600


    def __init__(self):
        super().__init__()

        self.title("Gestor de sueldo")
        self.geometry(f"{Ultima.WIDTH}x{Ultima.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when Ultima gets closed
        

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=100,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="MENU",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=30, padx=10)


    
        self.button_1 = customtkinter.CTkButton(master=self.frame_left,text="Cerrar sesion",command=self.on_closing,width=200)
        self.button_1.grid(row=9, column=0, columnspan=1, pady=20, padx=20, sticky="we")


        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(5, weight=30)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=2, column=0, columnspan=3, rowspan=6, pady=10, padx=10, sticky="nsew")
        
        
        self.cuadro = ttk.Notebook(self.frame_info)
        self.cuadro.pack(fill="both",expand=True)
        
        self.Inicio = customtkinter.CTkFrame(master=self.cuadro)
        self.Registro = customtkinter.CTkFrame(master=self.cuadro)
        self.categorias = customtkinter.CTkFrame(master =self.cuadro)
        self.parametros = customtkinter.CTkFrame(master=self.cuadro)
        self.cuadro.add(self.Inicio,text='Inicio',padding=10,)
        self.cuadro.add(self.Registro,text='Registro',padding=10)
        self.cuadro.add(self.categorias,text='Catergorias',padding=10)
        self.cuadro.add(self.parametros,text='Parametros',padding=10)
  



        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

#==========================INICIO==================================#
        nombre = StringVar()
        apellido = StringVar()
        dni = StringVar()
        direccion = StringVar()
        localidad = StringVar()
        telefono = IntVar() 

        self.label_4 = customtkinter.CTkLabel(master=self.Inicio,
                                              text="Ingresar Dni del empleado",
                                              text_font=("Roboto Medium", -16)) 
        self.label_4.grid(row=0, column=0, pady=20, padx=10)

        self.entry = customtkinter.CTkEntry(master=self.Inicio,
                                            width=200,
                                            placeholder_text="Ingresar DNI")
        self.entry.grid(row=3, column=0, columnspan=1, pady=20, padx=20, sticky="we")
        self.button_1 = customtkinter.CTkButton(master=self.Inicio,
                                                text="Buscar empleado",
                                                width=100,
                                                border_width=1,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event)
        self.button_1.grid(row=3, column=1, pady=20, padx=20, sticky="we")

        self.label_3 = customtkinter.CTkLabel(master=self.Inicio,
                                              text="Ingresar periodo de fechas",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_3.grid(row=5, column=0, pady=30, padx=10)

        self.fechaI = customtkinter.CTkEntry(master=self.Inicio,
                                            width=200,
                                            placeholder_text="Fecha inicial")
        self.fechaI.grid(row=6, column=0, columnspan=1, pady=10, padx=30, sticky="we")

        self.fechaS = customtkinter.CTkEntry(master=self.Inicio,
                                            width=200,
                                            placeholder_text="Fecha final")
        self.fechaS.grid(row=6, column=1, columnspan=1, pady=10, padx=30, sticky="we")

        
        self.button_2 = customtkinter.CTkButton(master=self.Inicio,
                                                text="Ver",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event)
        self.button_2.grid(row=10, column=2, columnspan=1, pady=30, padx=50, sticky="s")

   


        # ============ frame_registro ============



        self.radio_var = tkinter.IntVar(value=0)

        self.label_2 = customtkinter.CTkLabel(master=self.Registro,
                                              text="Nuevo registro",
                                              text_font=("Roboto Medium", -16,))  # font name and size in px
        self.label_2.grid(row=0, column=0, pady=10, padx=0, sticky="n")

        self.apellido = customtkinter.CTkEntry(master=self.Registro,
                                              width=300,
                                            placeholder_text="Apellido",textvariable=apellido)
        self.apellido.grid(row=3, column=0, columnspan=1, pady=20, padx=30, sticky="n")

        self.nombre = customtkinter.CTkEntry(master=self.Registro,
                                              width=300,
                                            placeholder_text="Nombre",textvariable=nombre)
        self.nombre.grid(row=3, column=1, columnspan=1, pady=20, padx=30, sticky="n")

        self.dni = customtkinter.CTkEntry(master=self.Registro,
                                            width=300,
                                            placeholder_text="DNI",textvariable= dni)
        self.dni.grid(row=4, column=0, columnspan=1, pady=20, padx=30, sticky="n")

        self.fechaN = customtkinter.CTkEntry(master=self.Registro,
                                          width=300,
                                            placeholder_text="Fecha de nacimiento")
        self.fechaN.grid(row=4, column=1, columnspan=1, pady=20, padx=30, sticky="n")

        self.direccion = customtkinter.CTkEntry(master=self.Registro,
                                              width=300,
                                            placeholder_text="Direccion",textvariable=direccion)
        self.direccion.grid(row=5, column=0, columnspan=1, pady=20, padx=30, sticky="n")

        self.telefono = customtkinter.CTkEntry(master=self.Registro,
                                                width=300,
                                            placeholder_text="Telefono",textvariable=telefono)
        self.telefono.grid(row=5, column=1, columnspan=1, pady=20, padx=30, sticky="n")

        self.categoria = customtkinter.CTkComboBox(master=self.Registro,
                                                    values=["categoria 1", "categoria 2","categoria 3"])
        self.categoria.grid(row=6, column=0, columnspan=1, pady=20, padx=30, sticky="s")

        
        self.button_2 = customtkinter.CTkButton(master=self.Registro,
                                                text="Registrar",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event)
        self.button_2.grid(row=8, column=1, columnspan=1, pady=10, padx=30, sticky="e")

        #===================================frame parametros============================================#

   

        



#=====================TABLA 1========================#
        self.tabla1 = customtkinter.CTkFrame(master=self.parametros,height=100,width=400)
        self.tabla1.grid(row=0, column=0,sticky="n",padx=10, pady=10)
        #self.tabla.pack(fill="x",expand=False)

        self.descrip = customtkinter.CTkLabel(master=self.tabla1,
                                              text="Obra social",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.descrip.grid(row=0, column=0, pady=10, padx=0, sticky="n")

        self.descrip = customtkinter.CTkLabel(master=self.tabla1,
                                              text="3%",
                                              text_font=("Roboto Medium", -14))  # font name and size in px
        self.descrip.grid(row=0, column=1, pady=10, padx=0, sticky="n")
        
        self.edit = customtkinter.CTkButton(master=self.tabla1,
                                                text="Editar",
                                                width=50,
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event)
        self.edit.grid(row=0, column=4, columnspan=1, pady=10, padx=30, sticky="e")



#=====================TABLA 2========================#
        self.tabla2 = customtkinter.CTkFrame(master=self.parametros,height=100,width=400)
        self.tabla2.grid(row=1, column=0,sticky="n",padx=10, pady=10)
        #self.tabla1.pack(fill="x",expand=False)

        self.descrip2 = customtkinter.CTkLabel(master=self.tabla2,
                                              text="Aguinado",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.descrip2.grid(row=0, column=0, pady=10, padx=0, sticky="n")

        self.descrip2 = customtkinter.CTkLabel(master=self.tabla2,
                                              text="50%",
                                              text_font=("Roboto Medium", -14))  # font name and size in px
        self.descrip2.grid(row=0, column=1, pady=10, padx=0, sticky="n")
        
        self.edit2 = customtkinter.CTkButton(master=self.tabla2,
                                                text="Editar",
                                                width=50,
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event)
        self.edit2.grid(row=0, column=4, columnspan=1, pady=10, padx=30, sticky="e")


        self.tabla3 = customtkinter.CTkFrame(master=self.parametros,height=100,width=400)
        self.tabla3.grid(row=2, column=0,sticky="n",padx=10, pady=10)
        #self.tabla1.pack(fill="x",expand=False)

        self.descrip3 = customtkinter.CTkLabel(master=self.tabla3,
                                              text="Jubilación",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.descrip3.grid(row=0, column=0, pady=10, padx=0, sticky="n")

        self.descrip3 = customtkinter.CTkLabel(master=self.tabla3,
                                              text="11%",
                                              text_font=("Roboto Medium", -14))  # font name and size in px
        self.descrip3.grid(row=0, column=1, pady=10, padx=0, sticky="n")
        
        self.edit3 = customtkinter.CTkButton(master=self.tabla3,
                                                text="Editar",
                                                width=50,
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event)
        self.edit3.grid(row=0, column=4, columnspan=1, pady=10, padx=30, sticky="e")


#========================table 4 =================================#
        self.tabla4 = customtkinter.CTkFrame(master=self.parametros,height=100,width=400)
        self.tabla4.grid(row=3, column=0,sticky="n",padx=10, pady=10)
        #self.tabla1.pack(fill="x",expand=False)

        self.descrip3 = customtkinter.CTkLabel(master=self.tabla4,
                                              text="INSSJP",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.descrip3.grid(row=0, column=0, pady=10, padx=0, sticky="n")

        self.descrip3 = customtkinter.CTkLabel(master=self.tabla4,
                                              text="3%",
                                              text_font=("Roboto Medium", -14))  # font name and size in px
        self.descrip3.grid(row=0, column=1, pady=10, padx=0, sticky="n")
        
        self.edit3 = customtkinter.CTkButton(master=self.tabla4,
                                                text="Editar",
                                                width=50,
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event)
        self.edit3.grid(row=0, column=4, columnspan=1, pady=10, padx=30, sticky="e")


        #========================table 4 =================================#
        self.tabla4 = customtkinter.CTkFrame(master=self.parametros,height=100,width=400)
        self.tabla4.grid(row=4, column=0,sticky="n",padx=10, pady=10)
        #self.tabla1.pack(fill="x",expand=False)

        self.descrip3 = customtkinter.CTkLabel(master=self.tabla4,
                                              text="Aporte Sindical",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.descrip3.grid(row=0, column=0, pady=10, padx=0, sticky="n")

        self.descrip3 = customtkinter.CTkLabel(master=self.tabla4,
                                              text="3%",
                                              text_font=("Roboto Medium", -14))  # font name and size in px
        self.descrip3.grid(row=0, column=1, pady=10, padx=0, sticky="n")
        
        self.edit3 = customtkinter.CTkButton(master=self.tabla4,
                                                text="Editar",
                                                width=50,
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event)
        self.edit3.grid(row=0, column=4, columnspan=1, pady=10, padx=30, sticky="e")
     
  


#=====================Categoria 1========================#
        self.sueldo1 = customtkinter.CTkFrame(master=self.categorias,height=100,width=400)
        self.tabla1.grid(row=0, column=0,sticky="n",padx=10, pady=10)
        #self.tabla.pack(fill="x",expand=False)

        self.categ1 = customtkinter.CTkLabel(master=self.tabla1,
                                              text="Obra social",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.categ1.grid(row=0, column=0, pady=10, padx=0, sticky="n")

        self.descrip = customtkinter.CTkLabel(master=self.tabla1,
                                              text="3%",
                                              text_font=("Roboto Medium", -14))  # font name and size in px
        self.descrip.grid(row=0, column=1, pady=10, padx=0, sticky="n")
        
        self.edit = customtkinter.CTkButton(master=self.tabla1,
                                                text="Editar",
                                                width=50,
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event)
        self.edit.grid(row=0, column=4, columnspan=1, pady=10, padx=30, sticky="e")



#=====================TABLA 2========================#
        self.tabla2 = customtkinter.CTkFrame(master=self.categorias,height=100,width=400)
        self.tabla2.grid(row=1, column=0,sticky="n",padx=10, pady=10)
        #self.tabla1.pack(fill="x",expand=False)

        self.descrip2 = customtkinter.CTkLabel(master=self.tabla2,
                                              text="Aguinado",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.descrip2.grid(row=0, column=0, pady=10, padx=0, sticky="n")

        self.descrip2 = customtkinter.CTkLabel(master=self.tabla2,
                                              text="50%",
                                              text_font=("Roboto Medium", -14))  # font name and size in px
        self.descrip2.grid(row=0, column=1, pady=10, padx=0, sticky="n")
        
        self.edit2 = customtkinter.CTkButton(master=self.tabla2,
                                                text="Editar",
                                                width=50,
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event)
        self.edit2.grid(row=0, column=4, columnspan=1, pady=10, padx=30, sticky="e")


        self.tabla3 = customtkinter.CTkFrame(master=self.categorias,height=100,width=400)
        self.tabla3.grid(row=2, column=0,sticky="n",padx=10, pady=10)
        #self.tabla1.pack(fill="x",expand=False)

        self.descrip3 = customtkinter.CTkLabel(master=self.tabla3,
                                              text="Jubilación",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.descrip3.grid(row=0, column=0, pady=10, padx=0, sticky="n")

        self.descrip3 = customtkinter.CTkLabel(master=self.tabla3,
                                              text="11%",
                                              text_font=("Roboto Medium", -14))  # font name and size in px
        self.descrip3.grid(row=0, column=1, pady=10, padx=0, sticky="n")
        
        self.edit3 = customtkinter.CTkButton(master=self.tabla3,
                                                text="Editar",
                                                width=50,
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event)
        self.edit3.grid(row=0, column=4, columnspan=1, pady=10, padx=30, sticky="e")

    def button_event(self):
        print("Button pressed")
        #Consulta(1)
        


    def change_Ultimaearance_mode(self, new_Ultimaearance_mode):
        customtkinter.set_Ultimaearance_mode(new_Ultimaearance_mode)

    def on_closing(self, event=0):
        print("Button pressed")
        self.destroy()
        


if __name__ == "__main__":
    Ultima = Ultima()
    Ultima.mainloop()



"""
        self.tabla2 = customtkinter.CTkLabel(master=self.parametros,height=100)
        self.tabla2.grid(row=1, column=0,sticky="n",padx=30, pady=30)
        self.tabla2.pack(fill="x",expand=False)
"""

"""
        self.label_4 = customtkinter.CTkLabel(master=self.parametros,
                                              text="Ingresar nuevo parametro",
                                              text_font=("Roboto Medium", -16)) 
        self.label_4.grid(row=0, column=0, pady=20, padx=10)

        self.sueldo = customtkinter.CTkEntry(master=self.parametros,
                                              width=300,
                                            placeholder_text="Sueldo por Hora")
        self.sueldo.grid(row=3, column=0, columnspan=1, pady=20, padx=30, sticky="n")

        self.categoria1 = customtkinter.CTkComboBox(master=self.parametros,
                                                    values=["categoria 1", "categoria 2","categoria 3"])
        self.categoria1.grid(row=3, column=1, columnspan=1, pady=20, padx=30, sticky="n")

        self.obraSoc = customtkinter.CTkEntry(master=self.parametros,
                                              width=300,
                                            placeholder_text="Obra social")
        self.obraSoc.grid(row=4, column=0, columnspan=1, pady=20, padx=30, sticky="n")

        self.aportes = customtkinter.CTkEntry(master=self.parametros,
                                              width=300,
                                            placeholder_text="aportes")
        self.aportes.grid(row=4, column=1, columnspan=1, pady=20, padx=30, sticky="n")

        self.presentismos = customtkinter.CTkEntry(master=self.parametros,
                                              width=300,
                                            placeholder_text="Presentismo")
        self.presentismos.grid(row=5, column=0, columnspan=1, pady=20, padx=30, sticky="n")

        self.Guardar = customtkinter.CTkButton(master=self.parametros,
                                                text="Guardar",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event)
        self.Guardar.grid(row=10, column=1, columnspan=1, pady=10, padx=50, sticky="e")

"""




     
