from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from PrimerosYSiguientes import *
from siguientesFinal import *
from InterfazCanonica import *

def DesplegarAlgoritmoSintactico(opcion):
    arr=["Primeros", "Siguientes","Colección canónica"]
    if opcion==arr[0]:
        #print("Primeros y siguientes")
        PrimerosYSiguientes()
    elif opcion==arr[1]:
        SiguientesMain()
    elif opcion==arr[2]:
        InterfazCanonica()
    else:
        messagebox.showerror("Error","Aún no existe esa opción")
    return

