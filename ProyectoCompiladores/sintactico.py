from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from interfazPyS import *
from InterfazCanonica import *
from TablaAnalisisSintactico import *
from analisisSintacticoLR import *

def DesplegarAlgoritmoSintactico(opcion):
    arr=["Primeros y siguientes","Colección canónica","Tabla Analisis Sintactico","Análisis Sintáctico LR"]
    if opcion==arr[0]:
        interfazPyS()
    elif opcion==arr[1]:
        InterfazCanonica()
    elif opcion == arr[2]:
        InterfazTablaAS()
    elif opcion == arr[3]:
        analisisSintactico()
    else:
        messagebox.showerror("Error","Aún no existe esa opción")
    return

