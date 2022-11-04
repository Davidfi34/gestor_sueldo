from dbEmpleados import Buscar, getCateg
from empleados import Empleado


nuevo = Empleado(2,'Diego','Gonzalez','1985-02-14','Mendoza 4500','Rosario',15546789)

#Insert(e=nuevo,categoria=1)

def Calcular(dni,porcetaje,tipo):
    total = 0 
    ver = Buscar(dni)
    total_horas = ver[9]
    categ = ver[8]

    costo_hora = getCateg(categ)[0]
    total_neto = total_horas * costo_hora
   # print(total_neto)
    if tipo == 1: total = (total_neto * porcetaje)/100
    else: total = (total_neto * porcetaje)/100
    return total

def CalNeto(horas,id):
    costo_hora = getCateg(id)[0]
    return horas * costo_hora
    




