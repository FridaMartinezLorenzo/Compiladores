from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from itertools import islice
import getpass
from tkinter import ttk 




def calcularReglasP(ruta,archivo,listaNoTerminales):
    listaProducciones=[]#contiene las tuplas de las producciones
    cadena = []
    lineas = archivo.readlines()   
    #print(len(lineas))
    archivo2=open(str(ruta),encoding="utf-8")
    archivo2.readline()#Salto de linea en el archivo
    archivo2.readline()
    #print(len(lineas))
    for l in lineas:#Obtener las producciones de cada no terminal
        cadena=[]
        reglaP = archivo2.readline().split("->")  # separa el no terminal de la produccion
        reglaP[1] = reglaP[1].replace("\n", "")  # quita el salto de linea
        indice = 0
        cad=reglaP[1]
        while indice < len(cad):
            aux=""
            if cad[indice] == ' ':
                indice+=1
            if indice < len(cad):
                caracter = cad[indice]  
                if caracter.isupper() == True:
                    cadena.append(caracter)
                    indice += 1
                elif caracter.isalpha() == False:
                    cadena.append(caracter)
                    indice += 1
                else:
                    while caracter.islower() == True and indice < len(cad):
                        caracter = cad[indice]
                        aux+=caracter
                        indice += 1
                    cadena.append(aux)
        producciones = (reglaP[0], cadena)
        listaProducciones.append(producciones)

    return listaProducciones

def getProducciones(symbol):#Ya esta bien
    global reglasProduccion
    aux=[]
    for i in reglasProduccion :
        if i[0] == symbol:
            aux.append(i[1])
    return aux

def ObtenerPrimeros(noTerminales,producciones):
    primerosP=[]

def primeros(symbol):#Funcion recursiva que obtiene los primeros de un simbolo dado symbol
    global terminales,noTerminales, primerosArray
    if symbol in terminales or not symbol.isalpha() or symbol == "λ":#Si es terminal o lambda
        print("obj=",symbol)
        return [symbol]
    if getPrimeros(symbol) is not None:  # Ya se calcularon estos primeros
        return getPrimeros(symbol)
    array1 = []
    for produccion in getProducciones(symbol):#getProducciones(symbol) devuelve una lista de listas con las reglas de produccion
        
        for a in produccion:
            if a == symbol and a in noTerminales:
                break  # Es el mismo no terminal
            elif a.islower() or not a.isalpha():  # Es un terminal
                aux = primeros(a)
                array1.extend(aux)  # Agrega los primeros de 'a' al conjunto de primeros
                if "λ" in aux and "λ" not in array1:
                    array1.append("λ")
                if "λ" not in aux:  # Si 'a' no deriva en λ, deja de procesar esta producción
                    break
            else:  # Es un no terminal
                aux = primeros(a)
                array1.extend(aux)  # Agrega los primeros de 'a' al conjunto de primeros
                if "λ" not in aux:  # Si 'a' no deriva en λ, deja de procesar esta producción
                    break

    primerosArray.append([symbol, array1])
    nuevoArray=quitar_duplicados(array1)
    return nuevoArray#Devuelve los primeros de symbol en forma de lista
        
def getPrimeros(symbol):
    global primerosArray
    for i in primerosArray:
        if i[0] == symbol:
            return i[1]#Devuelve solo los primeros de la letra symbol
    return None

def quitar_duplicados(lista):
    return list(dict.fromkeys(lista))


#Abre archivo gramatica.txt
##ruta="gramatica.txt"#Ruta del archivo
##archivoGramatica=open(ruta,encoding="utf-8")#Usar esta codificacion para que lea lambda
###Variables
##noTerminales=archivoGramatica.readline().split()
##terminales=archivoGramatica.readline().split()
##simboloInicial = noTerminales[0]
##
##reglasProduccion=calcularReglasP(ruta,archivoGramatica,noTerminales)
###print(getProducciones("T"))
##primerosArray=[]
###primerosArray=primeros("L")
###hacer un ciclo para recorrer los no terminales y obtener sus primeros
##for i in noTerminales:#Esto debe salir en la interfaz gráfica
##    print("Primeros de ",i,":")
##    print(primeros(i))


direccionArchivo = ""
terminales=[]
noTerminales=[]
primerosArray=[]
reglasProduccion=[]

def PrimerosYSiguientes():
    font1=("Times New Roman",14)
    VentanaPrincipal =Toplevel()
    VentanaPrincipal.title("Algoritmo de primeros y siguientes")
    VentanaPrincipal.state("zoomed")
    VentanaPrincipal.config(background="#363062")
    VentanaPrincipal.iconbitmap("Compiler.ico")
    font2=("Times New Roman",20)
    archivoLabel=Label(VentanaPrincipal,text="Seleccionar Archivo:",font=font1,width=20,background="#363062",foreground="white")
    archivoLabel.place(x=60,y=30)
    frameGramatica=Frame(VentanaPrincipal,width=470,height=600)
    frameGramatica.place(x=60,y=100)
    framePrimeros=Frame(VentanaPrincipal,width=800,height=600)
    framePrimeros.place(x=550,y=100)
    archivoButton=Button(VentanaPrincipal,text="Abrir archivo",width=20,command=lambda:abrirArchivo(VentanaPrincipal,frameGramatica),bg="#F99417",font=font1)
    archivoButton.place(x=300,y=20)
    ImprimirResultad0s=Button(VentanaPrincipal,text="Imprimir Resultados",width=20,bg="#F99417",font=font1,command=lambda:ImprimirResultados(VentanaPrincipal,framePrimeros))
    ImprimirResultad0s.place(x=300,y=60)
    limpiarButton=Button(VentanaPrincipal,text="Limpiar",width=20,bg="#F99417",font=font1,command=lambda:limpiar())
    limpiarButton.place(x=700,y=60)

def abrirArchivo(Ventana,frameGramatica):
    global direccionArchivo
    Ventana.grab_set()
    username=getpass.getuser()
    ruta_proyecto = r"C:\Users\{username}\Documents\ProyectoCompiladores"
    direccionArchivo=filedialog.askopenfilename(initialdir=ruta_proyecto,title="Abrir Archivo",filetypes=(("texto","*.txt"),))
    archivoGramatica=open(direccionArchivo,encoding="utf-8")
    noTerminales=archivoGramatica.readline().split()
    terminales=archivoGramatica.readline().split()
    ImprimirGramatica(frameGramatica,direccionArchivo)
    archivoGramatica.close()
    Ventana.grab_release()

def ImprimirGramatica(FrameGramatica,ruta_proyecto):
    global lista1
    fuente=("Times New Roman",15)
    archivoGramatica=open(ruta_proyecto,encoding="utf-8")
    contador=0
    lista1=Listbox(FrameGramatica)
    lista1.config(width=45,height=30,font=fuente)
    lista1.pack()
    texto="hola"
    lista1.insert(END,"-----Gramatica:------")
    while texto!="":
        texto=archivoGramatica.readline()
        lista1.insert(END,texto)

def procesarCadenas(array):
    cadenna=""
    print(array)
    for  i in array:
        cadenna+=i
        cadenna+=" "
    return cadenna

def ImprimirResultados(Ventana,FrameResultados):
    global lista
    global direccionArchivo
    global terminales
    global noTerminales
    global reglasProduccion
    Ventana.grab_set()
    if direccionArchivo=="":

        messagebox.showerror("Error","No se ha seleccionado ningun archivo")
    else:
        
        archivoGramatica=open(direccionArchivo,encoding="utf-8")#Usar esta codificacion para que lea lambda
        noTerminales=archivoGramatica.readline().split()
        terminales=archivoGramatica.readline().split()
        reglasProduccion=calcularReglasP(direccionArchivo,archivoGramatica,noTerminales)
        fuente=("Times New Roman",15)
        lista=Listbox(FrameResultados)
        lista.config(width=45,height=30,font=fuente)
        lista.pack()
        lista.insert(END,"-----Primeros:------")
        print("Lista de producciones de primeros:", type(reglasProduccion))
        for regla in reglasProduccion:
            print(regla, type(regla))
        for i in noTerminales:#Esto debe salir en la interfaz gráfica
            regla="Primeros de "+i+": ["
            primerosText=primeros(i)
            aux=regla+procesarCadenas(primerosText)+" ]"
            print(aux)
            lista.insert(END,aux)
        direccionArchivo=""
        #lista.insert(END,"-----Siguientes:------")
        Ventana.grab_release()
        #limpiar()
        


def limpiar():
    global direccionArchivo
    global terminales
    global noTerminales
    global reglasProduccion
    global lista1
    global lista
    #direccionArchivo=""
    terminales.clear()
    noTerminales.clear()
    primerosArray.clear()
    reglasProduccion.clear()

    lista.destroy()
    lista1.destroy()

    


    



    
