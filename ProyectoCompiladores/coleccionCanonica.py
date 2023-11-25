
from Ir_a_Algoritmo import *
from cerradura import *

#Funcion reciclada de primeros
def calcularReglasP(archivo,listaNoTerminales):
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

def agregarPunto(listaProducciones):
    listaProduccionesAux = []
    for produccion in listaProducciones:
        produccion = (produccion[0], ['•'] + produccion[1])
        listaProduccionesAux.append(produccion)
    return listaProduccionesAux

def convertirLista(Conjunto):
    for i, elemento in enumerate(Conjunto):
        Conjunto[i] = list(elemento)

##############################################################################################################
#Abre archivo gramatica.txt

ruta="gramatica.txt"
archivoGramatica=open(ruta,encoding="utf-8")#Usar esta codificacion para que lea lambda
##Variables
noTerminales=archivoGramatica.readline().split()
terminales=archivoGramatica.readline().split()
simboloInicial = noTerminales[0]
noTerminales=[]
terminales=[]
primerosArray=[]
reglasProduccion=[]
reglasProduccion=calcularReglasP(archivoGramatica,noTerminales)
#print(reglasProduccion)


elemento_gramatica_aumentada = [simboloInicial + "'", [simboloInicial,"$"]]

#Aumentar gramatica
reglasProduccion.insert(0,elemento_gramatica_aumentada)
gramatica_aumentada = agregarPunto(reglasProduccion)
print("\n\nGramatica aumentada: ",gramatica_aumentada)


ConjuntoC = cerradura(['I0', [gramatica_aumentada[0]]],reglasProduccion)
print("\n\nConjunto C: ",ConjuntoC)
convertirLista(ConjuntoC)

lista_elementos_para_ir_a = [] 
lista_estados = []

i = 0
aux_I = [   'I'+ str(i)  , ConjuntoC      ]
print("\n\naux_I: ", aux_I)

ConjuntoC = []
ConjuntoC.append(aux_I)

lista_estados_conjuntos = []
lista_estados_conjuntos.append(ConjuntoC)
print("\n\nlista_estados_conjuntos: ", lista_estados_conjuntos)
while (len(ConjuntoC) > 0):
    for elemento in ConjuntoC: #Vamos a ir recorriendo  
            #print("elemento: ",elemento)
            estado = elemento[0]
            #print("estado: ",estado)
            #Recorremos el conjunto de producciones generadas por el estado
            #Obtenemos los simbolos que vamos a evaluar en el ir_a, es decir los simbolos después del punto
            #print("la regla esta en elemento[1]: ",elemento[1])
            
            
            bandera_se_detecto_punto = False
            for reglas in elemento[1]:
                   for e in reglas[1]:
                    #print("\nelemento de la producción de la regla:", e)
                    
                    if bandera_se_detecto_punto:
                        lista_elementos_para_ir_a.append(e)
                        bandera_se_detecto_punto = False
                    
                    if e == '•':
                        bandera_se_detecto_punto = True
                        #print("Se detecto punto")

                
                    #print("estado de la bandera: ", bandera_se_detecto_punto)
            #del ConjuntoC[0]                
                
    lista_elementos_para_ir_a  = list(set(lista_elementos_para_ir_a))
    print("Lista de elementos a mandar a Ir_a: ", lista_elementos_para_ir_a)

    numero_estados = len(ConjuntoC)
    print("numero de estados: ", numero_estados)
    conta = 0
    while (conta < numero_estados):
        for elemento in lista_elementos_para_ir_a:
            print("ConjuntoC[0]: ")
            resultado_Ir_a = Ir_a(ConjuntoC[0], elemento, reglasProduccion)
    conta+=1
            



'''
while (len(conjuntos_C) > 0):
    for elemento in conjuntos_C: #Vamos a ir recorriendo 
            print("elemento: ",elemento)

            base  = elemento[0] #Base de la regla de produccion
            estados = elemento[1] #Estados de la regla de produccion
            print("estados: ",estados)
            temporal = [] #Lista temporal para guardar los estados
            bandera_se_detecto_punto = bandera_se_encontro_simbolo =False

            retorno_Ir_a =[]

            for estado in estados:
                print("estado: ",estado)
                for item in estado[1]:
                    print("item :", item)
                    
                    if bandera_se_detecto_punto == True:
                        print("Se entro a ir a")
                        retorno_Ir_a = Ir_a(elemento,item)

                        if retorno_Ir_a != None:
                            #Añadimos a C
                            for elem_Ir_a in retorno_Ir_a:
                                #Recorremos C de nuevo para ver que no se repita
                                for e in conjuntos_C:
                                    print("elemento: ",elemento)
                                    b  = elemento[0] #Base de la regla de produccion
                                    edos = elemento[1] #Estados de la regla de produccion
                                    print("estados: ",estados)
                                    temp = [] #Lista temporal para guardar los estados
                                    if elem_Ir_a in [edo for edo in edos] : 
                                        conjuntos_C.append(elem_Ir_a)
                    if estado == '•':
                        bandera_se_detecto_punto = True
                        #print("Se detecto punto")
            del conjuntos_C[0]
            print("Conjunto C, cada iteracion")
 '''       
        

