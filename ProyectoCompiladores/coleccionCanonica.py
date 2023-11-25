
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


def buscarEstado(estado, lista_estados):
    for est in lista_estados:
        if est == estado:
            return True
    return False    


def coleccionCanonica(ConjuntoC, reglasProduccion, lista_estados_conjuntos, lista_estados, lista_elementos_para_ir_a, i):
    while (ConjuntoC):
        lista_elementos_para_ir_a = []
        #Calculamos los no terminales sobre los cuales vamos a mandar a Ir_a al elemento del conjunto
        print("Conjunto C[0]: ", ConjuntoC)
        for elemento in ConjuntoC[0]: #Vamos a ir recorriendo  
                    #print("elemento: ",elemento)
                    estado = elemento[0]
                    print("estado: ",estado)
                    #Recorremos el conjunto de producciones generadas por el estado
                    #Obtenemos los simbolos que vamos a evaluar en el ir_a, es decir los simbolos después del punto


                    bandera_se_detecto_punto = False
                    print(" thisss elemento: ", elemento)
                    for elementoProducido in elemento :
                           
                           for lista_e in elementoProducido:
                                if len(lista_e) > 1:
                                    for e in lista_e:
                                        print("\nelemento de la producción de la regla:", e)

                                        if bandera_se_detecto_punto:
                                            lista_elementos_para_ir_a.append(e)
                                            bandera_se_detecto_punto = False

                                        if e == '•':
                                            bandera_se_detecto_punto = True
                                            #print("Se detecto punto")

                                #return None #Si se detecto punto en la ultima posición de la regla, no se puede hacer ir_a (No es necesario)

        lista_elementos_para_ir_a  = list(set(lista_elementos_para_ir_a))
        print("Lista de elementos a mandar a Ir_a: ", lista_elementos_para_ir_a)
        

        numero_estados = len(ConjuntoC)
        print("numero de estados: ", numero_estados)

        if len(lista_elementos_para_ir_a) != 0:
        #while ConjuntoC:
            conjunto_actual = ConjuntoC.pop(0)
            #lista_estados.append(conjunto_actual[0])

            for simbolo_gramatical in lista_elementos_para_ir_a:
                    print("Simbolo gramatical: ", simbolo_gramatical)
                    print("Conjunto actual: ", conjunto_actual)
                    conjunto_ir_a = Ir_a(conjunto_actual, simbolo_gramatical, reglasProduccion)
                    print("\nConjunto ir_a: ", conjunto_ir_a)
                    if conjunto_ir_a not in lista_estados_conjuntos and conjunto_ir_a != None:
                        i += 1
                        nuevo_estado = ['I' + str(i), conjunto_ir_a]
                        lista_estados.append(nuevo_estado)
                        lista_estados_conjuntos.append(nuevo_estado)

                        ConjuntoC.append(nuevo_estado)
                        print("Conjunto C con gregado: ", ConjuntoC)
        print("lista_estados_conjuntos: ", lista_estados_conjuntos)
        print("lista_estados: ", lista_estados)
        break;    



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
lista_estados_conjuntos.append(aux_I)
print("\n\nlista_estados_conjuntos: ", lista_estados_conjuntos)


coleccionCanonica(ConjuntoC, reglasProduccion, lista_estados_conjuntos, lista_estados, lista_elementos_para_ir_a,i)

print("\n\nlista_estados_conjuntos: ", lista_estados_conjuntos)


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
        

