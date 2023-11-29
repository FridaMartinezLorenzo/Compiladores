
from Ir_a_Algoritmo import *
from cerradura import *
class TablaColeccionCanonica:
    def __init__(self):
        self.estado = []
        self.SimboloIr_A = '-'
        self.estadoIr_A = '-'
        self.EnviadoACerradura = []
        
    #def __init__(self, estado, SimboloIr_A, estadoIr_A, EnviadoCerradura):
    #    self.estado = estado
    #    self.SimboloIr_A = SimboloIr_A
    #    self.estadoIr_A = estadoIr_A
    #    self.EnviadoACerradura = EnviadoCerradura
        
    def getEstado(self):
        return self.estado
        
    def getSimboloIr_A(self):
        return self.SimboloIr_A
    
    def getEstadoIr_A(self):
        return self.estadoIr_A
    
    def getEnviadoACerradura(self):
        return self.EnviadoACerradura
    
    def setEstado(self, estado):
        self.estado = estado
    
    def setSimboloIr_A(self, SimboloIr_A):
        self.SimboloIr_A = SimboloIr_A
    
    def setEstadoIr_A(self, estadoIr_A):
        self.estadoIr_A = estadoIr_A
    
    def setEnviadoACerradura(self, EnviadoACerradura):
        self.EnviadoACerradura = EnviadoACerradura
    
    def __str__(self):
        return "\nEstado: " + str(self.estado) + " \nSimboloIr_A: " + str(self.SimboloIr_A) + " \nEstadoIr_A: " + str(self.estadoIr_A) + " \nEnviadoACerradura: " + str(self.EnviadoACerradura) + "\n"


#Funcion reciclada de primeros
def calcularReglasP(archivo,listaNoTerminales,ruta):
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
        if produccion[1] == ['λ']:
            produccion = (produccion[0],['•'])
            #print("produccion: ", produccion)
        else:
            produccion = (produccion[0], ['•'] + produccion[1])
        listaProduccionesAux.append(produccion)
    return listaProduccionesAux

def convertirLista(Conjunto):
    for i, elemento in enumerate(Conjunto):
        Conjunto[i] = list(elemento)


def buscarEstado(lista_estados_conjuntos, conjunto_ir_a):
    for index, elemento_lista_conjuntos in enumerate(lista_estados_conjuntos):
        if conjunto_ir_a == elemento_lista_conjuntos[1]:
            #print("Ya se encontró este estado en el índice:", index)
            return index
    return -1  # Retorna -1 si no se encontró el estado

def coleccionCanonica(ConjuntoC, reglasProduccion, lista_estados_conjuntos, enumeracion_estados):
    listaCanonica = []
    
    while ConjuntoC:
        conjunto_actual = ConjuntoC.pop(0)

        #print("conjunto_actual[1]: ", conjunto_actual[1])
        for reglas in conjunto_actual[1]:
            regla = reglas[1]
            bandera_se_encontro_estado = -1
            conjunto_ir_a = []
            for i in range(len(regla)): 
                if regla[len(regla)-1] == '•' :
                    conjunto_ir_a = None
                
                elif regla[i] == '•' and regla[i+1] != None:
                    #Creamos el objeto que contiene la informacion sobre el proceso que se esta haciendo
                    nuevo_elemento_canonica = TablaColeccionCanonica()
                    nuevo_elemento_canonica.setEstadoIr_A(conjunto_actual[0])
                    nuevo_elemento_canonica.setSimboloIr_A(regla[i+1])
                    
                    #Llamamos  ala funcion Ir_a que internamente llama a la funcion cerradura
                    conjunto_ir_a = Ir_a(conjunto_actual, regla[i+1], reglasProduccion, nuevo_elemento_canonica)
                    
                    bandera_se_encontro_estado = -1
                    bandera_se_encontro_estado = buscarEstado(lista_estados_conjuntos, conjunto_ir_a)


            #Evaluamos si la bandera de busqueda de estado            
                
            if bandera_se_encontro_estado == -1:
                if (conjunto_ir_a != None and conjunto_ir_a != "Aceptacion"):
                    enumeracion_estados += 1
                    nuevo_estado = ['I' + str(enumeracion_estados), conjunto_ir_a]
                    #Insertamos en la informacion para la tabla
                    nuevo_elemento_canonica.setEstado(nuevo_estado)
                    listaCanonica.append(nuevo_elemento_canonica)
                    #Guardamos la recopilacion de todos los estados
                    lista_estados_conjuntos.append(nuevo_estado)
                    ConjuntoC.append(nuevo_estado)
                    
                if (conjunto_ir_a == "Aceptacion"):
                    listaCanonica.append(nuevo_elemento_canonica)
            if bandera_se_encontro_estado != -1:
                    #print("Ya se encontró este estado")
                    nuevo_elemento_canonica.setEstado('I'+str(bandera_se_encontro_estado))
                    listaCanonica.append(nuevo_elemento_canonica)
                    bandera_se_encontro_estado = -1
 
    return listaCanonica           
                
                    


##############################################################################################################
#Abre archivo gramatica.txt
def main(ruta):
    #global ruta

    archivoGramatica=open(ruta,encoding="utf-8")#Usar esta codificacion para que lea lambda
    ##Variables
    noTerminales=archivoGramatica.readline().split()
    terminales=archivoGramatica.readline().split()
    simboloInicial = noTerminales[0]
    noTerminales=[]
    terminales=[]
    primerosArray=[]
    reglasProduccion=[]
    reglasProduccion=calcularReglasP(archivoGramatica,noTerminales,ruta)
    #print(reglasProduccion)



    #Empieza el programa de colección canónica _________________________________________________________________
    elemento_gramatica_aumentada = [simboloInicial + "'", [simboloInicial,"$"]]
    elemento_gramatica_aumentada_aux = [simboloInicial + "'", [simboloInicial,"$"]] 
    elemento_gramatica_aumentada_aux[1].insert(0, '•')    
    print("elemento_gramatica_aumentada_aux: ",elemento_gramatica_aumentada_aux)         
    print("Enviado:",['I0',[elemento_gramatica_aumentada_aux]])
    ConjuntoC = cerradura(['I0',[elemento_gramatica_aumentada_aux]],reglasProduccion)
    print("\n\nConjuntoC: ",ConjuntoC)
    
    #Aumentar gramatica
    reglasProduccion.insert(0,elemento_gramatica_aumentada)
    gramatica_aumentada = agregarPunto(reglasProduccion)
    print("\n\nGramatica aumentada: ",gramatica_aumentada)

    reglasProduccion = [regla for regla in reglasProduccion if regla[1] != ['λ']]  #Quitamos las reglas lambda
    
    #"Preparamos el conjunto C para la coleccion canonica con el elemento inicial"
    #elemento gramatica aumentada, todas las reglas cuya base sea el simbolo inicial y el primer elemento no terminal que se encuentre como produccion de la regla
    #ConjuntoC = [['I0',[elemento_gramatica_aumentada]],reglasProduccion]
        #estadosI0 = []
        #estadosI0.append(gramatica_aumentada[0])
        #estadosI0.append(gramatica_aumentada[1])
        #aux = ['I0',estadosI0]
        #print("\n\naux: ",aux)
        #ConjuntoC = cerradura(aux,reglasProduccion)
        #print("\n\nConjuntoC: ",ConjuntoC)
    #Vamos a buscar la regla asociada a la devuelta para agregarla a C con el punto añadido
    lista_posociones_reglas = []
    #Vamos a buscar la regla asociada a la devuelta para agregarla a C con el punto añadido
    for i, regla in enumerate(gramatica_aumentada):
        for j, elemento in enumerate(ConjuntoC):
            if elemento == list(regla): 
                lista_posociones_reglas.append(i)
    print("lista_posociones_reglas: ",lista_posociones_reglas)
    
    aux = []
    for posicion in lista_posociones_reglas:
        aux.append(gramatica_aumentada[posicion]) 

    i = 0  #Inicializamos el contador de estados, se incrementa cada vez que se crea un nuevo estado
    aux_I = [   'I'+ str(i)  , aux      ] #Creamos el primer estado, el resultante de la cerradura

    ConjuntoC.clear()
    ConjuntoC.append(aux_I)

    #Nos aseguramos de que todos los elementos interiores sean listas
    for index, elemento in enumerate(ConjuntoC):
        ConjuntoC[index] = list(elemento)

        for e_index, e in enumerate(elemento[1]):
            ConjuntoC[index][1][e_index] = list(e)

    #Copiamos en la lista de estados el primer elemento de C
    lista_estados_conjuntos = []
    lista_estados_conjuntos.append(aux_I)

    #Convertimos en lista
    for index, elemento in enumerate(ConjuntoC):
        ConjuntoC[index] = list(elemento)

        for e_index, e in enumerate(elemento[1]):
            ConjuntoC[index][1][e_index] = list(e)


    ResultadosCanonica = coleccionCanonica(ConjuntoC, reglasProduccion, lista_estados_conjuntos,i)


    Estado_Inicial = TablaColeccionCanonica()
    Estado_Inicial.setEstado(lista_estados_conjuntos[0])
    Estado_Inicial.setEnviadoACerradura(gramatica_aumentada[0])
    ResultadosCanonica.insert(0,Estado_Inicial)

    #print("\n\nResultadosCanonica: _______________________________________________________________________________________ ")
    return ResultadosCanonica#regresa el resultado de la coleccion canonica


#main()