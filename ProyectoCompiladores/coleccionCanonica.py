
from Ir_a_Algoritmo import *
from cerradura import *

class TablaColeccionCanonica:
    pass



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


def buscarEstado(lista_estados_conjuntos, conjunto_ir_a):
    bandera_se_encontro_estado = False
    for elemento_lista_conjuntos in lista_estados_conjuntos:
            print("elemento_lista_conjuntos", elemento_lista_conjuntos)
            print("elemento_lista_conjunto[1]",elemento_lista_conjuntos[1])
            print("conjunto_ir_a",conjunto_ir_a)
            if conjunto_ir_a == elemento_lista_conjuntos[1]:
                print("Ya se encontró este estado")
                bandera_se_encontro_estado = True
    return bandera_se_encontro_estado

def coleccionCanonica(ConjuntoC, reglasProduccion, lista_estados_conjuntos, lista_estados, lista_elementos_para_ir_a, enumeracion_estados):
    contador = 0
    while ConjuntoC:
        conjunto_actual = ConjuntoC.pop(0)
        print("conjunto_actual POP: ", conjunto_actual)
        lista_estados.append(conjunto_actual)

        print("conjunto_actual[1]: ", conjunto_actual[1])
        for reglas in conjunto_actual[1]:
            print("reglas[1]: ", reglas[1])
            regla = reglas[1]
            bandera_se_encontro_estado = False
            conjunto_ir_a = []
            for i in range(len(regla)): 
                print("regla[i]: ", regla[i])
                if regla[len(regla)-1] == '•' :
                    conjunto_ir_a = None
                
                elif regla[i] == '•' and regla[i+1] != None:
                    conjunto_ir_a = Ir_a(conjunto_actual, regla[i+1], reglasProduccion)
                    bandera_se_encontro_estado = False
                    bandera_se_encontro_estado = buscarEstado(lista_estados_conjuntos, conjunto_ir_a)


            #Evaluamos si la bandera de busqueda de estado            
                
            #if auxiliar_conjunto_ir_a not in lista_estados_conjuntos and conjunto_ir_a != None:
            if bandera_se_encontro_estado == False:
                if (conjunto_ir_a != None):
                    enumeracion_estados += 1
                    nuevo_estado = ['I' + str(enumeracion_estados), conjunto_ir_a]
                    lista_estados.append(nuevo_estado)
                    lista_estados_conjuntos.append(nuevo_estado)
                    ConjuntoC.append(nuevo_estado)
                    print("Conjunto C con gregado: ", ConjuntoC)
            if bandera_se_encontro_estado == True:
                    print("Ya se encontró este estado")
                    bandera_se_encontro_estado = False
       # contador += 1
       # if contador == 4:
       #     break
                
                
                    


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

#"Preparamos el conjunto C para la coleccion canonica con el elemento inicial"
#elemento gramatica aumentada, todas las reglas cuya base sea el simbolo inicial y el primer elemento no terminal que se encuentre como produccion de la regla
ConjuntoC = [['I0',[elemento_gramatica_aumentada]],reglasProduccion]
#Vamos a buscar la regla asociada a la devuelta para agregarla a C con el punto añadido
lista_posociones_reglas = []

for i, regla in enumerate(reglasProduccion):
    print("ConjuntoC[1]: ",ConjuntoC[1])
    for j, elemento in enumerate(ConjuntoC[1]):
        print("elemento: ",elemento)
        if elemento == regla: 
            lista_posociones_reglas.append(i)

        
print("lista_posociones_reglas: ",lista_posociones_reglas)
aux = []
for posicion in lista_posociones_reglas:
    aux.append(gramatica_aumentada[posicion]) 

print("aux: ",aux)

#ConjuntoC = cerradura(['I0', [gramatica_aumentada[0]]],reglasProduccion)
print("\n\nConjunto C: ",ConjuntoC)
convertirLista(ConjuntoC)


i = 0
aux_I = [   'I'+ str(i)  , aux      ]
print("\n\naux_I: ", aux_I)

#ConjuntoC = [   'I'+ str(i)  , aux      ]
ConjuntoC.clear()
ConjuntoC.append(aux_I)

#Nos aseguramos de que todos los elementos interiores sean listas
for index, elemento in enumerate(ConjuntoC):
    ConjuntoC[index] = list(elemento)

    for e_index, e in enumerate(elemento[1]):
        ConjuntoC[index][1][e_index] = list(e)
        #print("e: ",ConjuntoC[index][1][e_index])

    #print("elemento conjunto C: ", ConjuntoC[index])

#Copiamos en la lista de estados el primer elemento de C
lista_estados_conjuntos = []
lista_estados_conjuntos.append(aux_I)

#Convertimos en lista
for index, elemento in enumerate(ConjuntoC):
    ConjuntoC[index] = list(elemento)

    for e_index, e in enumerate(elemento[1]):
        ConjuntoC[index][1][e_index] = list(e)

#Declaramos los otros dos estados

lista_elementos_para_ir_a = [] 
lista_estados = []

    
print("\n\nlista_estados_conjuntos: ", lista_estados_conjuntos)



coleccionCanonica(ConjuntoC, reglasProduccion, lista_estados_conjuntos, lista_estados, lista_elementos_para_ir_a,i)

#print("\n\nlista_estados_conjuntos: ", lista_estados_conjuntos)

for estado in lista_estados_conjuntos:
    print("Estado: ", estado)
