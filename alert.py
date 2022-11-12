
import tkinter
from tkinter.messagebox import askyesno, showerror, showinfo


def mens(tipo,text):
    if tipo == 1:
        showerror(
            title='Error',
            message=text)
    elif tipo == 2: 
      showinfo(
        title='Informacion',
        message=text)
    else:
      respuesta = askyesno("Gestor", text)
      return respuesta

