from tkinter import *
from tkinter import ttk 
import customtkinter
from admin.db import Consulta, Insert_p, delete, update
from alert import mens
from crear_doc.doc import pdf
from dbEmpleados import  Buscar, Insert
from empleados import Empleado
from operaciones import CalNeto, Calcular
from tkcalendar import DateEntry

from parametro import Parametro


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

class App(customtkinter.CTk):

    WIDTH = 830
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.info = []
        self.datos = []
        self.dato_usuario = StringVar()
        self.fechaN = StringVar()
        self.id_dato = StringVar()
        
        self.ver_pametros = Consulta()
        
        self.dato_param = StringVar()
        self.dato_porcentaje = StringVar()
        self.dato_tipo = StringVar()
        self.item =StringVar()

        self.iconAct = PhotoImage(file="image/actualizar.png")
        self.iconEdit = PhotoImage(file="image/edit.png")
        self.iconDelete = PhotoImage(file="image/delete.png")
 
     


        self.title("Gestor")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.iconbitmap("image/icono.ico")
        self.resizable(0,0)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
      
       
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
        self.Parametros = Frame(master=self.cuadro,background="#E5E7E9")
        self.cuadro.add(self.Inicio,text='Inicio',padding=10)
        self.cuadro.add(self.Registro,text='Registro',padding=10)
        self.cuadro.add(self.Parametros,text='Parametros',padding=10)

             # ============ PANTALLAS ============ #

#=======================BOTON CERRAR SESION ==========================#
        self.titulo = customtkinter.CTkLabel(master=self.menu,
                                                text="Liquidacion de sueldo",
                                                text_font=("Roboto Medium", -15,)
                                                )
        self.titulo.grid(row=0, column=1, columnspan=2, pady=10, padx=50, sticky="s")
        
        self.cerrar = customtkinter.CTkButton(master=self.menu,
                                                text="Salir",
                                                width=100,
                                                command=self.on_closing
                                                )
        self.cerrar.place(x=680,y=10)

  #=======================BOTON CERRAR SESION ==========================#


   #===================================frame Inicio- TABLA============================================#
        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview",
                        background="white",
                        foreground='black',
                        rowheight=35,
                        font=("Roboto Medium", 11),
                        fieldbackground="white",            
        ) 
        style.configure("Treeview.Heading",font=("Roboto Medium", 10,'bold'),background="#EAECEE")
    
        self.tree = ttk.Treeview(master=self.Inicio,height=10,columns=("#1", "#2"))
        self.tree.grid(row=0,column=3,columnspan=1,padx=20,pady=30)
    
        self.tree.heading('#0',text='Concepto')
        self.tree.column("# 0" )
        self.tree.heading('#1',text='Unidad')
        self.tree.column("#1")
        self.tree.heading('#2',text='Deducciones')
        self.tree.column("#2")
#===================================frame Inicio============================================#
        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.left = customtkinter.CTkFrame(master=self.Inicio,
                                                 width=200,
                                                 corner_radius=20)
        self.left.grid(row=0, column=0, sticky="nswe",pady=20,padx=10)




        self.titulo2 = customtkinter.CTkLabel(master=self.left,
                                                text="Buscar empleado",
                                                text_font=("Roboto Medium", -15,)
                                                )
        self.titulo2.grid(row=1, column=0, columnspan=1,padx= 20,pady=20)                                        
       
        self.buscar_dni = customtkinter.CTkEntry(master=self.left,
                                             width=200,
                                            placeholder_text="Ingresar DNI")
        self.buscar_dni.grid(row=2, column=0, columnspan=1,padx= 20,pady=20) 
    
        self.icon_buscar = PhotoImage(file="image/buscar.png")

        self.buscar = customtkinter.CTkButton(master=self.left,
                                                text="Buscar",
                                                width=80,
                                                image=self.icon_buscar,
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.get_parametros)
        self.buscar.grid(row=3, column=0, columnspan=1,padx= 20,pady=20) 
  
        self.usuario = customtkinter.CTkLabel(master=self.left,
                                               textvariable= self.dato_usuario,
                                                text_font=("Roboto Medium", -15,))
        self.usuario.grid(row=4, column=0, columnspan=1,padx= 20,pady=20) 
   
        self.icon_descarga = PhotoImage(file="image/descarga.png")

        self.Descargar = customtkinter.CTkButton(master=self.Inicio,
                                                text="Descargar",
                                                width=80,
                                                image=self.icon_descarga,
                                                fg_color="#58D68D",
                                                hover_color="#ABEBC6",  # <- no fg_color
                                                command=self.descarga
                                                )
        self.Descargar.grid(row=6, column=3, columnspan=1,padx= 50,pady=20)


        self.boton_actualizar2 = customtkinter.CTkButton(master=self.Inicio,
                                                text="",
                                                image=self.iconAct,
                                                width= 20,
                                                fg_color=None,
                                                command= self.get_parametros
                                                )
        self.boton_actualizar2.place(x=770,y=30)

#===================================frame Inicio============================================#


#========================= FRAME REGISTRO ================================#

        self.label_2 = customtkinter.CTkLabel(master=self.Registro,
                                              text="Nuevo registro",
                                              text_font=("Roboto Medium", -16,))  # font name and size in px
        self.label_2.grid(row=0, column=0, pady=10, padx=0, sticky="n")


        self.apellido = customtkinter.CTkEntry(master=self.Registro,
                                              width=250,
                                            placeholder_text="Apellido")
        self.apellido.grid(row=1, column=0, columnspan=1, pady=20, padx=30, sticky="n")



        self.nombre = customtkinter.CTkEntry(master=self.Registro,
                                              width=250,
                                            placeholder_text="Nombre")
        self.nombre.grid(row=1, column=1, columnspan=1, pady=20, padx=30, sticky="n")

        self.dni = customtkinter.CTkEntry(master=self.Registro,
                                            width=250,
                                            placeholder_text="DNI")
        self.dni.grid(row=2, column=0, columnspan=1, pady=20, padx=30, sticky="n")

        self.Ingreso =customtkinter.CTkLabel(self.Registro,text="Fecha de nacimiento",text_font=("Roboto Medium", -14,),text_color='gray').place(x= 340,y=137)
        self.campofecha = DateEntry(self.Registro,date_pattern='y-mm-dd',width=15,year= 2004,month= 10,day=1,textvariable = self.fechaN)
        self.campofecha.place(x= 600,y=175)

        self.direccion = customtkinter.CTkEntry(master=self.Registro,
                                              width=250,
                                            placeholder_text="Direccion")
        self.direccion.grid(row=3, column=0, columnspan=1, pady=20, padx=30, sticky="n")

        self.localidad = customtkinter.CTkEntry(master=self.Registro,
                                              width=250,
                                            placeholder_text="localidad")
        self.localidad.grid(row=3, column=1, columnspan=1, pady=20, padx=30, sticky="n")


        self.Labelcategoria =customtkinter.CTkLabel(self.Registro,text="Nro. Categoria: ",text_font=("Roboto Medium", -14,),text_color='gray').place(x= 320,y=275)
        self.categoria = customtkinter.CTkComboBox(master=self.Registro,
                                                    values=['1','2','3'])
        self.categoria.place(x= 450,y=275)
  
        self.horas = customtkinter.CTkEntry(master=self.Registro,
                                                width=250,
                                            placeholder_text="total de horas:")
        self.horas.grid(row=5, column=0, columnspan=1, pady=20, padx=30, sticky="n")

        
        self.button_2 = customtkinter.CTkButton(master=self.Registro,
                                                text="Registrar",
                                                fg_color="#58D68D",
                                                hover_color="#ABEBC6", # <- no fg_color
                                                command=self.Registro_Empleado)
        self.button_2.grid(row=6, column=2, columnspan=1, pady=50, padx=10, sticky="e")

#=========================================================================#


#===========================================================#

    

        self.tree1 = ttk.Treeview(master=self.Parametros,height=10,columns=("#1"))
        self.tree1.grid(row=0,column=3,columnspan=1,padx=100,pady=30)
    
        self.tree1.heading('#0',text='Concepto')
        self.tree1.column("#0" )
        self.tree1.heading('#1',text=' % ')
        self.tree1.column("#1",anchor='center')

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self.Parametros,
                                                 width=200,
                                                 corner_radius=20)
        self.frame_left.grid(row=0, column=0, sticky="nswe",pady=20,padx=50)



        self.boton_actualizar = customtkinter.CTkButton(master=self.Parametros,
                                                text="",
                                                image=self.iconAct,
                                                width= 20,
                                                fg_color=None,
                                                command= self.actualizar
                                                )
        self.boton_actualizar.place(x=740,y=40)

      
        self.boton_editar = customtkinter.CTkButton(master=self.Parametros,
                                                text="",
                                                image=self.iconEdit,
                                                width= 20,
                                                fg_color=None,
                                                command= self.get_select
                                                )
        self.boton_editar.place(x=740,y=80)

        self.boton_eliminar = customtkinter.CTkButton(master=self.Parametros,
                                                text="",
                                                image=self.iconDelete,
                                                width= 20,
                                                fg_color=None,
                                                command= self.eliminar
                                                )
        self.boton_eliminar.place(x=740,y=120)


        self.Label_descrip =customtkinter.CTkLabel(self.frame_left,text="Concepto: ",text_font=("Roboto Medium", -12,),text_color='gray')
        self.Label_descrip.grid(row=0,column=0,columnspan=1,padx=20,pady=0)

        self.dato_descrip = customtkinter.CTkEntry(master=self.frame_left,  placeholder_text="Descripcion",textvariable=self.dato_param,width=200)
        self.dato_descrip.grid(row=1,column=0,columnspan=1,padx=10,pady=10)
        
        self.Label_porc =customtkinter.CTkLabel(self.frame_left,text="Porcentaje: ",text_font=("Roboto Medium", -12,),text_color='gray')
        self.Label_porc.grid(row=2,column=0,columnspan=1,padx=20,pady=0)

        self.dato_porc = customtkinter.CTkEntry(master=self.frame_left,  placeholder_text="Porcentaje",textvariable=self.dato_porcentaje,width=200)
        self.dato_porc.grid(row=3,column=0,columnspan=1,padx=10,pady=10)

      
        self.texto = customtkinter.CTkLabel(self.frame_left,text="1- Descuentos 2- Bonificacion" ,text_font=("Roboto Medium", -12,),text_color='gray')
        self.texto.grid(row=4,column=0,columnspan=1,padx=0,pady=0)

        self.dato_tipo = customtkinter.CTkComboBox(master=self.frame_left,
                                                    width=200,
                                                    values=['1','2'])
        self.dato_tipo.grid(row=5,column=0,columnspan=1,padx=0,pady=10)


        self.editar = customtkinter.CTkButton(master=self.frame_left,
                                                text="Guardar",
                                                width= 100,
                                            
                                                fg_color="#58D68D",
                                                hover_color="#ABEBC6",
                                                command= self.update_param
                                                )
        self.editar.grid(row=6, column=0, columnspan=1, pady=30, padx=0, sticky="n")


        self.obtener()




#================ACTUALIZA TABLA DE CONCEPTO =====================#
    def actualizar(self):
        self.tree1.delete(*self.tree1.get_children())
        self.dato_descrip.delete(0, 'end')
        self.dato_porc.delete(0, 'end')
        self.dato_tipo.set("")
        self.id_dato.set("")
        self.obtener()
#=================================================================#  


#================  ELIMINA CONCEPTO  =====================#
    def eliminar(self):
          self.get_select()
          m = mens(3,"¿Desea eliminar registro?")
          if m:
            result =delete(self.id_dato.get())
            if result:
              self.actualizar()
              self.id_dato.set("")
#=========================================================#

        
#======================== GUARDAR =============================#
    def update_param(self):
      if self.String(self.dato_descrip.get()) and self.FloatInt(self.dato_porc.get()) and self.Number(self.dato_tipo.get()):
          id =self.id_dato.get()
          #=====ACTUALIZA SI TIENE ID =====#
          if len(id)!= 0:
            result = update(descrip=self.dato_descrip.get(),porc=self.dato_porc.get(),tipo=self.dato_tipo.get(),id=self.id_dato.get())
            if result: mens(2,"Actualizado")  
            else: mens(1,"sin datos!")
            
          else: 
          #========== CREA COCEPTO ===========#
              nuevo =Parametro(descrip=self.dato_descrip.get(),porcentaje=self.dato_porc.get(),tipo=self.dato_tipo.get())
              result = Insert_p(nuevo)
              if result: mens(2,"Concepto creado")  
              else: mens(1,"sin datos!")
          self.id_dato.set("")
          self.actualizar()
      else: mens(1,"Error, datos incorrectos!") 
#==============================================================# 
      


#==========  REGISTRAR EMPLEADO  ====================#
    def Registro_Empleado(self):
      if self.String(self.apellido.get())and self.String(self.nombre.get()) and self.String(self.nombre.get())and self.ValidarDni(self.dni.get()) and self.String(self.fechaN.get()) and self.String(self.direccion.get()) and self.String(self.localidad.get()) and self.Number(self.horas.get()) and self.Number(self.categoria.get()):
          nuevo = Empleado(dni=self.dni.get(),apellido=self.apellido.get(),nombre=self.nombre.get(),
          fechaN=self.fechaN.get(),direccion= self.direccion.get(),localidad= self.localidad.get(),
          horas=int(self.horas.get()),categoria=int(self.categoria.get()))
          Result = Insert(nuevo)      
          if Result: 
              self.clear()
              mens(2,'Empleado registrado')
          else: mens(1,'Error empleado no registrado')
      else: mens(1,'Error! los datos ingresados no son correctos')

#==========VALIDAR CANTIDAD DE NUMEROS DE DNI ================#
    def ValidarDni(self,data):
      result =False
      if self.Number(data) and len(data)> 7: result =True
      return result

#==========VERIFICA SI EL DATO ES NUMERICO ===============#
    def FloatInt(self,data):
        try:
          return float(data) if "." in data else int(data)
        except:
          return FALSE

#=========================================================#


#==========VERIFICA SI CONTIENE UN ENTERO ===============#
    def Number(self,data):
      try:
        int(data)
        result = True
      except(ValueError): result=False 
      return result
#=========================================================#

# ========VERIFICA QUE CONTENGA MAS DE UN CARACTER=========#    
    def String(self,data):
        result =False
        if len(data) > 0: result = True
        return result
#==========================================================#
  
#=======================================================#


#====================CLEAR ENTRY==============================#
    def clear(self):
          self.dni.delete(0, 'end'), self.apellido.delete(0, 'end'), self.nombre.delete(0, 'end'),
          self.direccion.delete(0, 'end'), self.localidad.delete(0, 'end'),self.horas.delete(0, 'end'),
          self.categoria.set(""),self.fechaN.set("")
#==================================================#



#============OBTIENE CONCEPTOS ============#
    def get_parametros(self):
      self.reiniciar(self.tree)
      #limpia paramentros
      self.dato_usuario.set('')
      self.datos = []
      self.info =[]
      total = 0
      query = Consulta()
      getDni = self.buscar_dni.get()
      if self.ValidarDni(getDni):
        self.datos.append(Buscar(getDni))
        empleado = Buscar(getDni)
        if empleado != None :
          #self.buscar_dni.delete(0, 'end')
          self.dato_usuario.set(empleado[1]+" "+empleado[2]+"\n\nDNI: "+getDni)
      
          total_horas = empleado[8]

          self.tree.insert('', 0,text='Horas laborales', values=(f"{total_horas}{' horas'}",(f"{'$'}{CalNeto(total_horas,empleado[7])}")))
          total += CalNeto(total_horas,empleado[7])
          #======AGREGA DATOS PARA DUC ======#
          self.info.append(['Horas laborales',(f"{total_horas}{' horas'}"), (f"{'$'}{CalNeto(total_horas,empleado[7])}")])
          #=================================#
          for row in query:
      
            self.tree.insert('', 1,text= row[1], values= (f"{row[2]}{'%'} ",(f" {' ' if row[3] == 2 else '-'} {'$'}{round(Calcular(getDni,row[2],row[3]), 2)}")))

            #======AGREGA DATOS PARA DUC ======#
            self.info.append([row[1], (f"{row[2]}{'%'} "),(f"{' ' if row[3] == 2 else '-'} {'$'}{round(Calcular(getDni,row[2],row[3]), 2)}")])
            #===================================#

            if row[3] == 1: total -= Calcular(getDni,row[2],row[3])
            else: total += Calcular(getDni,row[2],row[3])
         
          self.tree.insert('', 20,text='TOTAL',values=('',(f"{'$'}{round(total,2)}")))
          

          #======AGREGA DATOS PARA DUC ======#
          self.info.append(['TOTAL', "",(f"{'$'}{round(total,2)}")])
        else: mens(1,"El DNI no está registrado!")
      else: mens(1,"Error, ingresar dni!")
#==========================================#


#=======Limpiar tabla principal ======#
    def reiniciar(self,tipo):
      records = tipo.get_children()
      for element in records:
        self.tree.delete(element)
    
#=======================================#


#================= DESCARGA PDF =======================#
    def descarga(self):
        if len(self.info) > 0 and len(self.datos): pdf(self.info,self.datos)
        else: mens(1,"Error! sin datos")

#======================================================#
        



#========= OBTENER DATOS DE BD E INSERTAR EN TABLA============#
    def obtener(self):
          resp = Consulta()
          i = 0
          for row in resp:
              self.tree1.insert('',  0, iid=i,text= row[1],values= row[2],tags=(row[0],row[3]))
              i+= 1
#=============================================================#


#================ OBTENER DATOS DE SELCCION DE REGISTRO ==============#
    def get_select(self):
      selected_item = self.tree1.focus()
      if selected_item:
      
        id = self.tree1.item(selected_item)["tags"][0]
        text = self.tree1.item(selected_item)["text"]
        porcentaje = self.tree1.item(selected_item)["values"][0]
        tipo = self.tree1.item(selected_item)["tags"][1]
        self.dato_param.set(text)
        self.dato_porcentaje.set(porcentaje)
        self.dato_tipo.set(tipo)
        self.id_dato.set(id)
      else: mens(1,"Ningun item seleccionado ")
#====================================================================#
     
#===========CERRAR APP================#
    def on_closing(self):
        self.destroy()
#===========================#



if __name__ == "__main__":
    app = App()
    app.mainloop()
