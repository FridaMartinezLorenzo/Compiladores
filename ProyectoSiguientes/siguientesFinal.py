import re
from PrimerosYSiguientesOld import *
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from itertools import islice
import getpass
from tkinter import ttk
#from PrimerosYSiguientes import direccionArchivo

lista1 =[]
lista =[]
class reglaProduccion:
    
    def __init__(self, b):
        self.base = b
        self.produccion = []

    def getBase(self):
        return self.base

    def getProduccion(self):
        return self.produccion

    def setBase(self, b):
        self.base = b
   
    
    def addProduccion(self, p):
        self.produccion.append(p)
        
    
    def __str__(self):
        cadena = self.base + " -> " 
        for p in self.produccion:
            cadena += str(p) + " "
        return cadena

class Siguientes:
    def __init__(self, base):
        self.base = base
        self.siguientes =[]
    
    def getBase(self):
        return self.base
    
    def getSiguientes(self):
        return self.siguientes
    
    def setBase(self, b):
        self.base = b
    
    def addSiguientes(self, s):
        self.siguientes.append(s)
    
#________________________________________________________________________________________________________

def getSimboloInicial(reglasProduccion):
    simbolos_inicial = reglasProduccion[0].getProduccion()[0]
    print("Simbolo inicial: ", simbolos_inicial)
    return simbolos_inicial

def obtencionSiguientes(elemento_evaluado,reglasProducccion,lista_siguientes,index,simbolo_inicial): #Recibe un arreglo de reglas de producción    
    print("Elemento evaluado: ", elemento_evaluado)
    elemento_es_elemento_inicial = False
    for regla in reglasProducccion:    
        if index != -1:
            contador_de_elementos = 0
            for elemento in regla.getProduccion(): 
                print("Elemento: ", elemento)
                print("contador: ", contador_de_elementos)
                if contador_de_elementos == 0:
                    elemento_es_elemento_inicial = True
                    
                bandera_elemento_evaluado_encontrado = False #Se va a buscar el elemento_evaluado en la produccion de la regla

                #if simbolo_inicial == elemento_evaluado and regla.getBase() == elemento_evaluado: #Caso 1 (A -> A)
                if simbolo_inicial == elemento and elemento_es_elemento_inicial == True and regla.getBase() == elemento_evaluado: 
                    bandera_existe = False
                    for s in lista_siguientes[index].getSiguientes():
                        if s == '$':
                            bandera_existe = True
                    if bandera_existe == False:
                            lista_siguientes[index].addSiguientes('$')
                 #Armado de la beta y la alfa, caso dos y tres
                alfa = []
                beta = []
                for e in regla.getProduccion():
                    if e == elemento_evaluado:
                        bandera_elemento_evaluado_encontrado = True
                    if bandera_elemento_evaluado_encontrado == False:
                        alfa.append(e) #Todo lo que esta antes
                    if bandera_elemento_evaluado_encontrado == True and e != elemento_evaluado:
                        beta.append(e)
                print("alfa: ", alfa)
                print("beta: ", beta)
                if bandera_elemento_evaluado_encontrado == True: #Encontramos el elemento_evaluado en la produccion así que hay que checar
                    bandera_epsilon_encontrado_beta = False
                    if bandera_elemento_evaluado_encontrado == True and len(beta) != 0:#Caso dos, no evaluamos alfa porque no la ocupamos
                        #Una vez obtenidos alfa y beta, evaluamos los casos dos y tres
                        print("Caso dos")
                        bandera_epsilon_encontrado_beta = False
                        contador = 0
                        for e in beta:
                            #bandera_solo_una_vez = False
                            #if e.islower() == True: #Es terminal
                            #    bandera_solo_una_vez = True
                                
                            #while (bandera_solo_una_vez == True or e.islower() == False) and contador < len(beta) :
                            while (e.islower() == False) and contador < len(beta) :
                                if e == "lamda":
                                    primeros_elemento = primeros('λ')
                                primeros_elemento = primeros(e) 
                                print("Primeros de ", e, " : ", primeros_elemento)
                                for p in primeros_elemento:
                                    if p == 'λ':
                                       bandera_epsilon_encontrado_beta = True
                                    else:
                                       bandera_existe = False #Para que no se repitan los siguientes
                                       for s in lista_siguientes[index].getSiguientes():
                                           if s == p:
                                               bandera_existe = True
                                       if bandera_existe == False:
                                               lista_siguientes[index].addSiguientes(p)
                                               print("Agregando: ", p, "a ",lista_siguientes[index].getBase())
                                contador += 1

                if bandera_elemento_evaluado_encontrado == True and len(beta) != 0 and bandera_epsilon_encontrado_beta == True: #Caso tres
                    #Siguientes de la regla que estamos evaluando se vuelven parte de los siguientes del elemento que estamos evaluando

                    #if regla.getBase() == elemento_evaluado:
                    #    pass
                    #else:
                        if  regla.getBase() in [s.getBase() for s in lista_siguientes]:
                            for i, s in enumerate(lista_siguientes):
                                if s.getBase() == elemento and len(s.getSiguientes()) == 0:
                                    index_enviar = i
                                    obtencionSiguientes(regla.getBase(), reglasProduccion, lista_siguientes,index_enviar,simbolo_inicial)
                                #Añadir a los siguientes de A los siguientes de B, porque ya estan
                
                            for s in lista_siguientes:
                                if s.getBase() == regla.getBase():
                                    for s2 in s.getSiguientes():
                                        bandera_existe = False  #Para que no se repitan los siguientes
                                        for s in lista_siguientes[index].getSiguientes():
                                            if s == s2:
                                                bandera_existe = True
                                        if bandera_existe == False:
                                                lista_siguientes[index].addSiguientes(s2)
                                        
                elif bandera_elemento_evaluado_encontrado == True and len(beta) == 0: #Caso tres parte dos
                     #Colocamos los siguientes de B en siguientes de A S(A) <= S(B)
                    #if regla.getBase() == elemento_evaluado:
                    #    pass
                    #else:
                        if  regla.getBase() in [s.getBase() for s in lista_siguientes]:
                            for i, s in enumerate(lista_siguientes):
                                if s.getBase() == elemento and len(s.getSiguientes()) == 0:
                                    index_enviar = i
                                    obtencionSiguientes(regla.getBase(), reglasProduccion, lista_siguientes,index_enviar,simbolo_inicial)
                        for s in lista_siguientes:
                            if s.getBase() == regla.getBase():
                                for s2 in s.getSiguientes():
                                    bandera_existe = False
                                    for s in lista_siguientes[index].getSiguientes():
                                        if s == s2:
                                            bandera_existe = True
                                    if bandera_existe == False:
                                            lista_siguientes[index].addSiguientes(s2)
                contador_de_elementos += 1

        
def getSiguientes(elemento, lista_siguientes):
    for s in lista_siguientes:
        if s.getBase() == elemento:
            return s.getSiguientes()
    return None


#__________________________________________________________________________________________________________
def CargadoGramatica():
    global direccionArchivo
    listaNoTerminales = []
    listaTerminales = []
    reglasProduccion = []
    archivo2 = direccionArchivo
    with open(archivo2, 'r', encoding="utf-8") as file:
        lineas = file.readlines()
    
    index = 0
    for linea in lineas:
        if index == 0:
            #Desglocamos la linea para obtener los no terminales
            print(linea)
            linea = linea.replace("\n","")
            listaNoTerminales = linea.split(" ")
            #print(listaNoTerminales)
        if index == 1:
            #Desglocamos la linea para obtener los terminales
            linea = linea.replace("\n","")
            listaTerminales = linea.split(" ")
            #print(listaTerminales)
        if index > 1:
            #procesamos las reglas
            base = linea.split("->")[0].strip() #Se retorna el primer elemento
            produccion = linea.split("->")[1].strip() #Se retorna lo que produce
            produccion = produccion.replace("λ","lamda")
            print("produccion: ", produccion)
            
            #produccion = produccion.replace("lamda","λ")
            produccion = produccion.split(" ")
            reglasProduccion.append(reglaProduccion(base))
            for p in produccion:
                reglasProduccion[index-2].addProduccion(p.strip('\n'))
           
        index += 1
    
    return reglasProduccion, listaNoTerminales, listaTerminales
#SCRIPT____________________________________________________________________________________________________


reglasProduccion =[]
listaNoTerminales = []
listaTerminales = []
lista_siguientes = []
lista=Widget
def SiguientesMain():
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

    
def ImprimirResultados(Ventana,FrameResultados):
    global lista
    Ventana.grab_set()
    reglasProduccion, listaNoTerminales, listaTerminales =CargadoGramatica()
    print("No terminales: ", listaNoTerminales)
    print("Terminales: ", listaTerminales)
    print("Gramatica cargada")
    for regla in reglasProduccion:
        print(regla)
    fuente=("Times New Roman",15)
    lista=Listbox(FrameResultados)
    lista.config(width=45,height=30,font=fuente)
    lista.pack()
    lista.insert(END,"-----Siguientes:------")
    simbolo_inicial = getSimboloInicial(reglasProduccion)
    lista_siguientes = []
    for elemento in listaNoTerminales:
        lista_siguientes.append(Siguientes(elemento))
    for elemento in listaNoTerminales:
        for i, s in enumerate(lista_siguientes):
            #if s.getBase() == elemento and len(s.getSiguientes()) == 0:
            if s.getBase() == elemento :
                index = i
        obtencionSiguientes(elemento,reglasProduccion,lista_siguientes,index,simbolo_inicial)
    print (len(lista_siguientes))
    print("Lista de siguientes: ")

    for s in lista_siguientes:
        aux=s.getBase() + " -> " +"".join(s.getSiguientes())
        lista.insert(END,aux)

    Ventana.grab_release()


def limpiar():
    global lista_siguientes
    global lista
    global lista1
    global terminales
    global noTerminales
    #global primerosArray
    global reglasProduccion
    #direccionArchivo=""
    #terminales.clear()
    #noTerminales.clear()
    #primerosArray.clear()
    reglasProduccion.clear()
    lista_siguientes.clear()
    lista.destroy()
    lista1.destroy()


def abrirArchivo(Ventana,frameGramatica):
    global direccionArchivo
    Ventana.grab_set()
    username=getpass.getuser()
    ruta_proyecto = r"C:\Users\{username}\Documents\ProyectoCompiladores"

    direccionArchivo=filedialog.askopenfilename(initialdir=ruta_proyecto,title="Abrir Archivo",filetypes=(("texto","*.txt"),))
    with open(direccionArchivo, 'r', encoding="utf-8") as file:
        lineas = file.readlines()
    abrirArchivoInterno(direccionArchivo,lineas)
    ImprimirGramatica(frameGramatica,direccionArchivo)

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
    archivoGramatica.close()