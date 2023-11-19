import re
from PrimerosYSiguientes import *
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
    simbolos_inicial = reglasProduccion[0].getBase()
    print("Simbolo inicial: ", simbolos_inicial)
    return simbolos_inicial

def obtencionSiguientes(elemento_evaluado,reglasProducccion,lista_siguientes,index,simbolo_inicial): #Recibe un arreglo de reglas de producción    
    for regla in reglasProducccion:    
        if index != -1:
            for elemento in regla.getProduccion(): 
                bandera_elemento_evaluado_encontrado = False #Se va a buscar el elemento_evaluado en la produccion de la regla

                if simbolo_inicial == elemento_evaluado and regla.getBase() == elemento_evaluado: #Caso 1 (A -> A)
                    bandera_existe = False
                    for s in lista_siguientes[index].getSiguientes():
                        if s == '$':
                            bandera_existe = True
                    if bandera_existe == False:
                            lista_siguientes[index].addSiguientes('$')
                else: #Armado de la beta y la alfa, caso dos y tres
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
                            bandera_solo_una_vez = False
                            if e.islower() == True: #Es terminal
                                bandera_solo_una_vez = True
                                
                            while (bandera_solo_una_vez == True or e.islower() == False) and contador < len(beta) :
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

                    if regla.getBase() == elemento_evaluado:
                        pass
                    else:
                        if  regla.getBase() in [s.getBase() for s in lista_siguientes]:
                            for i, s in enumerate(lista_siguientes):
                                if s.getBase() == elemento:
                                    index_enviar = i
                            obtencionSiguientes(regla.getBase(), reglasProduccion, lista_siguientes,index_enviar,simbolo_inicial)
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
                    if regla.getBase() == elemento_evaluado:
                        pass
                    else:
                        if  regla.getBase() in [s.getBase() for s in lista_siguientes]:
                            for i, s in enumerate(lista_siguientes):
                                if s.getBase() == elemento:
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


        
def getSiguientes(elemento, lista_siguientes):
    for s in lista_siguientes:
        if s.getBase() == elemento:
            return s.getSiguientes()
    return None

def SiguientesDadoSimbolo(elemento, lista_siguientes, reglasProduccion):
    pass
#__________________________________________________________________________________________________________
def cargar_pReservadas(lineas):
    for linea in lineas:
        lista_pReservadas.append(linea.strip('\n'))


#__________________________________________________________________________________________________________
def CargadoGramatica():
    listaNoTerminales = []
    listaTerminales = []
    reglasProduccion = []
    archivo2 = "gramatica2.txt"
    with open(archivo2, 'r') as file:
        lineas = file.readlines()
    
    index = 0;
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
            produccion = produccion.replace("lamda","λ")
            produccion = produccion.split(" ")
            reglasProduccion.append(reglaProduccion(base))
            for p in produccion:
                reglasProduccion[index-2].addProduccion(p.strip('\n'))
           
        index += 1
    
    return reglasProduccion, listaNoTerminales, listaTerminales
#SCRIPT____________________________________________________________________________________________________

archivo_cargado = 'palabras_reservadas.txt'
with open(archivo_cargado, 'r') as file:
    lineas = file.readlines()
    
lista_pReservadas = []
cargar_pReservadas(lineas)


reglasProduccion =[]
listaNoTerminales = []
listaTerminales = []

reglasProduccion, listaNoTerminales, listaTerminales =CargadoGramatica()

print("No terminales: ", listaNoTerminales)
print("Terminales: ", listaTerminales)

print("Gramatica cargada")
for regla in reglasProduccion:
    print(regla)

#Preparacion para obtener los siguientes
simbolo_inicial = getSimboloInicial(reglasProduccion)

#Inicializamos la lista de siguientes
lista_siguientes = []
for elemento in listaNoTerminales:
    lista_siguientes.append(Siguientes(elemento))


            
for elemento in listaNoTerminales:
    for i, s in enumerate(lista_siguientes):
        if s.getBase() == elemento:
            index = i
    obtencionSiguientes(elemento,reglasProduccion,lista_siguientes,index,simbolo_inicial)


print (len(lista_siguientes))
print("Lista de siguientes: ")
for s in lista_siguientes:
    print(s.getBase() + " -> " +"".join(s.getSiguientes()))