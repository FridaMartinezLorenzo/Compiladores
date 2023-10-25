from tkinter import *
import lexico as lx
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from Thompson1 import *

def Conjuntos():
    font1=("Times New Roman",12)
    arrLabels=[]
    lexWindow=Toplevel()
    lexWindow.state("zoomed")
    lexWindow.title("Construccion de Conjuntos")
    lexWindow.config(bg="#363062")

    archivoL=Label(lexWindow,text="Selecciona una expresión regular",width=30,font=font1)
    archivoL.place(x=20,y=30)

    archivoButton=Button(lexWindow,text="Abrir archivo",width=20,command=lambda:abrirArchivo(alphaEntry,erEntry,lexWindow),bg="#F99417" ,font=font1)
    archivoButton.place(x=350,y=20)

    eregularL=Label(lexWindow,text="Expresión regular seleccionada",font=font1,width=30)
    eregularL.place(x=20,y=100)

    erEntry=Entry(lexWindow,width=30,font=font1)
    erEntry.place(x=350,y=100)

    alphaLabel=Label(lexWindow,text="Alfabeto",font=font1,width=30)
    alphaLabel.place(x=650,y=100)

    alphaEntry=Entry(lexWindow,font=font1,width=30)
    alphaEntry.place(x=950,y=100)

    canvas=Canvas(lexWindow,width=1500,height=450)
    canvas.place(x=0,y=200)

    def on_arrow_key(event):
            if event.keysym == "Left":
                canvas.xview_scroll(-1, "units")
            elif event.keysym == "Right":
                canvas.xview_scroll(1, "units")
            canvas.config(scrollregion=canvas.bbox("all"))    

    def on_arrow_key_v(event):
         if event.keysym == "Up":
             canvas.yview_scroll(-1, "units")
         elif event.keysym == "Down":
             canvas.yview_scroll(1, "units")
         canvas.config(scrollregion=canvas.bbox("all"))
    
    scrollbar=ttk.Scrollbar(canvas, orient="vertical", command=canvas.yview)

    scrollbar.set(0.0, 1.0)
    scrollbar.place(x=1500, y=50, height=300)

    horizontal_scrollbar = ttk.Scrollbar(canvas, orient="horizontal", command=canvas.xview)
    horizontal_scrollbar.set(0.0,1.0)
    horizontal_scrollbar.place(x=0,y=450,width=200)

    tabla=Frame(canvas,width=1500,height=400)
    canvas.create_window((0, 0), window=tabla, anchor=NW)
    canvas.configure(yscrollcommand=scrollbar.set,xscrollcommand=horizontal_scrollbar.set)

    def on_mousewheel(event):
         canvas.yview_scroll(-1 * (event.delta // 120), "units")
    
    afnButton=Button(lexWindow,text="Obtener AFN",width=15,font=font1,bg="#F99417",command=lambda:printTable(alphaEntry.get(),tabla,canvas,lexWindow,arrLabels,erEntry.get()) )
    afnButton.place(x=150,y=150)
    cleanButton=Button(lexWindow,text="Limpiar",font=font1,bg="#F99417",command=lambda:cleanTable(tabla,arrLabels,alphaEntry,erEntry))
    cleanButton.place(x=350,y=150)
    tabla.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    canvas.bind("<MouseWheel>", on_mousewheel)
    canvas.bind_all("<KeyPress-Left>", on_arrow_key)
    canvas.bind_all("<KeyPress-Right>", on_arrow_key)
    canvas.bind_all("<KeyPress-Up>", on_arrow_key_v)
    canvas.bind_all("<KeyPress-Down>", on_arrow_key_v)


def  printTable(alfabeto,tabla,canvas,lexWindow,arrLabels,er):
    expresion_reg = er
    expresion_reg = expresion_postfija(expresion_reg)
    print(expresion_reg)
    Automata=evaluar_expresion_postfija(expresion_reg)

    cerradura=[]
    cerradura.append(Automata.head.state.getId())#Agrega el estado inicial para que se haga la cerradura
    cerradura=cerradura_e(cerradura,Automata.head,"λ")
    cerradura.insert(0,0)#Agrega el estado 0 al inicio del primer estado manualmente
    cerradura.sort()#Ordena solo el estado 0
    NuevosEstados=AFD(cerradura,alfabeto,Automata.head)
    NuevosEstados.insert(0,cerradura)
    print(NuevosEstados)

    font1=("Times New Roman",11)
    estados=alfabeto
    columna=1
    encabezadoL=Label(tabla,text="Estado",font=font1,borderwidth=1, relief="solid",width=20)
    encabezadoL.grid(row=0,column=0)
    abecedario=[]
    for letra in estados:
        ColumnaL=Label(tabla,text=str(letra),width=20,borderwidth=1, relief="solid",font=font1)
        ColumnaL.grid(row=0,column=columna)
        arrLabels.append(ColumnaL)
        abecedario.append(letra)
        columna+=1
    abecedario.append("λ")
    lambdaL=Label(tabla,text="ε",font=font1,borderwidth=1, relief="solid",width=20)
    lambdaL.grid(row=0,column=columna)
    arrLabels.append(encabezadoL)
    arrLabels.append(lambdaL)
    tabla.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    numEstados=len(estados)#Numero de estados
    if numEstados:
        #elementos=[(1,2,3,5,4),(4,5,6),(7,8,9),(10,11,12),(13,14,15),(16,17,18),(19,20,21),(19,20,21),(19,20,21),(19,20,21),(19,20,21),(19,20,21),(19,20,21),(19,20,21),(19,20,21),(10,20,30),(10,20,70),(10,20,30),(10,20,30),(10,20,30),(1,2,3)]
        #i=1
        #for j in elementos:
        #    tupla=j
        #    l=0
        #    for k in tupla:
        #        celda=Label(tabla,text=str(k),width=20,borderwidth=1, relief="solid",font=font1)
        #        celda.grid(row=i,column=l)
        #        tabla.update_idletasks()
        #        l+=1
        #    i+=1
        i=1
        nodo=Automata.head
        while nodo:
            l=0
            num_estado=nodo.state.getId()
            celda=Label(tabla,text=str(num_estado),width=20,borderwidth=1, relief="solid",font=font1)
            celda.grid(row=i,column=l)
            l+=1
            edos=nodo.state.getTransitions()
            #print(edos)
            for transition in edos :
                l=1#Reestablecer columnas
                caracter=transition.getSymbol()
                #print(edo_sig)
                for aux in abecedario:#Para poner guiones
                    #print()
                    if aux==caracter:
                        #celda_sym=Label(tabla,text=str( transition.getState()+","+str),width=20,borderwidth=1, relief="solid",font=font1)
                        celda_sym=Label(tabla,text=str(nodo.state),width=20,borderwidth=1, relief="solid",font=font1)
                        celda_sym.grid(row=i,column=l)
                    else:
                        celda_sym=Label(tabla,text="-",width=20,borderwidth=1, relief="solid",font=font1)
                        celda_sym.grid(row=i,column=l)
                    l+=1
            i+=1
            nodo=nodo.next
        num_letras=len(abecedario)
        m=1
        i=i-1
        while m<=num_letras:
            celda_sym=Label(tabla,text="-",width=20,borderwidth=1, relief="solid",font=font1)
            celda_sym.grid(row=i,column=m)
            m+=1
        canvas.config(scrollregion=canvas.bbox("all"))
    else:
        lexWindow.grab_set()
        messagebox.showerror("Error","introduce un alfabeto")
        lexWindow.grab_release()

def cerradura_e(elems,head,letra):
    pila=[]
    conjunto=[]
    #edos=nodo.state.getTransitions()#Tiene todas las transiciones de 0

    for i in elems:#Agrega elementos a la pila
        pila.append(i)
    while pila:#Va sacando los numeros de estados de la lista
        elemento=pila.pop()#Obtiene el ultimo estado en la pila
        nodo1=buscarNodo(head,elemento)#Busca si esta el nodo en la
        edos=nodo1.state.getTransitions()#Retorna el arreglo de transiciones
        for transition in edos:#Recorrer todas las transiciones
            char=transition.getSymbol()#Obtiene solo el simbolo de la transicion iterada
            if char==letra:#Compara lambda con el simbolo de la transicion
                pila.append(transition.getState())#Agrega el estado al conjunto generado
                conjunto.append(transition.getState())#
    return conjunto #Devuelve una lista

def buscarNodo(head,num_estado):
    nodo=head
    while nodo:
        if num_estado==nodo.state.getId():
            return nodo#Encontro el nodo buscado
        nodo=nodo.next
    return None#No encontró nada

def AFD(listaInicial,abecedario,head):
    pilaEdos=[]
    pilaEdos.append(listaInicial)#Agregar el primer estado A
    conjuntoEdos=[]#trae los nuevos estados
    transicionesEstado=[]#trae una lista de tuplas
    transiciones=[]
    while pilaEdos:
        #print("pila",pilaEdos)
        estado=pilaEdos.pop()
       # pilaEdos = [sublista for sublista in pilaEdos if sublista]
        for letra in abecedario:#Mandar el alfabeto sin epsilon
            cerraduraAux= Mueve(estado,head,letra)
            nuevoEdo=cerradura_e(cerraduraAux,head,"λ")
            nuevoEdo+=cerraduraAux#Unir la lista Mueve con la otra lista
            nuevoEdo.sort()
            if nuevoEdo not in conjuntoEdos:
                pilaEdos.append(nuevoEdo)
                #pilaEdos = [sublista for sublista in pilaEdos if sublista]
                conjuntoEdos.append(nuevoEdo)
                #conjuntoEdos=[sublista for sublista in conjuntoEdos if sublista]
                #print("Conjunto=",conjuntoEdos)    

            transicionesEstado.append((estado,letra,nuevoEdo))
            cerraduraAux.clear()
            
        transiciones.append(transicionesEstado)
        #transicionesEstado.clear()

    #conjuntoEdos=[sublista for sublista in conjuntoEdos if sublista]
    return conjuntoEdos

def Mueve(elems,head,letra):#Esta funcion realiza el Mueve
    pila=[]
    conjunto=[]
    for i in elems:
        pila.append(i)
    while pila:
        elemento=pila.pop()#Obtener
        nodo1=buscarNodo(head,elemento)
        edos=nodo1.state.getTransitions()
        for transition in edos:#Recorrer todas las transiciones
            char=transition.getSymbol()
            if char==letra:
                #pila.append(transition.getState())
                conjunto.append(transition.getState())

    #cerraduratemp=cerradura_e(conjunto,head,letra)
    cerradura=[]
    for j in conjunto:
        cerradura.append(j)

    return cerradura #Devuelve una lista

def cleanTable(tabla,arrLabels,alphaEntry,erEntry):
    for widget in tabla.winfo_children():
        widget.destroy()
    for widget in arrLabels:
        widget.destroy()
    arrLabels.clear()#Limpiar la lista
    alphaEntry.delete(0,END)
    erEntry.delete(0,END)

def abrirArchivo(alphaEntry,erEntry,lexWindow):
    lexWindow.grab_set()
    alphaEntry.delete(0,END)
    erEntry.delete(0,END)
    direccionArchivo=filedialog.askopenfilename(initialdir=r"C:\Users\Documents\Compiladores",title="Abrir",filetypes=(("texto","*.txt"),))
    archivo=open(direccionArchivo)
    alfabeto=archivo.readline()
    expresionRegular =archivo.readline()
    expresionRegular = expresionRegular.replace('digitos','d')
    expresionRegular = expresionRegular.replace('letras','l')
    print(expresionRegular)
    #expresionRegular=expresionRegular[:-1]
    alfabeto = alfabeto.strip()
    alfabeto = alfabeto.replace('letras','l')
    
    #Si tiene la palabra reservada digito, letra sustituye y hay que encender la bandera para identificar
    indice_dig = alfabeto.find("digitos")
    if indice_dig != -1:
        alfabeto = alfabeto.replace('digitos','d')
        bandera_transformacion_digitos = 1
    
    indice_alfa = alfabeto.find("letras")
    if indice_alfa != -1:
        alfabeto = alfabeto.replace('digitos','d')
        bandera_transformacion_alfabeto = 1

    
    print(alfabeto)
    alphaEntry.insert(0,alfabeto)
    erEntry.insert(0,expresionRegular)
    lexWindow.grab_release()