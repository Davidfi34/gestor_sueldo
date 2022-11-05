from tkinter import Entry, Frame, StringVar, ttk
import tkinter
import customtkinter
from admin.db import Consulta
from crear_doc.doc import pdf
from dbEmpleados import All, Buscar, Insert
from empleados import Empleado
from operaciones import CalNeto, Calcular
from tkcalendar import DateEntry


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class App(customtkinter.CTk):

    WIDTH = 830
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.info = []
        self.datos = []
        self.dato_usuario = StringVar()
        self.fechaN = StringVar()
        
    

        self.title("Gestor")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.iconbitmap("image/icono.ico")
        self.resizable(0,0)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        # call .on_closing() when app gets closed
       
        # ============ PANTALLA PRINCIPAL ============ #

        self.menu = customtkinter.CTkFrame(master=self,height=70,background="white")
        self.menu.pack(fill='x')
        self.principal = customtkinter.CTkFrame(master=self)
        self.principal.pack(expand=True,fill="both")
       
 
        self.cuadro = ttk.Notebook(self.principal)
        self.cuadro.pack(fill="both",expand=True)
        
          # ============ PANTALLAS ============ #
        self.Inicio = Frame(master=self.cuadro,background="#E5E7E9")
        self.Registro = Frame(master=self.cuadro,background="#E5E7E9")
        self.cuadro.add(self.Inicio,text='Inicio',padding=10)
        self.cuadro.add(self.Registro,text='Registro',padding=10)

             # ============ PANTALLAS ============ #

#=======================BOTON CERRAR SESION ==========================#
        self.titulo = customtkinter.CTkLabel(master=self.menu,
                                                text="Gestor",
                                                text_font=("Roboto Medium", -20,)
                                                )
        self.titulo.grid(row=0, column=1, columnspan=2, pady=10, padx=30, sticky="s")
        
        self.cerrar = customtkinter.CTkButton(master=self.menu,
                                                text="Salir",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.on_closing
                                                )
        self.cerrar.grid(row=0, column=3, columnspan=1, pady=10, padx=30, sticky="s")
  #=======================BOTON CERRAR SESION ==========================#


   #===================================frame Inicio- TABLA============================================#
        style = ttk.Style()
        style.theme_use('alt')
        style.configure("Treeview",
                        background="white",
                        foreground='black',
                        rowheight=35,
                        font=("Roboto Medium", 11),
                        fieldbackground="white",            
        ) 
        style.configure("Treeview.Heading",font=("Roboto Medium", 11,'bold'),background="#EAECEE")
    
        self.tree = ttk.Treeview(master=self.Inicio,height=10,columns=("#1", "#2"))
        self.tree.grid(row=0,column=2,columnspan=1,padx=10,pady=40)
    
        self.tree.heading('#0',text='Concepto')
        self.tree.column("# 0" )
        self.tree.heading('#1',text='Unidad')
        self.tree.column("#1")
        self.tree.heading('#2',text='Deducciones')
        self.tree.column("#2")
#===================================frame Inicio============================================#
        self.buscar_dni = customtkinter.CTkEntry(master=self.Inicio,
                                            width=150,
                                            placeholder_text="Ingresar DNI")
        self.buscar_dni.grid(row=0, column=0, columnspan=1, pady=0, padx=20)

      
        self.tabla1 = customtkinter.CTkButton(master=self.Inicio,
                                                text="Buscar",
                                                width=80,
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.get_parametros)
        self.tabla1.grid(row=0, column=1, columnspan=1)

        self.usuario = customtkinter.CTkLabel(master=self.Inicio,
                                               textvariable= self.dato_usuario,
                                                text_font=("Roboto Medium", -15,))
        self.usuario.grid(row=3, column=0, columnspan=1, pady=0, padx=20)

        self.Guardar = customtkinter.CTkButton(master=self.Inicio,
                                                text="Descargar",
                                                width=80,
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.descarga
                                                )
        self.Guardar.grid(row=3, column=2, columnspan=1,padx= 50,pady=20)
       # self.tabla1.pack(pady=50,padx=0)

#===================================frame Inicio============================================#


#========================= FRAME REGISTRO ================================#

        self.label_2 = customtkinter.CTkLabel(master=self.Registro,
                                              text="Nuevo registro",
                                              text_font=("Roboto Medium", -16,))  # font name and size in px
        self.label_2.grid(row=0, column=0, pady=10, padx=0, sticky="n")


        self.apellido = customtkinter.CTkEntry(master=self.Registro,
                                              width=300,
                                            placeholder_text="Apellido")
        self.apellido.grid(row=3, column=0, columnspan=1, pady=20, padx=30, sticky="n")



        self.nombre = customtkinter.CTkEntry(master=self.Registro,
                                              width=300,
                                            placeholder_text="Nombre")
        self.nombre.grid(row=3, column=1, columnspan=1, pady=20, padx=30, sticky="n")

        self.dni = customtkinter.CTkEntry(master=self.Registro,
                                            width=300,
                                            placeholder_text="DNI")
        self.dni.grid(row=4, column=0, columnspan=1, pady=20, padx=30, sticky="n")

        self.Ingreso =customtkinter.CTkLabel(self.Registro,text="Fecha de nacimiento",text_font=("Roboto Medium", -14,),text_color='gray').place(x= 390,y=137)
        self.campofecha = DateEntry(self.Registro,date_pattern='y-mm-dd',width=15,year= 2004,month= 10,day=1,textvariable = self.fechaN).place(x= 660,y=175)

        self.direccion = customtkinter.CTkEntry(master=self.Registro,
                                              width=300,
                                            placeholder_text="Direccion")
        self.direccion.grid(row=5, column=0, columnspan=1, pady=20, padx=30, sticky="n")

        self.localidad = customtkinter.CTkEntry(master=self.Registro,
                                              width=300,
                                            placeholder_text="localidad")
        self.localidad.grid(row=5, column=1, columnspan=1, pady=20, padx=30, sticky="n")

        self.telefono = customtkinter.CTkEntry(master=self.Registro,
                                                width=300,
                                            placeholder_text="Telefono")
        self.telefono.grid(row=6, column=0, columnspan=1, pady=20, padx=30, sticky="n")

        self.categoria = customtkinter.CTkComboBox(master=self.Registro,
                                                    values=['1','2','3'])
        self.categoria.grid(row=6, column=1, columnspan=1, pady=20, padx=30, sticky="s")

        
        self.button_2 = customtkinter.CTkButton(master=self.Registro,
                                                text="Registrar",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.Registro_Empleado)
        self.button_2.grid(row=8, column=1, columnspan=1, pady=10, padx=30, sticky="e")

#=========================================================================#

#========= ALERT ===============#
    def abrir(self,texto):
      top = tkinter.Toplevel()
      top.resizable(0,0)
      top.iconbitmap("image/icono.ico")
      top.geometry("300x200")
      top = tkinter.Label(top, text=texto)
      top.pack(expand=True)
#===============================#

#==========REGISTRAR EMPLEADO====================#
    def Registro_Empleado(self):
        nuevo = Empleado(dni=self.dni.get(),apellido=self.apellido.get(),nombre=self.nombre.get(),
        fechaN=self.fechaN.get(),direccion= self.direccion.get(),localidad= self.localidad.get(),telefono= self.telefono.get())
        Result = Insert(nuevo,int(self.categoria.get()))
      
        if(Result == True): 
          print('Empleado Registrado')
          self.clear()
          self.abrir(texto='Empleado registrado')
        else: 
          self.abrir(texto='Error empleado no registrado')
#=======================================================#



#====================CLEAR ENTRY==============================#
    def clear(self):
          self.dni.delete(0, 'end'), self.apellido.delete(0, 'end'), self.nombre.delete(0, 'end'),
          self.direccion.delete(0, 'end'), self.localidad.delete(0, 'end'), self.telefono.delete(0, 'end')
#==================================================#



#============OBTIENE CONCEPTOS ============#
    def get_parametros(self):
      #limpia paramentros
      self.dato_usuario.set('')
      self.datos = []
      self.info =[]
      records =self.tree.get_children()
      for element in records:
        self.tree.delete(element)

      total = 0
      query = Consulta()
      getDni = self.buscar_dni.get()
      if len(getDni)> 0:
        self.datos.append(Buscar(getDni))
        empleado = Buscar(getDni)

        if empleado != None :
          self.dato_usuario.set(empleado[1]+" "+empleado[2])
          total_horas = empleado[9]
          self.tree.insert('', 0,text='Horas laborales', values=(f"{total_horas}{' horas'}",(f"{'$'}{CalNeto(total_horas,empleado[8])}")))
          total += CalNeto(total_horas,empleado[8])
          #======AGREGA DATOS PARA DUC ======#
          self.info.append(['Horas laborales',(f"{total_horas}{' horas'}"), (f"{'$'}{CalNeto(total_horas,empleado[8])}")])
          #=================================#
          for row in query:
            self.tree.insert('', 1,text= row[1], values= (f"{row[2]}{'%'} ",(f"{'$'}{round(Calcular(getDni,row[2],row[3]), 2)}")))

            #======AGREGA DATOS PARA DUC ======#
            self.info.append([row[1], (f"{row[2]}{'%'} "),(f"{'$'}{round(Calcular(getDni,row[2],row[3]), 2)}")])
            #===================================#

            if row[3] == 1: total -= Calcular(getDni,row[2],row[3])
            else: total += Calcular(getDni,row[2],row[3])

          self.tree.insert('', 20,text='TOTAL',values=('',(f"{'$'}{round(total,2)}")))

          #======AGREGA DATOS PARA DUC ======#
          self.info.append(['TOTAL', "",(f"{'$'}{round(total,2)}")])
          #==================================#

       



#================= DESCARGA PDF =======================#
    def descarga(self):
        if len(self.info) > 0 and len(self.datos): pdf(self.info,self.datos)

#======================================================#
        

#===========CERRAR APP================#
    def on_closing(self):
        self.destroy()
#===========================#
       


if __name__ == "__main__":
    app = App()
    app.mainloop()
