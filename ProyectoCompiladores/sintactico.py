from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from PrimerosYSiguientes import *

def DesplegarAlgoritmoSintactico(opcion):
    arr=["Primeros y Siguientes", "Canonica"]
    if opcion==arr[0]:
        #print("Primeros y siguientes")
        PrimerosYSiguientes()
    else:
        messagebox.showerror("Error","Aún no existe esa opción")
    return

