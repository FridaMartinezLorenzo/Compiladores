import re

class reglaProduccion:
    
    def __init__(self, b, p):
        self.base = b
        self.produccion_cadena = p
        self.produccion = []

    def getBase(self):
        return self.base

    def getProduccion(self):
        return self.produccion

    def setBase(self, b):
        self.base = b
    
    def setProduccionCadena(self, p):
        self.produccion = p
    
    def addProduccion(self, p):
        self.produccion.append(p)
        
    
    def __str__(self):
        return self.base + " -> " + self.produccion + ";"

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


def obtencionSiguientes(reglasProducccion): #Recibe un arreglo de reglas de producción
    lista_siguientes = [] #Se va a retornar

    simbolos_inicial = reglasProduccion[0].getBase()
    print("Simbolo inicial: ", simbolos_inicial)


    #Obtenemos el arreglo de los elementos a los ue les vamos a sacar siguientes
    elementos_para_siguientes = []
    for r in reglasProduccion:
        elementos_para_siguientes.append(r.getBase())
    #Hacemos un orden de prioridad de los elementos para calcular los siguientes
    nueva_lista = []
    for r in reglasProduccion:
        if r.getProduccion()[0].islower():
            #Es un terminal, se sugiere empezar por estos
            nueva_lista.append(r)
            
        
    
    
    elementos_para_siguientes = list(set(elementos_para_siguientes)) #Eliminamos los repetidos
    print("Elementos para siguientes: ", elementos_para_siguientes)    
    
    for elemento_evaluado in elementos_para_siguientes: #el elemento que estamos evaluando para obtener sus siguientes
        for i, regla in enumerate(reglasProduccion):
            index = -1
            if i>= 0 and regla.getBase() in [s.getBase() for s in lista_siguientes]:
                index = i #Se va a trabajar sobre esta posicion
            else:
                sig = Siguientes(regla.getBase())#Se crea un nuevo elemento
                lista_siguientes.append(sig)
                index = len(lista_siguientes) - 1 #Se va a trabajar sobre esta posicion

            for elemento in regla.getProduccion():
                bandera_elemento_evaluado_encontrado = False
                if elemento == simbolos_inicial and regla.getBase() == elemento_evaluado: #Primer caso (A -> A)
                    lista_siguientes[index].addSiguientes('$')

                else: #Armado de la beta y la alfa, caso dos y tres
                    alfa = []
                    beta = []

                    if elemento == elemento_evaluado:
                        bandera_elemento_evaluado_encontrado = True
                    
                    if bandera_elemento_evaluado_encontrado == False:
                        alfa.append(elemento) #Todo lo que esta antes 
                    
                    if bandera_elemento_evaluado_encontrado == True and elemento != elemento_evaluado:
                        beta.append(elemento)
            
            #Una vez obtenidos alfa y beta, evaluamos los casos dos y tres
            bandera_epsilon_encontrado_beta = False
            if bandera_elemento_evaluado_encontrado == True and beta != []: #Caso dos, no evaluamos alfa porque no la ocupamos            
                #primero = transformarPrimero(beta[0]) #Se manda el elemento que vamos a transformar en siguientes
                #if primero.find('e') != -1: #Si encontró epsilón se va a descartar       
                #    for elemento in primero:
                #        if elemento == 'e':
                #            bandera_epsilon_encontrado_beta = True
                #        else:
                #            lista_siguientes[index].addSiguientes(elemento)
                pass       
            elif bandera_elemento_evaluado_encontrado == True and beta !=[] and bandera_epsilon_encontrado_beta == True: #Caso tres
                #Siguientes de la regla que estamos evaluando se vuelven parte de los siguientes del elemento que estamos evaluando
               for k, s1 in enumerate(lista_siguientes):
                   if k>=0 and regla.getBase() in [s.getBase() for s in lista_siguientes]:
                        for s2 in lista_siguientes[k].getSiguientes():
                            lista_siguientes[index].addSiguientes(s2) #Colocamos los siguientes de B en siguientes de A S(A) <= S(B)
            
            elif bandera_elemento_evaluado_encontrado == True and beta == []: 
                for k, s1 in enumerate(lista_siguientes):
                   if k>=0 and regla.getBase() in [s.getBase() for s in lista_siguientes]:
                        for s2 in lista_siguientes[k].getSiguientes():
                            lista_siguientes[index].addSiguientes(s2) #Colocamos los siguientes de B en siguientes de A S(A) <= S(B)
                                    
    print("Lista de siguientes: ")
    for s in lista_siguientes:
        print(s.getBase() + " -> " +"".join(s.getSiguientes()))
        
    
    

#_____________________________________________________________________________________________________
def desgloceElementosProduccion(reglasProduccion, listaReservadas): #Recibe una produccion
    for regla in reglasProduccion:
        #Procedemos a buscar si existen palabras reservadas en la produccion
        for pReservada in listaReservadas:
            if regla.produccion_cadena.find(pReservada) != -1:
                #Si existe una palabra reservada en la produccion, la añadimos a la lista de elementos de la produccion
                regla.addProduccion(pReservada)
        
        #En caso de que no contenga palabras reservadas se va a proceder a desglozar la produccion elemento a elemento
        for elemento in regla.produccion_cadena:
            regla.addProduccion(elemento)      
        
        print("Produccion:" )
        for elemento in regla.produccion:
            print(elemento)                  


#__________________________________________________________________________________________________________
def cargar_pReservadas(lineas):
    for linea in lineas:
        lista_pReservadas.append(linea.strip('\n'))


#__________________________________________________________________________________________________________
#script
archivo_cargado = 'palabras_reservadas.txt'
with open(archivo_cargado, 'r') as file:
    lineas = file.readlines()
    
lista_pReservadas = []
cargar_pReservadas(lineas)



#Desglozamos la regla que entre
reglaproduccion = "A -> Aa;"
base = reglaproduccion.split("->")[0].strip() #Se retorna el primer elemento
produccion = reglaproduccion.split("->")[1].strip() #Se retorna lo que produce

#print("Regla de produccion: ", reglaproduccion)
#print("Base: ", base)
#print("produccion: ", produccion)

reglasProduccion = []
rp = reglaProduccion(base, produccion)
reglasProduccion.append(rp)

reglaproduccion2 = "B -> bA;"
base = reglaproduccion2.split("->")[0].strip() #Se retorna el primer elemento
produccion = reglaproduccion2.split("->")[1].strip() #Se retorna lo que produce
reglasProduccion.append(reglaProduccion(base, produccion))


desgloceElementosProduccion(reglasProduccion, lista_pReservadas)
obtencionSiguientes(reglasProduccion)
