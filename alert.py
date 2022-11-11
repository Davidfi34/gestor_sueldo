
from tkinter.messagebox import showerror, showwarning, showinfo


def mens(tipo,text):
    if tipo == 1:
        showerror(
            title='Error',
            message=text)
    else: 
      showinfo(
        title='Informacion',
        message=text)


