
from itertools import islice
def calcularReglasP(archivo,listaNoTerminales):
    listaProducciones=[]#contiene las tuplas de las producciones
    cadena = []
    lineas = archivo.readlines()   
    #print(len(lineas))
    archivo2=open("gramatica.txt",encoding="utf-8")
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
        #print(reglaP[0],cadena)
        producciones = (reglaP[0], cadena)
        #print("hola",producciones)
        listaProducciones.append(producciones)
        #cadena.clear()
    #print(listaProducciones)
    return listaProducciones

#def getProducciones(symbol):
#    global reglasProduccion
#    aux=[]
#    for i in reglasProduccion:
#        if i[0] == symbol:
#            aux+= i[1]
#    return aux
def getProducciones(symbol):#Ya esta bien
    global reglasProduccion
    aux=[]
    for i in reglasProduccion:
        if i[0] == symbol:
            aux.append(i[1])
    return aux

def ObtenerPrimeros(noTerminales,producciones):
    primerosP=[]

def primeros(symbol):#Funcion recursiva que obtiene los primeros de un simbolo dado symbol
    global terminales, primerosArray

    if symbol in terminales or not symbol.isalpha() or symbol == "λ":#Si es terminal o lambda
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

    # Guarda los primeros calculados para este símbolo
    
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
ruta="gramatica.txt"#Ruta del archivo
archivoGramatica=open(ruta,encoding="utf-8")#Usar esta codificacion para que lea lambda
#Variables
noTerminales=archivoGramatica.readline().split()
terminales=archivoGramatica.readline().split()
simboloInicial = noTerminales[0]

reglasProduccion=calcularReglasP(archivoGramatica,noTerminales)
#print(getProducciones("T"))
primerosArray=[]
#primerosArray=primeros("L")
#hacer un ciclo para recorrer los no terminales y obtener sus primeros
for i in noTerminales:#Esto debe salir en la interfaz gráfica
    print("Primeros de ",i,":")
    print(primeros(i))

#print(primeros("L"))
