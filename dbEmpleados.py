import sqlite3
from empleados import Empleado
import random

conn = sqlite3.connect('liquidaciones.db')
c= conn.cursor()

#=================INGRESAR NUEVO EMPLEADO ===============#
def Insert(e,categoria):
    result = False
    horas = random.randrange(160,200)
    try:
        c.execute("INSERT INTO empleados VALUES(?,?,?,?,?,?,?)", (e.dni,e.nombre,e.apellido,e.fechaN,e.direccion,e.localidad,e.telefono))
        c.execute("INSERT INTO dato_empleado VALUES(?,?,?)", (e.dni,categoria,horas))
        conn.commit()
        result = True
    except sqlite3.Error as error:
        print("Error", error)
    #conn.close()
    return result
#========================================================#

#=================SELECT EMPLEADO ===============#
def Buscar(e):
        #Crear()
        try:
            c.execute("SELECT * FROM empleados AS e JOIN dato_empleado AS d ON d.dni = e.dni WHERE e.dni = ?",(e,) )
            query = c.fetchone()
            return query
        except sqlite3.Error as error:
            print('error')
        
        conn.close()
#===============================================#

#============TODOS LOS EMPLEADOS==================#
def All():
    c.execute("SELECT * FROM empleados AS e JOIN dato_empleado AS d ON  d.dni = e.dni")
    conn.commit()
    empleados = c.fetchall()
    #conn.close()
    return empleados
#===============================================#

#====================OBTENER HORA X CATEGORIA===========================#
def getCateg(id):
    c.execute("SELECT monto FROM categorias WHERE id_categoria = ?",(id,))
    conn.commit()
    catg = c.fetchone()
    return catg
#===============================================#
