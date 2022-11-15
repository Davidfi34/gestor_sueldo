import sqlite3

conn = sqlite3.connect('liquidaciones.db')
c= conn.cursor()


def Crear():
    c.execute(""" CREATE TABLE IF NOT EXISTS administrador (
        contra TEXT PRIMARY KEY,
        usuario TEXT
    )""")

    c.execute(""" CREATE TABLE IF NOT EXISTS empleados (
        dni int NOT NULL PRIMARY KEY ,
        nombre TEXT,
        apellido TEXT,
        fechaN DATE,
        direccion TEXT,
        localidad TEXT
    )""")

    c.execute(""" CREATE TABLE IF NOT EXISTS dato_empleado (
        dni INT ,
        categoria INT,
        horas INT,
        FOREIGN KEY (dni)
        REFERENCES empleados (dni),
        FOREIGN KEY (categoria)
        REFERENCES honorarios (id_categoria)
    )""")

    c.execute(""" CREATE TABLE IF NOT EXISTS parametros (
        id_param integer primary key AUTOINCREMENT,
        descripcion TEXT,
        porcentaje REAL,
        tipo INT
   
    )""")

    c.execute(""" CREATE TABLE IF NOT EXISTS categorias (
        id_categoria INT PRIMARY KEY,
        descripcion TEXT,
        monto REAL
    )""")
    IngresarDatos()


def IngresarDatos():
    try:
        c.execute("INSERT INTO administrador(contra,usuario) VALUES(?,?)", ('1234','admin',))
        c.execute("INSERT INTO categorias VALUES (1,'operario 1',450),(2,'operario 2',550),(3,'operario 3',750)")
        c.execute("INSERT INTO parametros VALUES (1,'Obra social',3,1),(2,'Jubilacion',11,1),(3,'Sindicato',2.5,1),(4,'Ley 19032',3,1),(5,'Presetismo',8.3,2)")
        print('creo registro')
        conn.commit()
    except sqlite3.Error as error:
        Crear()
    #conn.close()
    
def Consulta():
    try:
        c.execute("SELECT * FROM parametros")
        result = c.fetchall()
        return result
    except sqlite3.Error as error:
        print('error')
        Crear()
   # conn.close()
    
    

 

def LoginDB(usario,contra):
    result = False
    try:
        c.execute("SELECT * FROM administrador WHERE usuario = ? AND contra = ?",(usario,contra,) )
        query = len(c.fetchall())
        if query > 0:
            result = True
    except sqlite3.Error as error:
        print('error')
    return result



def Insert_p(e):
    result = False
    if len(e.descrip) != 0 and len(e.porcentaje)!=0 and len(e.tipo)!=0:
        try:
            c.execute("INSERT INTO parametros VALUES (null,?,?,?)",(e.descrip,e.porcentaje,e.tipo))
            conn.commit()
            result = True
        except sqlite3.Error as error:
            print("Error", error)
    #conn.close()
    return result

def update(descrip,porc,tipo,id):
    result = False
    if len(descrip) != 0 and len(porc)!=0 and len(tipo)!=0:
        try:
            result = c.execute('''UPDATE parametros SET descripcion = ?,porcentaje = ?,tipo = ? WHERE id_param = ?''',(descrip,porc,tipo,id))
            conn.commit()
            result = True
        except sqlite3.Error as error:
            print("Error", error)
    return result

def delete(id):
    result = False
    try:
        result = c.execute('''DELETE FROM parametros WHERE id_param = ?''',(id,))
        conn.commit()
        result = True
    except sqlite3.Error as error:
         print("Error", error)
    return result