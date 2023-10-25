from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from lexico import *

root=Tk()
root.title("Compilador")#Titulo de ventana
root.iconbitmap("Compiler.ico")#Icono del programa
root.geometry("900x900")
root.state("zoomed")
root.config(bg="#363062")

def sublexico():
    arr=["Algoritmo de Thompson", "Algoritmo de Contruccion de Conjuntos","Analizador Lexico"]
    # Crear una variable de control para el ComboBox
    combo = ttk.Combobox(root, values=arr,width=23,height=15,font=font1,state="readonly")
    combo.place(x=520,y=350)
    lexicoButton.config(text="Buscar",command=lambda:analizadorLexico(combo.get()))
    combo.set(arr[0])

font1=("Times New Roman",14)

lexicoButton=Button(root,text="Analizador léxico",width=22,command=sublexico,bg="#F99417"   ,font=font1    )
lexicoButton.place(x=522,y=300)

syntaxButton=Button(root,text="Analizador sintáctico",width=22,bg="#F99417"  ,font=font1, state=DISABLED   )
syntaxButton.place(x=790,y=300)

semanticoButton=Button(root,text="Analizador semántico",width=22,bg="#F99417"   ,font=font1, state=DISABLED )
semanticoButton.place(x=1060,y=300)

root.mainloop()