import tkinter as tk
from tkinter import ttk

def mostrar_seleccion():
    seleccion = combo.get()
    resultado_label.config(text="Seleccionaste: " + seleccion)

root = tk.Tk()
root.title("ComboBox con Valor Predefinido en tkinter")

# Crear una variable de control para el ComboBox
opciones = ["Opción 1", "Opción 2", "Opción 3", "Opción 4"]
combo = ttk.Combobox(root, values=opciones)
combo.pack()

# Establecer un valor predefinido
combo.set(opciones[0])

# Etiqueta para mostrar la selección
resultado_label = tk.Label(root, text="", pady=10)
resultado_label.pack()

# Botón para mostrar la selección
boton_mostrar = tk.Button(root, text="Mostrar Selección", command=mostrar_seleccion)
boton_mostrar.pack()

root.mainloop()