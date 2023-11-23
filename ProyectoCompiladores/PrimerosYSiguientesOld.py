from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from itertools import islice
import getpass
from tkinter import ttk
from itertools import islice
from siguientesFinal import *



def calcularReglasP(ruta,lineas,listaNoTerminales):
    listaProducciones=[]#contiene las tuplas de las producciones
    cadena = []
    #print("Lineas: ",lineas)
    #lineas = archivo.readlines()   
    print(len(lineas))
    archivo2=open(str(ruta),'r',encoding="utf-8")
    archivo2.readline()#Salto de linea en el archivo
    archivo2.readline()

    #print(len(lineas))
    for l in lineas:#Obtener las producciones de cada no terminal
        cadena=[]
        reglaP = archivo2.readline().split("->")  # separa el no terminal de la produccion
        print("ReglaP: ",reglaP)
        if len(reglaP) > 1:
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


            
    print("Lista de producciones de primeros")
    print(listaProducciones)
    return listaProducciones

def getProducciones(symbol):#Ya esta bien
    global reglasProduccion1
    aux=[]
    for i in reglasProduccion1 :
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



terminales=[]
noTerminales=[]
primerosArray=[]
reglasProduccion1 = []
lista1 = []
lista = []
def abrirArchivoInterno(direccionArchivo,lineas):
    #global direccionArchivo
    ruta_proyecto = r"C:\Users\{username}\Documents\ProyectoCompiladores"
    #direccionArchivo=filedialog.askopenfilename(initialdir=ruta_proyecto,title="Abrir Archivo",filetypes=(("texto","*.txt"),))
    archivoGramatica=open(direccionArchivo,encoding="utf-8")
    global noTerminales
    #noTerminales.clear()
    noTerminales=archivoGramatica.readline().split()
    global terminales
    #terminales.clear()
    terminales=archivoGramatica.readline().split()
    archivoGramatica.close()
    global primerosArray
    global reglasProduccion1
    reglasProduccion1 = calcularReglasP(direccionArchivo,lineas,noTerminales)
    get_Primeros(reglasProduccion1)



def procesarCadenas(array):
    cadenna=""
    print(array)
    for  i in array:
        cadenna+=i
        cadenna+=" "
    return cadenna


def get_Primeros(listaProducciones):
    
    print("No terminales: ",noTerminales)
    print("Terminales: ",terminales)
    for p in listaProducciones:
         print(type(p))
         for i in range(len(p[1])):
            pinterno = p[1][i]
            print("Pinterno: ", pinterno, " ", len(pinterno))
            pinterno = pinterno.replace(" ", "")
            pinterno = pinterno.replace("\n", "")
            pinterno = pinterno.replace("\t", "")
            
            if "id" in pinterno:
                print("Hay un id en la produccion")
                pinterno = 'id'
                p[1][i] = pinterno  # Modifica el elemento original en listaProducciones
                print("Pinterno: ", pinterno, len(pinterno))
                
    print("Lista de producciones de primeros")
    print(type(listaProducciones))
    print(listaProducciones)
    
    for i in noTerminales:#Esto debe salir en la interfaz gráfica
                regla="Primeros de "+i+": [              "
                primerosText=primeros(i)
                #print("Primeros de ",i,":",primerosText)
                aux=regla+procesarCadenas(primerosText)+"            ]"
                print(aux)
                


print("Primeros de L en primeros")
print(primeros('L'))